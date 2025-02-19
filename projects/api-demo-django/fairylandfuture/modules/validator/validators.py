# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-24 14:41:30 UTC+08:00
"""

from typing import Any, Dict

from fairylandfuture.core.superclass.modules.validators import Validator


class RequestParamsValidator:
    def __init__(self, schema: Dict[str, Validator]):
        self.schema = schema

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {key: validator.validate(data.get(key)) for key, validator in self.schema.items()}
