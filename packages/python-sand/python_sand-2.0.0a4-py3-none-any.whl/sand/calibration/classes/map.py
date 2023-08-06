from __future__ import annotations

from copy import copy
from pathlib import Path

from cv2 import (
    COLOR_BGR2GRAY,
    FONT_HERSHEY_DUPLEX,
    INTER_AREA,
    THRESH_BINARY,
    bitwise_not,
    bitwise_or,
    cvtColor,
    imread,
    resize,
    threshold,
    warpPerspective,
)

from sand.calibration.classes.state import State
from sand.calibration.helper.transformation import calc_matrix
from sand.datatypes import Color, Dimensions, Image, Matrix, Point, Scale
from sand.transformer.focal import FocalNormalizer  # allowed
from sand.util.camera import get_path_from_camera_name
from sand.util.image import add_text_to_image, draw_x


class CalibrationMap:  # pylint: disable=too-many-instance-attributes
    camera_images: dict[str, Image] = {}
    warped_images: dict[str, Image] = {}
    warped_images_unmasked: dict[str, Image] = {}
    camera_masks: dict[str, Image] = {}
    map_masks: dict[str, Image] = {}
    show_map = True
    mask_active_camera = True

    def __init__(self, state: State, scale: float = 0.1) -> None:
        self.background_unscaled = imread("images/calibration.jpg")
        self.width = self.background_unscaled.shape[1]
        self.height = self.background_unscaled.shape[0]
        self.scale_factor = scale
        self.map_scale = Scale(
            input_dimension=Dimensions(self.width, self.height),
            output_dimension=Dimensions(
                int(self.width * scale), int(self.height * scale)
            ),
        )
        self.background = resize(
            self.background_unscaled,
            self.map_scale.scaled_image_dimensions(self.background_unscaled),
            interpolation=INTER_AREA,
        )
        self.image_scale: Scale | None = None
        self.state = state
        # stage 1
        self.image_only_map = copy(
            self.background
        )  # will updated if active camera moved, but with few seconds delay because of processing time
        self.image_only_map_work = copy(self.background)
        # stage 2
        self.active_camera_map = copy(
            self.background
        )  # active camera will be drawn over the image_only_map
        # stage 3
        self.lidar_map = copy(self.background)  # lidar points
        # stage 4
        self.enriched_map = copy(self.background)  # calibration points and Lidar

        for cam in self.state.camera_list():
            self.camera_images[cam.name] = self._load_image(
                get_path_from_camera_name(cam.name).as_posix()
            )
            self.transform_image(cam.name)
            cam.calc_corner_calibration_points()
        self._load_masks()

    def set_image_scale(self, image: Image) -> None:
        if self.image_scale is None:
            width = int(image.shape[1])
            height = int(image.shape[0])
            input_dimensions = Dimensions(width=int(width), height=int(height))
            output_dimensions = Dimensions(
                width=int(width * self.scale_factor),
                height=int(height * self.scale_factor),
            )
            self.image_scale = Scale(input_dimensions, output_dimensions)

    def _load_image(self, path: str) -> Image | None:
        image = imread(path)
        self.set_image_scale(image)
        assert self.image_scale is not None
        dim = self.image_scale.scaled_image_dimensions(image)
        return resize(image, dim, interpolation=INTER_AREA)

    def _load_map_image(self, path: str) -> Image:
        image = imread(path)
        width = int(image.shape[1] * self.map_scale.scale_width)
        height = int(image.shape[0] * self.map_scale.scale_height)
        return resize(image, (width, height), interpolation=INTER_AREA)

    def _load_masks(self) -> None:
        files = list(Path("images/map_mask").glob("*"))
        print("loadings masks")
        for file_path in files:
            try:
                image = self._load_map_image(file_path.as_posix())
                print(
                    self.map_scale.scaled_image_dimensions(image),
                )
                self.map_masks[file_path.name.split(".")[0]] = resize(
                    image,
                    self.map_scale.scaled_image_dimensions(image),
                    interpolation=INTER_AREA,
                )
            except:  # pylint: disable=bare-except
                print("fail")
        files = list(Path("images/camera_mask").glob("*"))
        for file_path in files:
            try:
                self.camera_masks[file_path.name.split(".")[0]] = self._load_image(
                    file_path.as_posix()
                )
            except:  # pylint: disable=bare-except
                pass
        print("camera_masks for: ", list(self.camera_masks.keys()))
        print("map masks for: ", self.map_masks.keys())

    @staticmethod
    def _mask_image(image: Image, mask: Image) -> Image:
        _th, mask = threshold(
            cvtColor(bitwise_not(mask), COLOR_BGR2GRAY), 253, 255, THRESH_BINARY
        )
        return bitwise_or(image, image, mask=bitwise_not(mask))

    def toggle_show_map(self) -> None:
        self.show_map = not self.show_map

    def toggle_mask_active_camera(self) -> None:
        self.mask_active_camera = not self.mask_active_camera

    def transform_image(self, camera_name: str, mask: bool = True) -> None:
        if self.image_scale is None:
            return
        cam_list = self.state.cam_list
        cam_id = 0
        for camera_id, obj in enumerate(cam_list):
            if obj.name == camera_name:
                cam_id = camera_id

        image = self.camera_images[camera_name]

        if camera_name in self.camera_masks and mask:
            image = self._mask_image(image, self.camera_masks[camera_name])

        undistorted_image = FocalNormalizer(
            int(cam_list[cam_id].focal), self.image_scale
        ).normalize_image(image)

        points = self.image_scale.scale_calpoints(
            cam_list[cam_id].corner_calibration_points
        )
        matrix: Matrix = calc_matrix(points)
        if not mask:
            self.warped_images_unmasked[camera_name] = warpPerspective(
                undistorted_image, matrix, self.map_scale.output_dimension
            )
            return
        self.warped_images[camera_name] = warpPerspective(
            undistorted_image, matrix, self.map_scale.output_dimension
        )

    def add_image(
        self, camera_name: str, map_image: Image, mask: bool = True
    ) -> Image | None:
        if (
            camera_name in self.warped_images
            or camera_name in self.warped_images_unmasked
        ):
            image = (
                self.warped_images[camera_name]
                if mask
                else self.warped_images_unmasked[camera_name]
            )
            _th, mask_image = threshold(
                cvtColor(image, COLOR_BGR2GRAY), 3, 255, THRESH_BINARY
            )
            print(f"{map_image.shape=}")
            print(f"{mask_image.shape=}")
            return image + bitwise_or(
                map_image, map_image, mask=bitwise_not(mask_image)
            )
        print(f"add_image returns None | {camera_name=}")
        return None

    # ======================================
    # stage 1

    def reset_image_only_work_map(self) -> None:
        self.image_only_map_work = copy(self.background)

    def add_image_to_image_only_map(self, camera_name: str) -> None:
        map_image = self.add_image(camera_name, self.image_only_map_work)

        if map_image is not None:
            print("image only camera map")
            self.image_only_map_work = map_image
        else:
            print("Image NONE!")

    def save_image_only_work_map(self) -> None:
        self.image_only_map = copy(self.image_only_map_work)

    # ======================================
    # stage 2

    def draw_active_camera(self) -> None:
        image = (
            copy(self.background) if not self.show_map else copy(self.image_only_map)
        )
        self.transform_image(self.state.active_cam.name, mask=self.mask_active_camera)
        combined_image = self.add_image(
            self.state.active_cam.name, image, mask=self.mask_active_camera
        )
        if combined_image is not None:
            print("active camera map")
            self.active_camera_map = combined_image
        else:
            print("Image NONE!")

    # ======================================
    # stage 3
    @staticmethod
    def draw_point(
        map_image: Image, point_x: int, point_y: int, color: tuple[int, int, int]
    ) -> None:
        if point_y < len(map_image) and point_x < len(map_image[1]):
            map_image[point_y][point_x] = color

    def draw_lidar_points(self) -> None:
        temp_map = copy(self.active_camera_map)
        point_size = int(self.width / 1000)
        if point_size <= 0:
            point_size = 1
        half_point_size = int(point_size / 2)
        for lidar_id, lidar in enumerate(self.state.lidar_list):
            color = (255, 255, 0)
            if lidar_id == self.state.active_lidar_index:
                color = (255, 0, 0)
            for point in lidar.get_2d_cloud():
                point_x = int((point[0] * 100) * self.map_scale.scale_width)
                point_y = int((point[1] * 100) * self.map_scale.scale_height)
                for x_offset in range(point_size):
                    for y_offset in range(point_size):
                        self.draw_point(
                            temp_map,
                            point_x + x_offset - half_point_size,
                            point_y + y_offset - half_point_size,
                            color,
                        )

        self.lidar_map = self.draw_lidar_center_point(temp_map)

    def draw_lidar_center_point(self, temp_map: Image) -> Image:
        map_image = temp_map
        for lidar_id, lidar in enumerate(self.state.lidar_list):
            color = Color(255, 255, 0)
            if lidar_id == self.state.active_lidar_index:
                color = Color(255, 0, 0)
            map_image = draw_x(
                map_image,
                int(
                    lidar.vlp_cloud.transformation.x * 100 * self.map_scale.scale_width
                ),
                int(
                    lidar.vlp_cloud.transformation.y * 100 * self.map_scale.scale_height
                ),
                color,
                line_width=int(20 * self.map_scale.scale_avg),
                size=int(200 * self.map_scale.scale_avg),
            )
        return map_image

    # ======================================
    # stage 4

    def enrich_map(self) -> None:
        image = copy(self.lidar_map)
        image = self.draw_calibration_points(image)
        image = self.write_info_on_map(image)
        self.enriched_map = image

    def draw_calibration_points(
        self,
        image: Image,
        draw_source: bool = False,
    ) -> Image:
        def draw(image: Image, points: list[Point]) -> Image:
            for pid, point in enumerate(points):
                if pid == self.state.active_point_index:
                    image = draw_x(
                        image,
                        int(point.x * self.map_scale.scale_width),
                        int(point.y * self.map_scale.scale_height),
                        Color(0, 0, 255),
                        line_width=int(20 * self.map_scale.scale_avg),
                        size=int(200 * self.map_scale.scale_avg),
                    )
                else:
                    image = draw_x(
                        image,
                        int(point.x * self.map_scale.scale_width),
                        int(point.y * self.map_scale.scale_height),
                        Color(0, 255, 0),
                        line_width=int(20 * self.map_scale.scale_avg),
                        size=int(200 * self.map_scale.scale_avg),
                    )
            return image

        points = self.state.active_cam.corner_calibration_points
        if draw_source:
            return draw(image, points.source_points)
        return draw(image, points.target_points)

    def write_info_on_map(self, image: Image) -> Image:
        map_image = image

        map_image = add_text_to_image(
            map_image,
            self.state.active_cam.name,
            position=Point(
                int(100 * self.map_scale.scale_width),
                int(300 * self.map_scale.scale_height),
            ),
            font_scale=10 * self.map_scale.scale_avg,
            font=FONT_HERSHEY_DUPLEX,
            color=Color(0, 0, 255),
            thickness=int(20 * self.map_scale.scale_avg),
            copy=False,
        )
        if len(self.state.lidar_list) > 0:
            map_image = add_text_to_image(
                map_image,
                self.state.lidar_list[self.state.active_lidar_index].config.name,
                font=FONT_HERSHEY_DUPLEX,
                position=Point(
                    int(100 * self.map_scale.scale_width),
                    int(600 * self.map_scale.scale_height),
                ),
                font_scale=10 * self.map_scale.scale_avg,
                color=Color(255, 0, 0),
                thickness=int(20 * self.map_scale.scale_avg),
                copy=False,
            )

        return map_image
