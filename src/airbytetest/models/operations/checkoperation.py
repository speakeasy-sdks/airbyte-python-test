"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import checkoperationread as shared_checkoperationread
from ..shared import invalidinputexceptioninfo as shared_invalidinputexceptioninfo
from typing import Optional


@dataclasses.dataclass
class CheckOperationResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    check_operation_read: Optional[shared_checkoperationread.CheckOperationRead] = dataclasses.field(default=None)
    r"""Successful operation"""
    invalid_input_exception_info: Optional[shared_invalidinputexceptioninfo.InvalidInputExceptionInfo] = dataclasses.field(default=None)
    r"""Input failed validation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    