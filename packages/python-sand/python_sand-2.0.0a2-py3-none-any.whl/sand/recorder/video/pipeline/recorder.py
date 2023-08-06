from __future__ import annotations

from sand.config import CameraConfig, CommunicationConfig
from sand.interfaces.config import find_config
from sand.interfaces.util import EnrichedSubscriber, NamedCollectAble

from .normalizer import VideoNormalizer
from .writer import VideoWriter


class VideoRecorder:
    def __init__(
        self,
        collectable: NamedCollectAble[EnrichedSubscriber],
        configs: list[CameraConfig],
        communication_config: CommunicationConfig,
        playback: bool,
    ):
        config = find_config(collectable.get_name(), configs)

        if config is None:
            raise ValueError(f"No config with name: {collectable.get_name()} found")

        if config.writer_active:
            raise ValueError(
                f"Writer is not configured as active for {collectable.get_name()}: {config.writer_active=}"
            )

        self._writer = VideoWriter(
            config,
            communication_config,
            playback,
        )

        self._normalizer = VideoNormalizer(
            communication_config,
            collectable,
            self._writer,
        )

    @classmethod
    def from_collectable(
        cls,
        collectable: NamedCollectAble[EnrichedSubscriber],
        communication_config: CommunicationConfig,
        playback: bool = False,
        fps: float = 5,
    ) -> VideoRecorder:
        # pylint: disable=unexpected-keyword-arg
        config = CameraConfig(  # type: ignore[call-arg]
            writer_active=True,
            fps=fps,
            name=collectable.get_name(),
            stream="invalid",
            interesting_mode="off",
        )

        return cls(
            collectable,
            [config],
            communication_config,
            playback,
        )
