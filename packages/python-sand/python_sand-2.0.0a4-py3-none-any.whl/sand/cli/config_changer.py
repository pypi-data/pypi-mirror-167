from __future__ import annotations

import pickle
import readline
from argparse import ArgumentParser
from ast import literal_eval
from operator import itemgetter
from typing import Any

from paho.mqtt.client import Client, MQTTMessage, MQTTv5
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties

from sand.datatypes import Topic
from sand.interfaces.communication import get_client_with_reconnect
from sand.interfaces.config import ConfigurationManager

_SETTINGS: dict[Topic, Any] = {}


def _on_message(_: Client, __: None, msg: MQTTMessage) -> None:
    try:
        value = pickle.loads(msg.payload)
    except pickle.UnpicklingError:
        value = msg.payload

    _SETTINGS[msg.topic] = value


def _change_value(client: Client, topic: Topic, new_value: Any) -> None:
    publish_properties = Properties(PacketTypes.PUBLISH)
    # to make sure we can pickle everything and make it easier here, performance here is irrelevant
    publish_properties.UserProperty = ("datatype", "pickle")

    client.publish(
        topic,
        pickle.dumps(new_value),
        retain=True,
        qos=2,
        properties=publish_properties,
    )


def _help_change_menu() -> None:
    print(
        """
Usage:
    h, help     print this help
    q, Q        go back to main prompt
    history     your history is pre-filled with every possible value
    """
    )


def _change_command(client: Client) -> None:
    # you can use your "history" for completion
    for key in sorted(_SETTINGS.keys(), reverse=True):
        readline.add_history(key)

    while True:
        topic_input = input("Key you want to change: ").strip()
        readline.set_pre_input_hook(None)

        if topic_input in ("q", "Q"):
            break

        if topic_input in ("h", "help"):
            _help_change_menu()
            continue

        if topic_input not in _SETTINGS:
            print(f"Key: {topic_input} not found, try again")

            def fix_key() -> None:
                readline.insert_text(topic_input)
                readline.redisplay()

            # make things fixable
            readline.set_pre_input_hook(fix_key)
            continue

        # key found in settings
        def prefill_previous_value() -> None:
            readline.insert_text(str(_SETTINGS[topic_input]))
            readline.redisplay()

        readline.set_pre_input_hook(prefill_previous_value)
        new_value_input = input("New value: ")
        readline.set_pre_input_hook(None)

        new_value = (
            new_value_input
            if isinstance(_SETTINGS[topic_input], str)
            else literal_eval(new_value_input)
        )

        _change_value(client, topic_input, new_value)
        break


def _help_main_menu() -> None:
    print(
        """
Usage:
    h, help     show this help message
    q, Q        quit or go a level up
    l, list     list all available keys to change
    c, change   go into the change menu, further information in there also with "h" or "help"
    """
    )


def _command_loop(client: Client) -> None:
    while True:
        user_input = input("prompt: ").strip()

        if user_input in ("q", "Q"):
            break

        if user_input in ("h", "help"):
            _help_main_menu()
        elif user_input in ("list", "l"):
            for key, item in sorted(_SETTINGS.items(), key=itemgetter(0)):
                print(f"{key} : {item}")
        elif user_input in ("change", "c"):
            _change_command(client)


def _start(host: str, topic: Topic) -> None:
    client = get_client_with_reconnect(protocol=MQTTv5)

    client.on_message = _on_message
    client.connect(host)

    client.subscribe(topic)
    client.loop_start()

    _command_loop(client)

    client.loop_stop()
    client.disconnect()


def run() -> None:
    parser = ArgumentParser(
        description="Tool that can change SAND configuration values live via MQTT."
    )

    parser.add_argument(
        "--host",
        metavar="HOST",
        type=str,
        help="Host to connect to",
        default="127.0.0.1",
    )
    parser.add_argument(
        "--configuration-topic",
        metavar="TOPIC",
        type=str,
        default=f"{ConfigurationManager.__name__}/+/data/#",
        help="You can customize what configuration values you can change. This "
        "can be helpful as we have a lot of possible configurations. "
        "Especially with multiple devices those configuration options multiply."
        " This is a paho-mqtt-topic regex.",
    )

    args = parser.parse_args()

    _start(
        args.host,
        args.configuration_topic,
    )
