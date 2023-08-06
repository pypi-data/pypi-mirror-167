from __future__ import annotations

import numpy
from cv2 import BORDER_CONSTANT, CV_16SC2, INTER_LINEAR, remap
from cv2.fisheye import initUndistortRectifyMap
from numpy import array, eye

from sand.datatypes import EnrichedFrame, Image
from sand.datatypes.scale import Scale


class FocalNormalizer:

    """
    intrinsic matrix ist in unserem fall immer:
    [[focal_x, 0.0, optical_center_x], [0.0, focal_y, optical_center_x], [0.0, 0.0, 1.0]]
    focal_x = focal_y = kommt aus der Config und ist in der Regel 1400 (wir nutzen der einfachheit 1000)
    optical_center_x = width/2
    optical_center_y = height/2
    könnte aber theoretisch auch verschoben sein.
    Wir nehmen an das unsere Kameras ihre Optische Mitte auch in der Mitte haben.
    """

    def __init__(self, focal: int, scale: Scale) -> None:
        self.focal = focal
        self.scale = scale
        self.distortion_coefficients = array([[0], [0], [0], [0]], dtype=numpy.float32)

        self.camera_intrinsic_matrix = array(
            [
                [
                    self.focal * self.scale.scale_width,
                    0,
                    self.scale.output_dimension.width / 2,
                ],
                [
                    0,
                    self.focal * self.scale.scale_height,
                    self.scale.output_dimension.height / 2,
                ],
                [0, 0, 1],
            ],
            dtype=numpy.float32,
        )
        self.map_x, self.map_y = initUndistortRectifyMap(
            self.camera_intrinsic_matrix,
            self.distortion_coefficients,
            eye(3),
            self.camera_intrinsic_matrix,
            (self.scale.output_dimension.width, self.scale.output_dimension.height),
            CV_16SC2,
        )

    def _get_default_focal_map(self) -> list[list[list[int]]]:
        focal_map = []
        for outer in range(0, self.scale.output_dimension.width):
            row = []
            for inner in range(0, self.scale.output_dimension.height):
                row.append([inner, outer])
            focal_map.append(row)
        return focal_map

    def normalize_enriched_frame(self, frame: EnrichedFrame) -> Image:
        """corrects the focal distortion"""
        return remap(
            frame.frame,
            self.map_x,
            self.map_y,
            interpolation=INTER_LINEAR,
            borderMode=BORDER_CONSTANT,
        )

    def normalize_image(self, image: Image) -> Image:
        """corrects the focal distortion"""
        return remap(
            image,
            self.map_x,
            self.map_y,
            interpolation=INTER_LINEAR,
            borderMode=BORDER_CONSTANT,
        )
