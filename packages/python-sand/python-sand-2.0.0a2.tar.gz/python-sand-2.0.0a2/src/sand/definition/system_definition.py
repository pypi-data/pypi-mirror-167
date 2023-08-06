from __future__ import annotations

from functools import partial
from pathlib import Path
from typing import cast

import prctl
from config_builder import ConfigBuilder

from sand.config import (
    CameraConfig,
    ConstantConfig,
    SandConfig,
    change_to_playback_config,
)
from sand.config.helpers import (
    is_box_transformer_active,
    is_camera_isolated,
    is_camera_writer_active,
    is_config_transformer_active,
    is_converter_active,
    is_drive_watcher_active,
    is_fusion_active,
    is_image_transformer_active,
    is_lidar_active,
    is_lidar_packet_enricher_active,
    is_lidar_writer_active,
    is_map_active,
    is_metric_active,
    is_neural_active,
    is_publisher_active,
)
from sand.datatypes import Dimensions
from sand.interfaces.synchronization import Isolator
from sand.logger import Logger
from sand.reader.video import CameraSystem  # allowed
from sand.util import chunk
from sand.util.config_publisher import publish_config
from sand.view.stream import StreamServer  # allowed

# pylint: disable=import-outside-toplevel


def _is_primary_system(process_index: int, process_count: int) -> bool:
    return process_count == -1 or process_index == 0


def _start_camera_system(
    camera_config: CameraConfig, sand_config: SandConfig, is_playback: bool
) -> CameraSystem:
    log = Logger("camera system")
    camera_system = CameraSystem(camera_config, sand_config, is_playback)
    log.d("camera system is up", camera_config.name)
    if is_camera_writer_active(camera_config):
        from sand.recorder.video import VideoRecorder

        VideoRecorder(
            camera_system.reader,
            sand_config.cameras,
            sand_config.communication,
            is_playback,
        )
        log.d("camera recorder is up", camera_config.name)

    camera_system.start()
    return camera_system


def _start_debug_system(sand_config: SandConfig, is_playback: bool) -> None:
    log = Logger("debug system")

    log.d("Building debug system", "_start_debug_system")
    for camera_config in sand_config.cameras:
        if is_image_transformer_active(sand_config):
            from sand.reader.video import FrameDecoder

            decoder = FrameDecoder(camera_config, sand_config.communication)
            from sand.transformer import ImageTransformer

            ImageTransformer(decoder, camera_config.name, sand_config, is_playback)

    log.d("Decoder and transformer are up", "_start_debug_system")

    # start after Transformer
    # depents on boxtransformer, Imagetransformer, Fusion, LidarPacketEnricher
    if is_map_active(sand_config):
        from sand.map import MapBuilder, MapEnricher

        dimension = Dimensions(
            sand_config.map_builder.output_width, sand_config.map_builder.output_height
        )

        builder = MapBuilder(sand_config, is_playback)
        enricher = MapEnricher(sand_config, is_playback, builder)

        if sand_config.map_builder.serve_streams:
            StreamServer(
                "map_builder",
                sand_config.map_builder.builder_port,
                dimension,
                sand_config.communication,
                builder,
            )
            StreamServer(
                "map_enricher",
                sand_config.map_builder.enricher_port,
                dimension,
                sand_config.communication,
                enricher,
            )

        if sand_config.map_builder.record:
            from sand.recorder.video import VideoRecorder

            VideoRecorder.from_collectable(enricher, sand_config.communication)
            VideoRecorder.from_collectable(builder, sand_config.communication)

        log.d("MapBuilder is up", "_start_debug_system")


def _start_publisher(sand_config: SandConfig) -> None:
    log = Logger("debug system")

    # start after all CollectAbles
    if is_publisher_active(sand_config):
        from sand.view.frontend import Publisher

        Publisher(sand_config)

    log.d("Publisher is up", "_start_debug_system")
    prctl.set_proctitle("SAND_publisher")


def _start_multi_gpu_camera_system(
    sand_config: SandConfig,
    is_playback: bool,
    process_index: int,
    process_count: int,
) -> None:
    log = Logger("multi gpu camera starter")
    fct = "_start_multi_gpu_camera_system"

    camera_indices = chunk(
        sand_config.cameras,
        process_count,
        process_index,
    )

    camera_systems: list[CameraSystem] = []
    for camera_index in camera_indices:

        camera_config = sand_config.cameras[camera_index]
        if is_camera_isolated(sand_config):
            log.d(f"start camera isolated: {camera_config.name}", fct)
            Isolator(
                target=partial(
                    _start_camera_system,
                    camera_config=camera_config,
                    sand_config=sand_config,
                    is_playback=is_playback,
                ),
                global_config=sand_config,
                name=f"b_{camera_config.name}",
            )
        else:
            log.d(f"start camera: {camera_config.name}", fct)
            camera_systems.append(
                _start_camera_system(
                    camera_config=camera_config,
                    sand_config=sand_config,
                    is_playback=is_playback,
                )
            )
        if is_box_transformer_active(sand_config):
            from sand.transformer import BoxTransformer

            Isolator(
                target=partial(
                    BoxTransformer,
                    camera_name=camera_config.name,
                    global_config=sand_config,
                    playback=is_playback,
                ),
                global_config=sand_config,
                name=f"b_{camera_config.name}",
            )

    log.d("cameras are up", fct)
    if is_neural_active(sand_config):
        log.d("neural net setup", fct)
        from sand.neural import NeuralNetwork

        NeuralNetwork([cs.reader for cs in camera_systems], sand_config)
        log.d("neural net is up", "_start_multi_gpu_camera_system")


