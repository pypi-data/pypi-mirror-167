from __future__ import annotations

import numpy
from cv2 import (
    INTER_AREA,
    INTER_NEAREST,
    getPerspectiveTransform,
    resize,
    warpPerspective,
)
from numpy import array

from sand.config import CameraConfig
from sand.datatypes import CalPoints, Dimensions, EnrichedFrame, Image, Matrix
from sand.datatypes.scale import Scale
from sand.transformer.focal import FocalNormalizer


# Works with the EnrichedFrame Pointer
class Transformation:
    def __init__(
        self, camera_config: CameraConfig, output_dimension: Dimensions
    ) -> None:
        self.camera_config = camera_config
        self.output_dimensions = output_dimension
        self.input_dimensions = self.camera_config.transformation_source_resolution
        self.focal_output_dimensions = self.input_dimensions

        self.image_scale = Scale(
            self.camera_config.transformation_source_resolution,
            self.focal_output_dimensions,
        )
        self.map_scale = Scale(
            self.camera_config.transformation_target_resolution, output_dimension
        )
        self.focal = FocalNormalizer(self.camera_config.focal, self.image_scale)
        self.calpoints = self.camera_config.transformation
        self.scaled_calpoints = CalPoints(
            self.image_scale.scale_source_calpoints(self.calpoints),
            self.map_scale.scale_target_calpoints(self.calpoints),
        )
        self.matrix: Matrix = self._calc_matrix()

    def get_scale_informations(self) -> str:
        return str(self.map_scale)

    def _calc_matrix(self) -> Matrix:
        source_points, target_points = self.scaled_calpoints
        if len(target_points) == 4 and len(source_points) == 4:
            return getPerspectiveTransform(  # type: ignore[no-any-return]
                numpy.float32(source_points),  # type: ignore[arg-type]
                numpy.float32(target_points),  # type: ignore[arg-type]
            )
        return array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def get_matrix(self) -> Matrix:
        return self.matrix

    def set_cal_points(self, calpoints: CalPoints) -> None:
        self.calpoints = calpoints
        self.scaled_calpoints = self.map_scale.scale_calpoints(self.calpoints)
        self.matrix = self._calc_matrix()

    def transform_enriched_frame(self, frame: EnrichedFrame) -> None:
        focal_correct_image = self.focal.normalize_enriched_frame(frame)  # cached
        size = self.image_scale.scaled_avg_image_dimensions(focal_correct_image)
        resized_image = resize(focal_correct_image, size, INTER_AREA)
        matrix = self.get_matrix()  # cached
        frame.mapped_frame = warpPerspective(
            resized_image,
            matrix,
            self.output_dimensions,
            flags=INTER_NEAREST,
        )

    def transform_image(self, image: Image) -> Image:
        focal_correct_image = self.focal.normalize_image(image)  # cached
        size = self.image_scale.scaled_avg_image_dimensions(image)
        resized_image = resize(focal_correct_image, size, INTER_AREA)
        matrix = self.get_matrix()  # cached
        return warpPerspective(
            resized_image,
            matrix,
            self.output_dimensions,
            flags=INTER_NEAREST,
        )
