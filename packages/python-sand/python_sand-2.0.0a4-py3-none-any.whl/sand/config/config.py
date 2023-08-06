from __future__ import annotations

import re
from ast import literal_eval
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from re import search
from typing import DefaultDict, List, Tuple
from xml.dom import minidom

from config_builder import BaseConfigClass
from related import (
    BooleanField,
    ChildField,
    FloatField,
    IntegerField,
    SequenceField,
    StringField,
    mutable,
)

try:
    from mlcvzoo_base.configuration.model_config import ModelConfig
except ModuleNotFoundError:
    ModelConfig = BaseConfigClass  # type: ignore[assignment, misc]

from sand.datatypes import CalPoints, CameraName, Dimensions, LidarTransformation, Point
from sand.logger import Logger
from sand.registry import RegisterAble
from sand.util.camera import get_camera_name

log = Logger("config")


def _to_points(point_tuples: list[tuple[int, int]]) -> list[Point]:
    return list(map(lambda point_tuple: Point(*point_tuple), point_tuples))


@mutable(strict=True)
class CommunicationConfig(BaseConfigClass):
    # localhost not possible because of CI and docker defaulting to ipv6 and failing there
    host: str = StringField(default="127.0.0.1")
    use_mqtt: bool = BooleanField(default=True)


@mutable(strict=True)
class CameraConfig(BaseConfigClass):
    writer_active: bool = BooleanField(default=False)
    fps: int = IntegerField(default=25)
    name: str = StringField(default="webcam")
    stream: str = StringField(default="0")
    focal: int = IntegerField(default=1500)

    metric_interval: int = IntegerField(default=10)
    interesting_source: str = StringField(default="neural")  # movement, neural
    interesting_mode: str = StringField(default="off")  # off, single, all
    is_interesting_before: int = IntegerField(default=30)
    is_interesting_after: int = IntegerField(default=30)
    stream_resolution_str: str = StringField(default="2560x1440")
    transformation_source_resolution_str: str = StringField(default="3840x2160")
    transformation_target_resolution_str: str = StringField(default="7000x8000")
    serve_stream: bool = BooleanField(default=False)
    serve_port: int = IntegerField(default=-1)
    serve_boxes: bool = BooleanField(default=False)
    image_download_link: str = StringField(default="")
    group: str = StringField(default="default")

    transformation_unit_matrix = "[(1, 1), (1, 2), (2, 2), (2, 1)]"

    transformation_source_points: str = StringField(
        default="[(1, 1), (1, 2), (2, 2), (2, 1)]"
    )
    transformation_target_points: str = StringField(
        default="[(1, 1), (1, 2), (2, 2), (2, 1)]"
    )

    @property
    def stream_resolution(self) -> Dimensions:
        return CameraConfig.__get_resolution(self.stream_resolution_str)

    @property
    def transformation_source_resolution(self) -> Dimensions:
        return CameraConfig.__get_resolution(self.transformation_source_resolution_str)

    @property
    def transformation_target_resolution(self) -> Dimensions:
        return CameraConfig.__get_resolution(self.transformation_target_resolution_str)

    @staticmethod
    def __get_resolution(resolution_str: str) -> Dimensions:
        splitted = resolution_str.split("x")
        return Dimensions(int(splitted[0]), int(splitted[1]))

    @property
    def transformation(self) -> CalPoints:
        if self.transformation_source_points == self.transformation_unit_matrix:
            return self.__get_calibration_points(
                self.transformation_source_points,
                self.transformation_target_points,
                False,
            )
        return self.__get_calibration_points(
            self.transformation_source_points,
            self.transformation_target_points,
        )

    def __get_calibration_points(
        self, source_points: str, target_points: str, scale: bool = True
    ) -> CalPoints:
        scaled_points: list[Point] = []
        for point in _to_points(literal_eval(source_points)):
            if scale:
                scaled_points.append(
                    Point(
                        int(
                            point.x
                            / self.transformation_source_resolution.width
                            * self.stream_resolution.width
                        ),
                        int(
                            point.y
                            / self.transformation_source_resolution.height
                            * self.stream_resolution.height
                        ),
                    )
                )
            else:
                scaled_points.append(Point(point.x, point.y))
        return CalPoints(
            source_points=scaled_points,
            target_points=_to_points(literal_eval(target_points)),
        )


@mutable(strict=True)
class FrameStatsConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    process_delay: int = IntegerField(default=2)


@mutable(strict=True)
class CraneMapStatsConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)


