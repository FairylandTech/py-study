# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-27 00:07:43 UTC+08:00
"""

from dataclasses import dataclass, field
from typing import Optional, Union, Sequence, MutableSequence, Mapping, MutableMapping

from fairylandfuture.core.superclass.structures.structure import BaseStructure


@dataclass(frozen=True)
class StructureMySQLExecute(BaseStructure):
    query: str
    args: Optional[Union[Sequence, MutableSequence, Mapping, MutableMapping]] = field(default=None)


@dataclass(frozen=True)
class StructurePostgreSQLExecute(BaseStructure):
    query: str
    vars: Optional[Union[Sequence, MutableSequence, Mapping, MutableMapping]] = field(default=None)
