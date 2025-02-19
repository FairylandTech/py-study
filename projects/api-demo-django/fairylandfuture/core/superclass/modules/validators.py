# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-13 20:40:53 UTC+08:00
"""
from typing import Any, Callable, Optional, Union, Sequence, Type

from fairylandfuture.exceptions.generic import ValidationError


class Validator:

    def __init__(self, required: bool, typedef: Union[Type, Sequence[Type]], validator_factory: Optional[Callable[[Any], bool]] = None):
        self.__required = required
        self.__typedef = typedef
        self.__validator_factory = validator_factory

    @property
    def required(self):
        return self.__required

    @property
    def typedef(self):
        return self.__typedef

    @property
    def validator_factory(self):
        return self.__validator_factory

    def validate(self, value: Any) -> Any:
        if self.required and value is None:
            raise ValidationError("Required parameter is missing.")

        if value is not None and not isinstance(value, self.typedef):
            raise ValidationError(f"Parameter type error. Expected type: {self.typedef}")

        if self.validator_factory is not None and not self.validator_factory(value):
            raise ValidationError("Parameter validation failed.")

        return value
