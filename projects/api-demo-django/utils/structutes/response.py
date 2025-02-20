# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-20 20:54:18 UTC+08:00
"""
from dataclasses import dataclass, field, asdict
from typing import MutableSequence, Sequence, MutableMapping, Mapping, Union, Self, Any, Dict

from fairylandfuture.const.response.code import RESPONSE_CODE_MAP


@dataclass
class StructureResponse:
    code: int = field(default=None)
    message: str = field(default=None)
    data: Union[MutableSequence, Sequence, MutableMapping, Mapping] = field(default=None)

    def __post_init__(self):
        if self.code and not self.message:
            self.message = RESPONSE_CODE_MAP.get(self.code, "Internal Server Error")

    @property
    def asdict(self: Self) -> Dict[str, Any]:
        return asdict(self)
