"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import streamtransform as shared_streamtransform
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CatalogDiff:
    r"""Describes the difference between two Airbyte catalogs."""
    
    transforms: list[shared_streamtransform.StreamTransform] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transforms') }})
    r"""list of stream transformations. order does not matter."""
    