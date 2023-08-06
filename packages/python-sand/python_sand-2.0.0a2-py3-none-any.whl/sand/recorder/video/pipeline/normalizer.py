from __future__ import annotations

from time import time

from numpy import uint8, zeros
from overrides import overrides

from sand.config import CommunicationConfig
from sand.datatypes import EnrichedFrame
from sand.interfaces.synchronization import SandNode
from sand.interfaces.util import EnrichedSubscriber, NamedCollectAble
from sand.util.per_second import PerSecondHelper
from sand.util.time import now

from .writer import VideoWriter


class VideoNormalizer(SandNode, EnrichedSubscriber):
    _INITIAL_FRAME = EnrichedFrame(
        camera_name="init",
        timestamp=now(),
        frame=zeros(shape=[1, 1, 3], dtype=uint8),
    )

    def __init__(
        self,
        communication_config: CommunicationConfig,
        collectable: NamedCollectAble[EnrichedSubscriber],
        writer: VideoWriter,
        busy_waiting_factor: int = 10,
    ) -> None:
        SandNode.__init__(self, communication_config)
        self._writer = writer
        self._name = f"normalizer_{collectable.get_name()}"

        self._frame = VideoNormalizer._INITIAL_FRAME
        self._time_between_frames = 1 / self._writer.config.fps
        self._time_to_wait = self._time_between_frames / busy_waiting_factor
        self._fps = PerSecondHelper(
            communicator=self,
            name="fps",
            device=self._writer.config.name,
            expected=self._writer.config.fps,
        )

        self.create_thread(
            target=self._normalize,
            args=(),
            name=self._name,
        )

        collectable.subscribe(self)

    @overrides
    def push_frame(self, frame: EnrichedFrame) -> None:
        initial = self._frame is VideoNormalizer._INITIAL_FRAME
        self._frame = frame
        if initial:
            self.start_all_threads()

    def _normalize(self) -> None:
        self.set_thread_name(self._name)
        start_time = time()
        frame_count = 0

        while not self.shutdown_event.is_set():
            self._writer.push_frame(self._frame)
            frame_count += 1

            next_frame_time = start_time + frame_count * self._time_between_frames
            try:
                self._writer.stats.log_metric()
            except IndexError:
                self.log.exception("Writer thread not started yet", "normalize")

            self._fps.inc_and_publish()
            while not self.shutdown_event.is_set() and time() < next_frame_time:
                # wait on shutdown_event to recognize shutdown
                self.shutdown_event.wait(self._time_to_wait)
