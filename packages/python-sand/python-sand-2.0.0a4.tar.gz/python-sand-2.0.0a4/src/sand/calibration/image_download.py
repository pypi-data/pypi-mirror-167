from __future__ import annotations

import urllib.request
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path

from cv2 import VideoCapture, imwrite

from sand.config import CameraConfig, get_config
from sand.util.camera import get_path_from_camera_name


def _get_stream(config: CameraConfig) -> str | int:
    try:
        return int(config.stream)
    except ValueError:
        return config.stream


def _download_stream(config: CameraConfig, path: Path) -> bool:
    try:
        image_path = get_path_from_camera_name(config.name, folder=path)
        print(f"download {config.name} from stream started")
        stream = VideoCapture(_get_stream(config))
        if not stream.isOpened():
            print(f"Could not open stream: {config=}")

        _, frame = stream.read()

        imwrite(str(image_path), frame)
        stream.release()
        return True
    except Exception as exception:  # pylint: disable=broad-except
        print(f"Error while retrieving image: {config=} | {exception}")
        if stream is not None:
            stream.release()
        return False


def _download_image_link(name: str, link: str, path: Path) -> bool:
    try:
        image_path = get_path_from_camera_name(name, folder=path)
        print(f"try download {name} from image link started | {link=}")
        urllib.request.urlretrieve(
            link,
            str(image_path),
        )
        return True
    except Exception as exception:  # pylint: disable=broad-except
        print(f"Error while retrieving image: {name=} {link=} | {exception}")
        return False


def _download(camera_configs: list[CameraConfig], path: Path) -> None:
    for config in sorted(camera_configs, key=lambda x: x.name, reverse=True):
        if _download_image_link(
            config.name,
            f"http://{config.name}/axis-cgi/jpg/image.cgi?resolution=3840x2160",
            path,
        ):
            print("download success ")
            continue
        if _download_image_link(config.name, config.image_download_link, path):
            print("download success")
            continue
        if _download_stream(config, path):
            print("download success")
            continue
        print("download failed")


def _backup_old_images(images_path: Path) -> None:
    if not images_path.exists():
        return

    print("Backing up old frames")

    folder = f"backup_{str(int(datetime.now().timestamp()))}"
    backup_path = images_path.joinpath(folder)
    backup_path.mkdir()

    for image in images_path.glob("*.jpg"):
        image.rename(backup_path.joinpath(image.name))


def main() -> None:
    parser = ArgumentParser(
        description="Tool to download/extract images from your configured "
        "stream in your config."
    )

    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="config/sand_config.yaml",
        help="Path to the config to use.",
    )
    parser.add_argument(
        "-i",
        "--images-path",
        type=str,
        default="images/cameras",
        help="Where to store the retrieved images.",
    )

    args = parser.parse_args()

    print(
        """
Attention!

This tool reads from the config. For calibration and focal correction it is
advised to use the _maximum_ resolution possible that your camera can provide,
regardless of what resolution you want to use in the production system.

Please make sure that your config contains streams to the maximum resolution
before executing this downloader-tool.
"""
    )

    images_path = Path(args.images_path)
    config = get_config(args.config)

    _backup_old_images(images_path)

    _download(config.cameras, images_path)


if __name__ == "__main__":
    main()
