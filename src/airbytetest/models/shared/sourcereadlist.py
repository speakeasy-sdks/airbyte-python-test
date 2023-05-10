"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sourceread as shared_sourceread
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceReadList:
    r"""Successful operation"""
    
    sources: list[shared_sourceread.SourceRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sources') }})
    