@mutable(strict=False)
class NeuralNetworkConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    demo: bool = BooleanField(default=True)
    log_detections: bool = BooleanField(default=False)
    replacement_config_path: str | None = ChildField(
        cls=str, required=False, default=None
    )
    model_config: ModelConfig | None = ChildField(
        cls=ModelConfig,
        required=False,
        default=None,
    )
    wait_time_no_image_available: float = FloatField(default=0.2)


@mutable(strict=True)
class DangerZone(BaseConfigClass):
    svg_color_object: str = StringField(default="#ff0000")
    svg_color_person: str = StringField(default="#000080")
    svg_file: str = StringField(default="images/areas.svg")

    @property
    def object_polygons(self) -> list[list[Point]]:
        return DangerZone.__load_svg(self.svg_file, self.svg_color_object)

    @property
    def person_polygons(self) -> list[list[Point]]:
        return DangerZone.__load_svg(self.svg_file, self.svg_color_person)

    @staticmethod
    @lru_cache
    def __load_svg(svg_path: str, color: str) -> list[list[Point]]:
        doc = minidom.parse(svg_path)
        view_config = doc.getElementsByTagName("sodipodi:namedview")
        unit = view_config[0].getAttribute("units")
        scale = 10 if unit == "cm" else 1
        rect_root = doc.getElementsByTagName("rect")
        polygons: list[list[Point]] = []
        for rect in rect_root:
            rect_color = rect.getAttribute("style").split(";")[2].split(":")[1]
            if color == rect_color:
                width = int(float(rect.getAttribute("width")) * scale)
                height = int(float(rect.getAttribute("height")) * scale)
                x_pos = int(float(rect.getAttribute("x")) * scale)
                y_pos = int(float(rect.getAttribute("y")) * scale)
                poly: list[Point] = [
                    Point(x_pos, y_pos),
                    Point(x_pos + width, y_pos),
                    Point(x_pos + width, y_pos + height),
                    Point(x_pos, y_pos + height),
                ]
                polygons.append(poly)
        return polygons


@mutable(strict=True)
class MapBuilderConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    output_height: int = IntegerField(default=800)
    output_width: int = IntegerField(default=700)
    calc_per_seconds_map: int = IntegerField(default=10)
    calc_per_seconds_drawings: int = IntegerField(default=10)
    danger_zones: DangerZone = ChildField(cls=DangerZone, default=DangerZone())
    draw_calibration_points: bool = BooleanField(default=False)
    scale: float = FloatField(default=0.1)
    record: bool = BooleanField(default=False)
    groups: str = SequenceField(
        cls=str,
        default=[],
        required=False,
    )
    serve_streams: bool = BooleanField(default=False)
    enricher_port: int = IntegerField(default=7998)
    builder_port: int = IntegerField(default=7999)


@mutable(strict=True)
class SensorFusionConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    output_height: int = IntegerField(default=8000)
    output_width: int = IntegerField(default=7000)
    calc_per_seconds: int = IntegerField(default=5)
    heat_map_cluster_size: int = IntegerField(default=10)
    heat_up_factor: int = IntegerField(default=1)
    cool_down_factor: int = IntegerField(default=2)
    danger_zones: DangerZone = ChildField(cls=DangerZone, default=DangerZone())
    groups: str = SequenceField(
        cls=str,
        default=[],
        required=False,
    )


@mutable(strict=True)
class TransformerImageConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    output_height: int = IntegerField(default=800)
    output_width: int = IntegerField(default=700)
    groups: str = SequenceField(
        cls=str,
        default=[],
        required=False,
    )


@mutable(strict=True)
class TransformerBoxConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    output_height: int = IntegerField(default=8000)
    output_width: int = IntegerField(default=7000)
    groups: str = SequenceField(
        cls=str,
        default=[],
        required=False,
    )


@mutable(strict=True)
class TransformerConfig(BaseConfigClass):
    image: TransformerImageConfig = ChildField(
        cls=TransformerImageConfig, default=TransformerImageConfig()
    )
    box: TransformerBoxConfig = ChildField(
        cls=TransformerBoxConfig, default=TransformerBoxConfig()
    )


@mutable(strict=True)
class MetricConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    batch_size: int = IntegerField(default=5)
    default_interval: int = IntegerField(default=5)
    influx_org: str = StringField(default="automodal")
    influx_token: str = StringField(default="supergeheimertoken")
    influx_url: str = StringField(default="localhost:8086")
    commit_in_db: bool = BooleanField(default=False)


