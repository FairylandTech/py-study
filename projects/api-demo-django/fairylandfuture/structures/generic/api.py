# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-14 17:02:11 UTC+08:00
"""

from dataclasses import dataclass, field
from typing import MutableSequence, Sequence, MutableMapping, Mapping, Union

from fairylandfuture.core.superclass.structures import BaseStructure
from fairylandfuture.const.response.code import RESPONSE_CODE_MAP


@dataclass(frozen=True)
class StructureResponse(BaseStructure):
    code: int = field(default=None)
    message: str = field(default=None)
    data: Union[MutableSequence, Sequence, MutableMapping, Mapping] = field(default=None)

    def __post_init__(self):
        if self.code and not self.message:
            object.__setattr__(self, "message", RESPONSE_CODE_MAP.get(self.code, "Internal Server Error"))

    def __str__(self):
        return self.string
