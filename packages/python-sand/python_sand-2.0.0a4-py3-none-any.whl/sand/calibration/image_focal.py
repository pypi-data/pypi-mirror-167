from __future__ import annotations

import sys
from argparse import ArgumentParser
from pathlib import Path

from cv2 import WINDOW_NORMAL, destroyAllWindows, imread, imshow, namedWindow, waitKey

from sand.config import CameraConfig, get_camera_id, get_config
from sand.datatypes import Dimensions
from sand.transformer.transformation import Transformation  # allowed
from sand.util.camera import get_path_from_camera_name
from sand.util.image import add_text_to_image, split_image

HELP_TEXT = """h -> toggle this help
s -> decrease focal by 100
w -> increase focal by 100
q -> exit"""


def find_focal(
    camera_config: CameraConfig,
    camera_name: str,
    camera_id: int,
    file_path: Path,
    split: bool = False,
) -> int:
    print(
        f"Run focal | {camera_id=} | {camera_name=} | {camera_config.focal=} | {file_path=}"
    )

    image = imread(str(file_path))
    print(f"{image.shape=}")
    show_help = False
    if split:
        image, _right = split_image(image)

    while True:
        height, width, _ = image.shape
        output_dimension = Dimensions(width=width, height=height)
        transformation = Transformation(camera_config, output_dimension)
        transformed_image = transformation.focal.normalize_image(image)
        output = (
            add_text_to_image(transformed_image, text=HELP_TEXT)
            if show_help
            else transformed_image
        )

        imshow("focal", output)

        key = waitKey(50)
        if key == ord("h"):
            show_help = not show_help
        elif key == ord("s"):
            camera_config.focal = camera_config.focal - 100
            print(camera_config.focal)
        elif key == ord("w"):
            camera_config.focal = camera_config.focal + 100
            print(camera_config.focal)
        elif key in (27, ord("q")):  # esc
            return camera_config.focal


def main() -> None:
    parser = ArgumentParser(description="yolo")

    parser.add_argument(
        "-c",
        "--camera",
        type=str,
        required=True,
        help="camera name from config",
    )
    parser.add_argument(
        "-s",
        "--split",
        default=False,
        action="store_true",
        help="split image vertikal for side by side thermal images",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config/sand_config.yaml",
        help="path to config file",
    )

    args = parser.parse_args()
    config = get_config(args.config)

    split = args.split
    camera_name = args.camera
    camera_id = get_camera_id(config, camera_name)
    camera_config = config.cameras[camera_id]
    file_path = get_path_from_camera_name(camera_name)
    namedWindow("focal", WINDOW_NORMAL)

    if camera_id < 0:
        print("no helper for camera found")
        sys.exit(3)

    new_focal = find_focal(camera_config, camera_name, camera_id, file_path, split)
    print(f"found focal {new_focal} for {camera_name}")
    print("write it manually in the config!")
    destroyAllWindows()


if __name__ == "__main__":
    main()
