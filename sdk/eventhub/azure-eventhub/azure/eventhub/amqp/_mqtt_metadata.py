# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------

from __future__ import annotations
from typing import NamedTuple, Optional, Any, cast, Mapping, Dict, Union, List

from traceback import print_stack
from ._amqp_utils import normalized_data_body, normalized_sequence_body


class MqttMetadata:
    """
    The MQTT Metadata Message
    """

    def __init__(self, value=List[Any]):
        self.topic_name = ""
        self.qos = 0
        self.retain = False
        self.dup = False
        self.content_type = None
        self.message_expiry_interval_sec = None
        self.user_properties = []
        self.correlation_data = None
        self.response_topic = None
        self.payload_format_indicator = 0

        if len(value) > 0:
            self.topic_name = value.pop(0)
        if len(value) > 0:
            qos = value.pop(0)
        if len(value) > 0:
            retain = value.pop(0)
        if len(value) > 0:
            dup = value.pop(0)
        if len(value) > 0:
            content_type = value.pop(0)
        if len(value) > 0:
            message_expiry_interval_sec = value.pop(0)
        if len(value) > 0:
            for prop in value.pop(0):
                self.user_properties.append(MqttUserProperty(prop.value))
        if len(value) > 0:
            correlation_data = value.pop(0)
        if len(value) > 0:
            response_topic = value.pop(0)
        if len(value) > 0:
            payload_format_indicator = value.pop(0)

    def __repr__(self) -> str:
        return "MqttMetadata(topic_name={}, qos={}, retain={}, dup={}, content_type={}, message_expiry_interval_sec={}, user_properties={}, correlation_data={}, response_topic={}, payload_format_indicator={})".format(
            self.topic_name,
            self.qos,
            self.retain,
            self.dup,
            self.content_type,
            self.message_expiry_interval_sec,
            self.user_properties,
            self.correlation_data,
            self.response_topic,
            self.payload_format_indicator)


class MqttUserProperty:

    def __init__(self, value=List[Any]):
        self.name = value[0]
        self.value = value[1]

    def __repr__(self) -> str:
        return "MqttUserProperty(name={}, value={})".format(self.name, self.value)
