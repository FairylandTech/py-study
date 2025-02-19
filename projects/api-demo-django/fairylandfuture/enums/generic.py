# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-24 10:26:13 UTC+08:00
"""

from fairylandfuture.core.superclass.enums.enumerate import BaseEnum


class ComparisonOperatorEnum(BaseEnum):
    EQUAL = "="
    NOT_EQUAL = "!="
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN = "<"
    LESS_THAN_OR_EQUAL = "<="

    IN = "in"
    NOT_IN = "not in"
    LIKE = "like"
    ILIKE = "ilike"
    NOT_LIKE = "not like"
    IS_NULL = "is null"
    IS_NOT_NULL = "is not null"
