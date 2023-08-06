from __future__ import annotations

from pathlib import Path

from cv2 import INTER_AREA, imread, resize
from overrides import overrides

from sand.config import MapBuilderConfig, SandConfig
from sand.datatypes import Dimensions, EnrichedFrame, EnrichedLidarPacket, Image
from sand.datatypes.aerialmap import AerialMap
from sand.interfaces.config import ConfigurationManager
from sand.interfaces.synchronization import SandNode
from sand.interfaces.util import (
    EnrichedSubscriber,
    ImageTransformerSubscriber,
    NamedCollectAble,
)
from sand.map.build import build_map
from sand.registry import get_nodes
from sand.transformer import ImageTransformer  # allowed
from sand.util.delta import DeltaHelper
from sand.util.per_second import PerSecondHelper
from sand.util.time import now
from sand.util.time_management import TimeManagement


class MapBuilder(
    SandNode,
    NamedCollectAble[EnrichedSubscriber],
    ImageTransformerSubscriber,
    ConfigurationManager[MapBuilderConfig],
):
    images: dict[str, EnrichedFrame] = {}
    fusion_status: bool = False
    packet: EnrichedLidarPacket | None = None
    map: AerialMap | None = None
    map_masks: dict[str, Image] = {}

    camera_names_to_map: list[str] = []

    def __init__(
        self,
        global_config: SandConfig,
        playback: bool,
    ):
        SandNode.__init__(self, global_config.communication)
        ConfigurationManager.__init__(self, self, global_config)
        NamedCollectAble.__init__(self)

        self.playback = playback
        image_transformer = get_nodes(ImageTransformer)
        self.source = "ImageTransformer"
        for camera in global_config.cameras:
            if camera.group in self.config.groups or len(self.config.groups) == 0:
                self.camera_names_to_map.append(camera.name)

        for transformer in image_transformer:
            transformer.subscribe(self)

        self.output_dimensions = Dimensions(
            self.config.output_width, self.config.output_height
        )

        self.input_dimensions = Dimensions(
            self.global_config.transformer.image.output_width,
            self.global_config.transformer.image.output_height,
        )

        self.time_management_map = TimeManagement(
            fps=self.config.calc_per_seconds_map,
            slowdown_factor=1,
            shutdown_event=self.shutdown_event,
        )
        # correctly it's calculations per second, but with fps the influx querys are way easier
        self.fps = PerSecondHelper(
            communicator=self,
            name="fps",
            device="all",
            expected=self.config.calc_per_seconds_map,
        )

        self.create_thread(
            target=self.work_map,
            args=(),
            name=f"wk_{self.__class__.__name__}",
            start=True,
        )

    @overrides
    def get_name(self) -> str:
        return "map_builder"

    @overrides
    def select_config(self, global_config: SandConfig) -> MapBuilderConfig:
        return global_config.map_builder

    @overrides
    def push_transformed_frame(self, frame: EnrichedFrame) -> None:
        if frame.camera_name in self.camera_names_to_map:
            self.images[frame.camera_name] = frame

    def _load_image(self, path: str, dim: Dimensions) -> Image:
        image = imread(path)
        return resize(image, (dim.width, dim.height), interpolation=INTER_AREA)

    def _load_masks(self) -> None:
        files = list(Path("images/map_mask").glob("*"))
        for file_path in files:
            try:
                image = self._load_image(file_path.as_posix(), self.output_dimensions)
                self.map_masks[file_path.name.split(".")[0]] = image
            except:  # pylint: disable=bare-except
                self.log.d(
                    f"failed loading map_mask {file_path.as_posix()}", "_load_masks"
                )

    def work_map(self) -> None:
        self.set_thread_name(f"{self.__class__.__name__}")
        map_id = 0
        self.log.d("map_builder worker thread started", "work_map")
        self._load_masks()

        while not self.shutdown_event.is_set():
            if not self.time_management_map.wait_for_next_frame():
                self.log.d("shutdown occurred", "work_map")
                break

            map_id += 1
            delta = DeltaHelper(
                communicator=self,
                device_name="all",
                data_id=map_id,
                source=[self.source],
            )
            self.map = build_map(
                self.images, map_id, self.map_masks, self.output_dimensions
            )
            frame = EnrichedFrame(self.get_name(), now(), self.map.map)
            for sub in self.subscribers:
                sub.push_frame(frame)

            self.fps.inc_and_publish()
            delta.set_end_and_publish()
