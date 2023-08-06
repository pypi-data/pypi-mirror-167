"""Module for our configuration

It provides different configuration classes for the other modules. Generally the configuration class is named like the
module or the specific class for which the configuration is needed.
"""
from __future__ import annotations

from typing import cast

from config_builder import ConfigBuilder

from .config import CameraConfig as CameraConfig
from .config import ClassificationId as ClassificationId
from .config import ClassificationName as ClassificationName
from .config import CommunicationConfig as CommunicationConfig
from .config import ConstantConfig as ConstantConfig
from .config import ConverterConfig as ConverterConfig
from .config import CraneMapStatsConfig as CraneMapStatsConfig
from .config import DangerZone as DangerZone
from .config import DemoBoundingBox as DemoBoundingBox
from .config import DemoBox as DemoBox
from .config import DemoContent as DemoContent
from .config import DemoDifficult as DemoDifficult
from .config import DemoOccluded as DemoOccluded
from .config import DemoScore as DemoScore
from .config import DriveWatcherConfig as DriveWatcherConfig
from .config import FrameStatsConfig as FrameStatsConfig
from .config import GroupConfig as GroupConfig
from .config import LidarConfig as LidarConfig
from .config import LidarEnricherConfig as LidarEnricherConfig
from .config import MapBuilderConfig as MapBuilderConfig
from .config import MetricConfig as MetricConfig
from .config import NeuralNetworkConfig as NeuralNetworkConfig
from .config import PublisherConfig as PublisherConfig
from .config import SandConfig as SandConfig
from .config import SensorFusionConfig as SensorFusionConfig
from .config import StatsConfig as StatsConfig
from .config import TransformerConfig as TransformerConfig
from .config import change_to_playback_config as change_to_playback_config
from .transformer_combination_config import (
    TransformerCombinationConfig as TransformerCombinationConfig,
)


def get_config(config_path: str) -> SandConfig:
    ConstantConfig()
    config_builder = ConfigBuilder(class_type=SandConfig, yaml_config_path=config_path)
    return cast(SandConfig, config_builder.configuration)


def get_basic_transformer_combination_config() -> TransformerCombinationConfig:
    camera = CameraConfig()
    camera.stream_resolution_str = "2560x1440"
    camera.transformation_source_resolution_str = "3840x2160"
    camera.transformation_target_resolution_str = "7000x8000"
    transformer = TransformerConfig()
    return TransformerCombinationConfig(camera=camera, transformer=transformer)


def get_camera_id(sand_config: SandConfig, name: str) -> int:
    for cam_id, value in enumerate(sand_config.cameras):
        if value.name == name:
            return cam_id
    return -1
