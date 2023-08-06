from __future__ import annotations

from sand.config import LidarConfig, SandConfig

from .collector import Vlp16Collector
from .reader import LidarReader


class LidarSystem:
    def __init__(
        self, config: LidarConfig, is_playback: bool, sand_config: SandConfig
    ) -> None:
        self.reader = LidarReader(config, is_playback, sand_config)
        # cannot use registry here, as its a specific reader
        self.collector = Vlp16Collector(self.reader, config.name, sand_config)