def _start_lidar(sand_config: SandConfig, is_playback: bool) -> None:
    for lidar_config in sand_config.lidars:
        if is_lidar_active(lidar_config):
            from sand.reader.lidar import LidarSystem

            lidar = LidarSystem(lidar_config, is_playback, sand_config)
            if is_lidar_writer_active(lidar_config):
                from sand.recorder.lidar import LidarRecorder

                LidarRecorder(
                    lidar, lidar_config, sand_config.communication, is_playback
                )
    if is_lidar_packet_enricher_active(sand_config):
        from sand.reader.lidar import LidarPacketEnricher

        LidarPacketEnricher(sand_config)


def start_primary_system(sand_config: SandConfig, is_playback: bool) -> None:
    Isolator(
        target=lambda: _start_lidar(sand_config, is_playback),
        global_config=sand_config,
        name="lidar",
    )
    Isolator(
        target=lambda: _start_debug_system(sand_config, is_playback),
        global_config=sand_config,
        name="debug_system",
    )
    Isolator(
        target=lambda: _start_publisher(sand_config),
        global_config=sand_config,
        name="publisher",
    )
    # start after DriverWatcher
    if is_converter_active(sand_config):
        from sand.converter import Converter

        Isolator(
            target=lambda: Converter(sand_config),
            global_config=sand_config,
            name=Converter.__name__,
        )
    if is_metric_active(sand_config):
        from sand.metric import Committer, DeltaCollector

        Isolator(
            target=partial(DeltaCollector, global_config=sand_config),
            global_config=sand_config,
            name=DeltaCollector.__name__,
        )
        Isolator(
            target=lambda: Committer(sand_config),
            global_config=sand_config,
            name=Committer.__name__,
        )
    # start after lidar and camera
    if is_fusion_active(sand_config):
        from sand.sensor_fusion import SensorFusion

        Isolator(
            target=lambda: SensorFusion(sand_config),
            global_config=sand_config,
            name=SensorFusion.__name__,
        )

    # start after lidar and camera
    if is_config_transformer_active(sand_config):
        from sand.transformer.pipeline.config import ConfigTransformer

        Isolator(
            target=lambda: ConfigTransformer(sand_config),
            global_config=sand_config,
            name=ConfigTransformer.__name__,
        )


def define_system(
    config: Path,
    playback_path: Path | None,
    process_index: int = -1,
    process_count: int = -1,
) -> None:
    fct = "start"
    log = Logger(f"system[{process_index=}]")
    is_playback = playback_path is not None

    log.i(
        f"{config=} | {playback_path=} | {process_count=} | {process_index=}",
        fct,
    )

    ConstantConfig()
    config_builder = ConfigBuilder(
        class_type=SandConfig, yaml_config_path=config.as_posix()
    )
    sand_config = cast(SandConfig, config_builder.configuration)

    if is_playback:
        sand_config = change_to_playback_config(sand_config, playback_path)  # type: ignore[arg-type]

    if _is_primary_system(process_index, process_count):
        publish_config(sand_config)
        log.i("Configuration published to mqtt", fct)
    log.d(
        f"""sand_config.cameras: {', '.join(map(str, sand_config.cameras))}
        sand_config.lidars: {', '.join(map(str, sand_config.lidars))}
        {sand_config.publisher=}
        {sand_config.watcher=}
        {sand_config.metric=}
        {sand_config.converter=}
        {sand_config.neural=}
        {sand_config.transformer=}
        {sand_config.map_builder=}
        Starting nodes...
        """,
        fct,
    )

    if _is_primary_system(process_index, process_count) and is_drive_watcher_active(
        sand_config
    ):
        from sand.watcher import DriveWatcher

        Isolator(
            target=lambda: DriveWatcher(sand_config),
            global_config=sand_config,
            name=DriveWatcher.__name__,
        )

    _start_multi_gpu_camera_system(
        sand_config,
        is_playback,
        process_index,
        process_count,
    )

    if _is_primary_system(process_index, process_count):
        start_primary_system(sand_config, is_playback)

    log.i("Finished startup", fct)

    prctl.set_proctitle(f"SAND_Main[{process_index=}]")
