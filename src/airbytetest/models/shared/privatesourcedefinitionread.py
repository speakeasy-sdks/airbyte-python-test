"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sourcedefinitionread as shared_sourcedefinitionread
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PrivateSourceDefinitionRead:
    r"""Successful operation"""
    
    granted: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('granted') }})
    source_definition: shared_sourcedefinitionread.SourceDefinitionRead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinition') }})
    