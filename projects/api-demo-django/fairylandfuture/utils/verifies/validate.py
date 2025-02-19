# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-10 18:56:45 UTC+08:00
"""

from typing import Dict, Tuple, Type, Union

from fairylandfuture.exceptions.generic import ParamsInvalidException, ParamsTypeException


class ParamTypeValidatorUtils:
    """
    Argument type validators.

    :param expected_types: A dictionary of expected types for each parameter.
    :type expected_types: dict[str, type]

    Usage::

        validator = ParamTypeValidator({
            "param1": int,
            "param2": str,
            "param3": bool
        })

        params = {
            "param1": 123,
            "param2": "abc",
            "param3": True,
            "param4": "def"
        }

        if validator.validate(params):
            # do something
        else:
            # handle errors
    """

    def __init__(self, expected_types: Dict[str, Union[Type, Tuple[Type, ...]]]):
        self.expected_types = expected_types

    def validate(self, params: Dict[str, object]):
        for param_name, param_value in params.items():
            if param_name not in self.expected_types:
                raise ParamsInvalidException(f"Parameter '{param_name}' is not defined in the expected types.")

            expected_type = self.expected_types[param_name]
            if not isinstance(param_value, expected_type):
                err_msg = f"The type of parameter '{param_name}' is '{type(param_value)}', which does not match the expected type '{expected_type}'."
                raise ParamsTypeException(err_msg)

        return True
