from __future__ import annotations

from collections import deque
from threading import Lock
from time import sleep
from typing import Deque

from cv2 import INTER_AREA, imread, resize
from numpy import zeros
from overrides import overrides

from sand.config import SandConfig, TransformerCombinationConfig
from sand.datatypes import Dimensions, EnrichedFrame, Image
from sand.interfaces.config import ConfigurationManager, find_config
from sand.interfaces.synchronization import SandNode
from sand.interfaces.util import (
    CollectAble,
    EnrichedSubscriber,
    ImageTransformerSubscriber,
)
from sand.reader.video import FrameDecoder  # allowed
from sand.transformer.transformation import Transformation
from sand.util.config import get_camera_config_by_camera_name
from sand.util.delta import DeltaHelper
from sand.util.image import mask_image
from sand.util.per_second import PerSecondHelper


class ImageTransformer(
    SandNode,
    EnrichedSubscriber,
    CollectAble[ImageTransformerSubscriber],
    ConfigurationManager[TransformerCombinationConfig],
):  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        frame_decoder: FrameDecoder,
        camera_name: str,
        global_config: SandConfig,
        playback: bool,
    ) -> None:
        SandNode.__init__(self, global_config.communication)
        ConfigurationManager.__init__(
            self,
            self,
            global_config,
            update_pattern=f"{ConfigurationManager.__name__}/{camera_name}/data/cameras/transformation_target_points",
        )
        CollectAble.__init__(self)

        self.camera_name = camera_name

        self.queue: Deque[EnrichedFrame] = deque(maxlen=1)
        self.queue_lock = Lock()
        self.playback = playback
        self.source = FrameDecoder.__name__
        self.fps = PerSecondHelper(
            communicator=self,
            name="fps",
            device=self.config.camera.name,
            expected=self.config.camera.fps,
        )
        self.dropped = PerSecondHelper(
            communicator=self,
            name="dropped",
            device=self.config.camera.name,
            expected=self.config.camera.fps,
        )

        frame_decoder.subscribe(self)
        self.output_dimensions = Dimensions(
            self.config.transformer.image.output_width,
            self.config.transformer.image.output_height,
        )

        self.input_dimensions = self.config.camera.stream_resolution

        self.transformer_helper = Transformation(
            self.config.camera, self.output_dimensions
        )

        self.image_mask = zeros(
            (self.input_dimensions.width, self.input_dimensions.height, 3)
        )

        self.log.d(
            f"{self.transformer_helper.get_scale_informations()}, {self.transformer_helper.calpoints=}, {self.transformer_helper.scaled_calpoints=}",
            "__init__",
        )

        self.create_thread(
            target=self.work,
            args=(),
            name="image_transformer",
            start=True,
        )

    def _load_image(self, path: str, dim: Dimensions) -> Image:
        image = imread(path)
        return resize(image, (dim.width, dim.height), interpolation=INTER_AREA)

    def _load_mask(self) -> None:
        path = f"images/camera_mask/{self.camera_name}.jpg"
        try:
            self.image_mask = self._load_image(path, self.input_dimensions)
        except:  # pylint: disable=bare-except
            self.log.d(f"failed loading image mask {path}", "_load_masks")

    @overrides
    def select_config(self, global_config: SandConfig) -> TransformerCombinationConfig:
        camera_config = find_config(self.camera_name, global_config.cameras)

        assert camera_config is not None

        return TransformerCombinationConfig(camera_config, global_config.transformer)

    @overrides
    def push_frame(self, frame: EnrichedFrame) -> None:
        with self.queue_lock:
            self.dropped.add(float(len(self.queue)))
            self.queue.append(frame)

    @overrides
    def config_has_updated(self) -> None:
        self.log.d(
            "config_has_updated calculate new transformation", "config_has_updated"
        )
        self.transformer_helper.set_cal_points(self.config.camera.transformation)

    def work(self) -> None:
        """
        we only transform cameras that are in the right group.
        that way we save resources. for example the map builder only needs
        transformations of the "level3" group cameras
        but the detections of all other cameras must be transformed in any case
        """
        self.set_thread_name(self.__class__.__name__)
        self._load_mask()
        while not self.shutdown_event.is_set():
            try:
                with self.queue_lock:
                    enriched_frame = self.queue.popleft()
                delta = DeltaHelper(
                    communicator=self,
                    device_name=enriched_frame.camera_name,
                    data_id=enriched_frame.id,
                    source=[self.source],
                )
                cam_config = get_camera_config_by_camera_name(
                    self.global_config, enriched_frame.camera_name
                )
                if cam_config is None:
                    continue
                if (
                    len(self.config.transformer.image.groups) == 0
                    or cam_config.group in self.config.transformer.image.groups
                ):
                    enriched_frame.frame = mask_image(
                        enriched_frame.frame,
                        self.image_mask,
                        f"imagemask_{self.camera_name}",
                    )
                    self.transformer_helper.transform_enriched_frame(enriched_frame)
                    for subscriber in self.subscribers:
                        subscriber.push_transformed_frame(enriched_frame)
                self.fps.inc_and_publish()
                self.dropped.publish()
                delta.set_end_and_publish()
            except IndexError:
                # this is somewhat expected, as we have a configured slowdown
                sleep(1 / self.config.camera.fps)
