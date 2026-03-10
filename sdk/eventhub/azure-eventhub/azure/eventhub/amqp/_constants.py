# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
from enum import Enum
from azure.core import CaseInsensitiveEnumMeta

from ._mqtt_metadata import MqttMetadata, MqttUserProperty


PUBLISH_METADATA_DESCRIPTOR = 311 << 32 | 2003
USER_PROPERTY_METADATA_DESCRIPTOR = 311 << 32 | 2004;

COMPOSITES = {
    PUBLISH_METADATA_DESCRIPTOR: MqttMetadata,
    USER_PROPERTY_METADATA_DESCRIPTOR: MqttUserProperty,
}


class AmqpMessageBodyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    DATA = "data"
    SEQUENCE = "sequence"
    VALUE = "value"
