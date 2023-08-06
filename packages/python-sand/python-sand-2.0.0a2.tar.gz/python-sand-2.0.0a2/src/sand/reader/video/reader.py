from __future__ import annotations

from datetime import datetime, timedelta
from threading import Event
from time import time
from typing import Any

from cv2 import (
    CAP_PROP_BUFFERSIZE,
    CAP_PROP_FOURCC,
    INTER_AREA,
    VideoCapture,
    VideoWriter_fourcc,
)
from cv2 import error as CVError
from cv2 import imread, resize
from overrides import overrides

from sand.config import CameraConfig
from sand.config.config import SandConfig
from sand.datatypes import Dimensions, EnrichedFrame, Image
from sand.interfaces.config import ConfigurationManager, find_config
from sand.interfaces.synchronization import SandNode
from sand.interfaces.util import EnrichedSubscriber, NamedCollectAble
from sand.util.delta import DeltaHelper
from sand.util.per_second import PerSecondHelper
from sand.util.time import now

from .stats import ReaderStatistics


class _CannotOpenStreamException(Exception):
    pass


class _ImageCapture(VideoCapture):  # type: ignore[misc]
    """Convenience class so the image replay doesn't give as many errors."""

    _image: Image

    def __init__(
        self,
        path: str,
        resize_dimension: Dimensions,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self._image = resize(imread(path), resize_dimension, interpolation=INTER_AREA)
        super().__init__(*args, **kwargs)

    def isOpened(self) -> bool:  # pylint: disable=invalid-name
        return True

    def set(self, *_: Any) -> None:
        pass

    def release(self) -> None:
        pass

    def getExceptionMode(self) -> str:  # pylint: disable=invalid-name
        return "static jpeg mode"

    def grab(self) -> bool:
        return True

    def retrieve(
        self, image: Any = None, flag: Any = None  # pylint: disable=unused-argument
    ) -> tuple[bool, Image]:
        return True, self._image


class CameraReader(
    SandNode,
    NamedCollectAble[EnrichedSubscriber],
    ConfigurationManager[CameraConfig],
):
    """Your basic everyday stream readerself.

    This class can record anything that is opencv understandable. Our own
    general use-cases were mainly 'rtsp'- and 'jpg'-"streams", but also a direct
    webcam access via an integer (i.e. your webcam is accessible on opencv with
    the int `0`) is possible and supported.

    The class has basically two blocks that are interesting and work on two
    layers.

    The outer layer is `_open_camera`. It manages the actual `VideoCapture`
    and the basic settings around that. If the inner layer fails the outer one
    will catch most of it and try to recover, mainly by opening a new capture.

    The inner layer is `_record_stream`. This is the actual getter of frames and
    will get the capture from the outer layer. It will create `EnrichedFrame`s
    from the images and push them to `subscribers`. If the capture returns an
    invalid grab or retrieve, the function will return to the outer layer for a
    possible recovery.
    This generally can happen due to a number of reasons from network problems
    to the stream beeing broken completely. This happens "often" when you
    playback videos. If your video file is finished the grab will say that it
    doesn't have another frame. The inner layer will return and the outer layer
    "recovers" by opening the file in a new `VideoCapture` restarting the
    playback and looping the video.

    While in `playback` mode we could be immensely faster than any real world
    camera could ever be. So when in playback mode we try to honour the set fps
    in the config as close as possible and therefore idle a little bit.

    In general usage we also create a number of logs that could be useful. After
    around 1 minute the logs get much more infrequent (around every 10 min) to
    not overwhelm the reader with the same logs.
    """

    def __init__(
        self,
        global_config: SandConfig,
        device_name: str,
        playback: bool,
    ) -> None:
        SandNode.__init__(self, global_config.communication)
        ConfigurationManager.__init__(
            self,
            self,
            global_config,
            update_pattern=f"{ConfigurationManager.__name__}/{device_name}/data/cameras/stream",
        )
        NamedCollectAble.__init__(self)

        self._name = device_name
        self._fps = self.config.fps
        # log intermediary statistic every {self.fps}-frames in the first minute
        self._verbose_log_frame_count = self._fps * 60

        # after that log them once every 10 minutes
        self._non_verbose_log_frame_count = self._fps * 60 * 10

        self._playback = playback
        self._next_metric: datetime

        self._stats = ReaderStatistics(self.config, self)

        self._stream_updated = Event()

        self.create_thread(
            target=self._open_camera,
            args=(),
            name=f"r_{self._name}",
            start=False,
        )

        self._fps_per_second_helper = PerSecondHelper(
            communicator=self,
            name="fps",
            device=self._name,
            expected=self._fps,
        )

    @overrides
    def select_config(self, global_config: SandConfig) -> CameraConfig:
        config = find_config(self._name, global_config.cameras)
        assert config is not None, f"Got no CameraConfig for {self._name}"
        return config

    @overrides
    def config_has_updated(self) -> None:
        self._stream_updated.set()

    @overrides
    def get_name(self) -> str:
        return self._name

    def start(self) -> None:
        """This method start all threads that were prepared in `__init__`."""
        self.start_all_threads()

    def _should_log_intermediary_stats(self) -> bool:
        if self._stats.recorded_frames < self._verbose_log_frame_count:
            return not self._stats.recorded_frames % self._fps

        return not self._stats.recorded_frames % self._non_verbose_log_frame_count

    def _get_stream(self) -> str | int:
        stream = self.config.stream

        try:
            return int(stream)
        except ValueError:
            return stream

    def _get_capture(self) -> VideoCapture:
        fct = "_get_capture"
        stream = self._get_stream()

        if str(stream).endswith(".jpg"):
            self.log.d(f"Opening stream with ImageCapture: {stream}", fct)
            capture = _ImageCapture(
                str(stream), resize_dimension=self.config.stream_resolution
            )
        else:
            self.log.d(f"Opening stream with VideoCapture: {stream}", fct)
            capture = VideoCapture(stream)

        if not capture.isOpened():
            self.log.w(f"Error when opening stream: {stream}", fct)
            raise _CannotOpenStreamException()

        stream_buffer_size = 1
        capture.set(CAP_PROP_BUFFERSIZE, stream_buffer_size)
        capture.set(CAP_PROP_FOURCC, VideoWriter_fourcc("M", "J", "P", "G"))

        return capture

    def _stream_logging(self, successful_grab: bool, successful_retrieve: bool) -> None:
        if not successful_grab or not successful_retrieve:
            self.log.w(
                "Stream could not read frame, increasing dropped_frames and trying again, "
                f"successful_grab: {successful_grab} | successful_retrieve: {successful_retrieve}",
                "_stream_logging",
            )
            self._stats.add_dropped_frame()

        self._stats.log_metric()
        self._fps_per_second_helper.inc_and_publish()

    def _open_camera(self) -> None:
        self.set_thread_name(f"CR_{self._name}")
        fct = "open_cam"
        try:
            while not self.shutdown_event.is_set():
                try:
                    stream = self._get_capture()
                except _CannotOpenStreamException:
                    self.shutdown_event.wait(1)
                    continue

                (
                    successful_grab,
                    successful_retrieve,
                ) = self._record_stream(stream)

                stream.release()

                self._stream_logging(successful_grab, successful_retrieve)
        except CVError:
            self.log.exception("Critical error while reading from camera", fct)

        self.log.w(f"Shutting down CameraReader for {self._name}", fct)
        self._stats.log_metric()

    def _publish(
        self,
        frame: Image,
        successful_grab: bool,
        successful_retrieve: bool,
        after_retrieve: datetime,
    ) -> None:
        if not successful_grab or not successful_retrieve:
            return

        enriched_frame = EnrichedFrame(self._name, now(), frame)
        delta = DeltaHelper(
            communicator=self,
            device_name=self._name,
            data_id=enriched_frame.id,
            source=["none"],
        )
        delta.set_start(after_retrieve.timestamp())
        for subscriber in self.subscribers:
            subscriber.push_frame(enriched_frame)
        delta.set_end_and_publish()

    def _record_stats(  # pylint: disable=too-many-arguments
        self,
        stream: VideoCapture,
        after_grab: datetime,
        after_retrieve: datetime,
        before_grab: datetime,
        successful_grab: bool,
        successful_retrieve: bool,
    ) -> None:
        self._stats.add_grab_time(after_grab - before_grab)
        self._stats.add_retrieve_time(after_retrieve - after_grab)
        self._stats.add_frame()

        if self._should_log_intermediary_stats():
            self._stats.log_statistics(successful_grab, successful_retrieve, stream)

    def _wait_for_playback(self, segment_start: datetime) -> None:
        next_frame_time = (
            segment_start.timestamp() + self._stats.recorded_frames / self._fps
        )

        playback_wait_time = 1 / self._fps / 10
        while time() < next_frame_time and not self.shutdown_event.is_set():
            self.shutdown_event.wait(playback_wait_time)

    def _record_stream(self, stream: VideoCapture) -> tuple[bool, bool]:
        successful_retrieve = True
        successful_grab = True
        segment_start = now()
        self._next_metric = now() + timedelta(seconds=self.config.metric_interval)

        while (
            successful_grab and successful_retrieve and not self.shutdown_event.is_set()
        ):
            before_grab = now()
            successful_grab = stream.grab()
            after_grab = now()
            successful_retrieve, frame = stream.retrieve()
            after_retrieve = now()

            self._publish(
                frame,
                successful_grab,
                successful_retrieve,
                after_retrieve,
            )

            self._record_stats(
                stream,
                after_grab,
                after_retrieve,
                before_grab,
                successful_grab,
                successful_retrieve,
            )

            # for playback we will force the reader to $fps
            if self._playback:
                self._wait_for_playback(segment_start)

            self._stats.time_for_one_frame = now() - before_grab

            if now() > self._next_metric:
                self._stats.log_metric()
                self._next_metric = now() + timedelta(
                    seconds=self.config.metric_interval
                )

            if self._stream_updated.is_set():
                self._stream_updated.clear()
                return True, True

        return successful_grab, successful_retrieve
