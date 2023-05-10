"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import workspaceread as shared_workspaceread
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkspaceReadList:
    r"""Successful operation"""
    
    workspaces: list[shared_workspaceread.WorkspaceRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaces') }})
    