@mutable(strict=True)
class LidarConfig(BaseConfigClass):
    writer_active: bool = BooleanField(default=False)
    name: str = StringField(default="lidar")
    compression: str = StringField(default="lz4")
    ip: str = StringField(default="127.0.0.1")
    data_port: int = IntegerField(default=2368)
    tele_port: int = IntegerField(default=8308)
    transformation_list: str = StringField(default="[0, 0, 0, 0]")
    rpm: int = IntegerField(default=600)
    active: bool = BooleanField(default=False)
    file_path: str = StringField(default="")

    @property
    def transformation(self) -> LidarTransformation:
        return LidarConfig.__get_transformation(self.transformation_list)

    @staticmethod
    @lru_cache
    def __get_transformation(transformation_list: str) -> LidarTransformation:
        data: list[float] = literal_eval(transformation_list)

        return LidarTransformation(*data)


@mutable(strict=True)
class LidarEnricherConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)


@mutable(strict=True)
class GroupConfig(BaseConfigClass):
    name: str = StringField(default="")
    offset_x: int = IntegerField(default=0)
    offset_y: int = IntegerField(default=0)
    offset_z: int = IntegerField(default=0)
    transform_x: bool = BooleanField(default=True)
    transform_y: bool = BooleanField(default=True)
    transform_z: bool = BooleanField(default=True)
    child_off: str = StringField(default="NONE")


@mutable(strict=True)
class ConfigTransformerConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    scale: float = FloatField(default=1.0)


@mutable(strict=True)
class PublisherConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    image_scale: float = FloatField(default=-1.0)
    default_image_size_str: str = StringField(default="320x240")
    slowdown_factor: int = IntegerField(default=5)
    name: str = StringField(default="SAND")
    host: str = StringField(default="0.0.0.0")
    port: int = IntegerField(default=5000)
    groups: str = SequenceField(
        cls=str,
        default=[],
        required=False,
    )

    communication: CommunicationConfig = ChildField(
        cls=CommunicationConfig,
        default=CommunicationConfig(),
        required=False,
    )

    @property
    def default_image_size(self) -> Dimensions:
        return PublisherConfig.__get_resolution(self.default_image_size_str)

    @staticmethod
    def __get_resolution(resolution_str: str) -> Dimensions:
        splitted = resolution_str.split("x")
        return Dimensions(int(splitted[0]), int(splitted[1]))


@mutable(strict=True)
class DriveWatcherConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    memory_remaining_gb: int = IntegerField(default=20)
    segment_length_secs: int = IntegerField(default=3600)
    folders: list[str] = SequenceField(cls=str, default=["recordings"])


@mutable(strict=True)
class ConverterConfig(BaseConfigClass):
    active: bool = BooleanField(default=False)
    folders: list[str] = SequenceField(cls=str, default=["recordings"])
    scan_interval_sec: int = IntegerField(default=300)
    scan_start_offset_sec: int = IntegerField(default=600)
    gpu_index: int = IntegerField(default=0)
    process_poll_interval_sec: int = IntegerField(default=10)
    delete_after_conversion: bool = BooleanField(default=False)
    speedup_visual: int = IntegerField(default=5)
    speedup_thermal: int = IntegerField(default=12)
    segment_length_sec: int = IntegerField(default=3600)


@mutable(strict=False)
class StatsConfig(BaseConfigClass):
    frames: FrameStatsConfig = ChildField(
        cls=FrameStatsConfig, default=FrameStatsConfig()
    )
    map: CraneMapStatsConfig = ChildField(
        cls=CraneMapStatsConfig, default=CraneMapStatsConfig()
    )


