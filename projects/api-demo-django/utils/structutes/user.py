# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-20 20:16:46 UTC+08:00
"""
from typing import Dict, Sequence

from datetime import datetime
from dataclasses import dataclass
from fairylandfuture.core.superclass.structures.structure import BaseStructure
from fairylandfuture.enums.chrono import DateTimeEnum


@dataclass(frozen=True)
class UserinfoStruct(BaseStructure):
    # id: str
    name: str
    account: str
    department: str
    existed: int
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        object.__setattr__(self, "existed", bool(self.existed))
        object.__setattr__(self, "created_at", self.created_at.strftime(DateTimeEnum.datetime.value))
        object.__setattr__(self, "updated_at", self.updated_at.strftime(DateTimeEnum.datetime.value))
