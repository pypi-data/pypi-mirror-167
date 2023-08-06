from __future__ import annotations

from copy import copy

from cv2 import INTER_AREA, resize

from sand.datatypes import Dimensions, EnrichedFrame, Image
from sand.datatypes.aerialmap import AerialMap
from sand.util.image import mask_image


def build_map(
    images: dict[str, EnrichedFrame],
    map_id: int,
    map_masks: dict[str, Image],
    map_dimension: Dimensions,
) -> AerialMap:
    """
    takes all frames of the moment and throws it in a new map object.
    than build a new representation of images, detections and las0rs
    We throw an copy of the moment dictonary in the new CraneMap Obj.
    Its like a moment recording with the correct pointer to the original Frame Obj.
    """
    images_copy = copy(images)
    terminal_map = AerialMap(
        images_copy,
        map_dimension,
        map_id,
    )

    # add images
    for camera_name, image in images_copy.items():
        if image.mapped_frame is not None:
            mapped_frame = image.mapped_frame
            mapped_frame = resize(mapped_frame, map_dimension, interpolation=INTER_AREA)
            if (
                camera_name in map_masks
                and mapped_frame.shape == map_masks[camera_name].shape
            ):
                # TODO: log if not the same shape
                mapped_frame = mask_image(
                    mapped_frame, map_masks[camera_name], camera_name
                )
            terminal_map.add_frame(mapped_frame)

    return terminal_map
