from __future__ import annotations

import logging
import pickle
import re
import sys
from argparse import ArgumentParser
from functools import partial
from operator import itemgetter
from threading import Thread
from time import sleep
from typing import Any

from paho.mqtt.client import Client, MQTTMessage, topic_matches_sub

from sand.interfaces.communication import get_client_with_reconnect

_TOPIC_LIST: dict[
    str,
    tuple[str, bool, str, type[Any], Any],
] = {}


def _on_message(
    _: Client,
    __: None,
    msg: MQTTMessage,
    ignore_topics: list[str] | None = None,
    collect_topics: bool = False,
) -> None:
    collection_topic = re.sub(
        r"^MQTTLogger/[^/]*",
        "MQTTLogger/+",
        re.sub(r"^ShutdownAble/[^/]*", "ShutdownAble/+", msg.topic),
    )
    if collect_topics and collection_topic not in _TOPIC_LIST:
        found_datatype: str = str(None)
        try:
            for prop in msg.properties.UserProperty:
                if prop[0] == "datatype":
                    found_datatype = str(prop[1])
                    break
        except AttributeError:
            found_datatype = "no properties"

        try:
            payload_example = pickle.loads(msg.payload)
        except (EOFError, pickle.UnpicklingError):
            payload_example = msg.payload.decode()

        calculated_type = type(payload_example)

        _TOPIC_LIST[collection_topic] = (
            collection_topic,
            msg.retain,
            found_datatype,
            calculated_type,
            payload_example,
        )

    if ignore_topics is not None:
        if any(
            map(
                partial(
                    topic_matches_sub,
                    topic=msg.topic,
                ),
                ignore_topics,
            ),
        ):
            return

    try:
        try:
            print(f"topic: {msg.topic} | p_message:", pickle.loads(msg.payload))
        except (EOFError, pickle.UnpicklingError):
            print(f"topic: {msg.topic} | s_message:", msg.payload)
    except Exception as exception:  # pylint: disable=broad-except
        print(
            f"Exception on topic: {msg.topic} | exception:", type(exception), exception
        )


def _on_logging_message(
    _: Client,
    __: None,
    msg: MQTTMessage,
    ignore_topics: list[str] | None = None,
) -> None:
    if ignore_topics is not None:
        if any(
            map(
                partial(
                    topic_matches_sub,
                    topic=msg.topic,
                ),
                ignore_topics,
            ),
        ):
            return

    try:
        print(msg.payload.decode())
    except Exception as exception:  # pylint: disable=broad-except
        print(
            f"Exception on topic: {msg.topic}  | payload: {msg.payload} | exception:",
            type(exception),
            exception,
        )


def _kill_client(time: int, client: Client) -> None:
    sleep(time)
    client.disconnect()


def _truncate_message(msg: str, max_len: int = 100, suffix: str = "...") -> str:
    if len(msg) < max_len:
        return str(msg)

    return msg[:max_len] + suffix


def _print_summary() -> None:
    print(
        """
#############################
# Topic Summary start
# Topic | Retained | Property-Type | Calculated-Type | Example Message
#############################
"""
    )

    for _, summary in sorted(_TOPIC_LIST.items(), key=itemgetter(0)):
        print(
            f"{summary[0]} | {bool(summary[1])} | {summary[2]} | {summary[3]} | "
            f"{_truncate_message(str(summary[4]))}"
        )

    print(
        """
#############################
# Topic Summary ended
# Topic | Retained | Property-Type | Calculated-Type | Example Message
#############################
"""
    )


def _listen(  # pylint: disable=too-many-arguments
    host: str,
    topic: str,
    ignore_topics: list[str],
    logger: bool,
    time: int,
    summary: bool,
) -> None:
    client = get_client_with_reconnect()

    if logger and any(map(lambda t: not t.startswith("log"), ignore_topics)):
        print(
            "Logger mode but ignored topics outside of logging topics, clearing ignored topics"
        )
        ignore_topics = []

    client.on_message = partial(
        _on_logging_message if logger else _on_message,  # type: ignore[arg-type]
        ignore_topics=ignore_topics,
        collect_topics=summary,
    )
    client.connect(host)
    client.subscribe(topic)

    if time > 0:
        thread = Thread(target=_kill_client, args=(time, client))
        thread.start()

    print(
        f"""
#############################
# Starting to listen to host: {host}
# Topic: {topic} | ignoring: {ignore_topics}
#############################
"""
    )
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        pass

    print(
        f"""

#############################
# Finished listening to host: {host}
# Topic: {topic} | ignoring: {ignore_topics}
#############################
"""
    )

    if summary:
        _print_summary()


def run() -> None:
    parser = ArgumentParser(
        description="Tool to listen to the sand MQTT communication. It will "
        "try to decode or depickle anything it recognizes and is therefore a "
        "little bit more adapted to SAND compared to just generic listening to "
        "MQTT."
    )

    parser.add_argument(
        "--host",
        metavar="HOST",
        type=str,
        help="Host to connect to",
        default="127.0.0.1",
    )
    parser.add_argument(
        "--topic",
        type=str,
        default="#",
        help="Subscribe to a specific topic",
    )
    parser.add_argument(
        "--ignore-topics",
        type=str,
        nargs="*",
        default=[
            "MQTTLogger/#",
            "SensorFusion/all/data/collision_map",
            "LidarPacketEnricher/all/data/pointcloud2d",
        ],
        help="Ignore specific topics",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset all topics before starting listening",
    )
    parser.add_argument(
        "--reset-only",
        action="store_true",
        help="Reset all topics and quit",
    )
    parser.add_argument(
        "--logger",
        action="store_true",
        help="Subscribe on logging topics",
    )
    parser.add_argument(
        "--list-all-topics",
        action="store_true",
        help="List all topics at the end",
    )
    parser.add_argument(
        "--time",
        metavar="SECONDS",
        default=-1,
        type=int,
        help="Kill listener after SECONDS, useful for topic-lists, suppresses all other output",
    )
    args = parser.parse_args()

    if args.reset or args.reset_only:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)-7.7s: [%(name)-15.15s][%(threadName)-15.15s] %(message)s",
            handlers=[logging.StreamHandler(stream=sys.stdout)],
        )

        # pylint: disable=import-outside-toplevel
        from sand.mqtt import reset_broker

        reset_broker(args.host)

        if args.reset_only:
            print("Done with resetting")
            sys.exit(0)

    _listen(
        args.host,
        args.topic if not args.logger else "log/#",
        args.ignore_topics,
        args.logger,
        args.time,
        args.list_all_topics,
    )