@mutable(strict=False)
class SandConfig(BaseConfigClass):
    cameras: list[CameraConfig] = SequenceField(
        cls=CameraConfig,
        default=[],
        required=False,
    )
    lidars: list[LidarConfig] = SequenceField(
        cls=LidarConfig,
        default=[],
        required=False,
    )
    lidar_enricher: LidarEnricherConfig = ChildField(
        cls=LidarEnricherConfig,
        default=LidarEnricherConfig(),
        required=False,
    )
    publisher: PublisherConfig = ChildField(
        cls=PublisherConfig,
        default=PublisherConfig(),
        required=False,
    )
    config_transformer: ConfigTransformerConfig = ChildField(
        cls=ConfigTransformerConfig,
        default=ConfigTransformerConfig(),
        required=False,
    )
    groups: list[GroupConfig] = SequenceField(
        cls=GroupConfig,
        default=[],
        required=False,
    )
    watcher: DriveWatcherConfig = ChildField(
        cls=DriveWatcherConfig,
        default=DriveWatcherConfig(),
        required=False,
    )
    metric: MetricConfig = ChildField(
        cls=MetricConfig,
        default=MetricConfig(),
        required=False,
    )
    converter: ConverterConfig = ChildField(
        cls=ConverterConfig,
        default=ConverterConfig(),
        required=False,
    )
    neural: NeuralNetworkConfig = ChildField(
        cls=NeuralNetworkConfig,
        default=NeuralNetworkConfig(),
        required=False,
    )
    transformer: TransformerConfig = ChildField(
        cls=TransformerConfig,
        default=TransformerConfig(),
        required=False,
    )
    map_builder: MapBuilderConfig = ChildField(
        cls=MapBuilderConfig,
        default=MapBuilderConfig(),
        required=False,
    )
    sensor_fusion: SensorFusionConfig = ChildField(
        cls=SensorFusionConfig,
        default=SensorFusionConfig(),
        required=False,
    )
    stats: StatsConfig = ChildField(
        cls=StatsConfig,
        default=StatsConfig(),
        required=False,
    )
    communication: CommunicationConfig = ChildField(
        cls=CommunicationConfig,
        default=CommunicationConfig(),
        required=False,
    )


ClassificationName = str
ClassificationId = int
DemoBoundingBox = List[int]
DemoDifficult = bool
DemoOccluded = bool
DemoContent = str
DemoScore = float
DemoBox = Tuple[
    ClassificationName,
    ClassificationId,
    DemoBoundingBox,
    DemoDifficult,
    DemoOccluded,
    DemoContent,
    DemoScore,
]


class ConstantConfig(RegisterAble):
    demo_boxes: DefaultDict[CameraName, list[DemoBox]] = defaultdict(
        lambda *x, **xx: [
            ("Person", 1, [1431, 267, 1664, 453], False, False, "", 1.0),
            ("PKW", 2, [1309, 225, 1496, 278], False, False, "", 1.0),
            ("LKW", 3, [1500, 300, 1564, 458], False, False, "", 1.0),
        ]
    )


def _get_lidar_name(lidar_file: Path) -> str:
    possible_lidar_name = search(r"(f[1-4]_l[1-3]_[l][ia])(.velo)", lidar_file.name)

    if possible_lidar_name is None:
        return "invalid"
    return possible_lidar_name.group(1)


def _get_lidar_dictionary(
    lidar_file_expression: str, playback_path: Path
) -> dict[CameraName, Path]:
    lidar_files = playback_path.glob(lidar_file_expression)
    lidar_dictionary = dict(list(map(lambda x: (_get_lidar_name(x), x), lidar_files)))

    log.d(f"Loading lidar_dictionary: {lidar_dictionary}", "_get_lidar_dictionary")
    return lidar_dictionary


def _get_camera_dictionary(
    camera_file_expression: str, playback_path: Path
) -> dict[CameraName, Path]:
    video_files = playback_path.glob(camera_file_expression)
    video_dictionary = dict(
        list(map(lambda x: (get_camera_name(x.name), x), video_files))
    )

    log.d(f"Loading video_dictionary: {video_dictionary}", "_get_video_dictionary")
    return video_dictionary


def change_to_playback_config(
    sand_config: SandConfig, playback_path: Path
) -> SandConfig:
    log.d(f"playback_path: {playback_path}", "change_to_playback_config")

    video_files = playback_path.glob(r"*/*.mp4")
    pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}_(.*)\.mp4")
    video_dictionary = dict(
        list(map(lambda x: (pattern.findall(x.name)[0], x), video_files))
    )

    if len(video_dictionary) == 0:
        video_files = playback_path.glob(r"*.jpg")
        video_dictionary = dict(
            list(map(lambda x: (x.name.split(".")[0], x), video_files))
        )

        log.d(
            f"Loading video_dictionary:  {str(video_dictionary)}",
            "change_to_playback_config",
        )

    for camera_config in sand_config.cameras:
        if camera_config.name in video_dictionary:
            camera_config.stream = (
                video_dictionary[camera_config.name].absolute().as_posix()
            )

    lidar_dictionary = _get_lidar_dictionary(
        r"f[1-4]_l[1-3]_[l][ia]/*f[1-4]_l[1-3]_[l][ia]*.velo", playback_path
    )

    log.d(
        f"Loading lidar_dictionary: {lidar_dictionary}",
        "change_to_playback_config",
    )

    for lidar_config in sand_config.lidars:
        if lidar_config.name in lidar_dictionary:
            lidar_config.file_path = lidar_dictionary[lidar_config.name].as_posix()

    return sand_config
