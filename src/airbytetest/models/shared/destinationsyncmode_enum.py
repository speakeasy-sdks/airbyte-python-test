"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class DestinationSyncModeEnum(str, Enum):
    APPEND = 'append'
    OVERWRITE = 'overwrite'
    APPEND_DEDUP = 'append_dedup'
