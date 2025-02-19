# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-10 10:46:52 UTC+08:00
"""
import abc
from enum import Enum
from typing import Any, List, Tuple, TypeVar, Union, Optional, Sequence, Type

_TypeBaseEnum = TypeVar("_TypeBaseEnum", bound="BaseEnum")


class BaseEnum(Enum):
    """
    Enum Base Class.
    """

    @classmethod
    def get(cls: Type[_TypeBaseEnum], value: str) -> Any:
        """
        Get the Enum value by member.

        :param value: Attribute action
        :type value: str
        :return: Attribute value
        :rtype: ...
        """
        if not isinstance(value, str):
            raise TypeError("The value must be a string.")

        value_object: _TypeBaseEnum = getattr(cls, value)

        return value_object.value

    @classmethod
    def members(cls: Type[_TypeBaseEnum], exclude_enums: Optional[Sequence[str]] = None, only_value: bool = False) -> Union[Tuple[_TypeBaseEnum, ...], Tuple[Any, ...]]:
        """
        Returns a tuple with all members of the Enum.

        :param exclude_enums: List of members to exclude from the result.
        :type exclude_enums: list or tuple or set
        :param only_value: If True, returns only the values of the members.
        :type only_value: bool
        :return: Tuple with all members of the Enum.
        :rtype: tuple
        """
        if exclude_enums and not isinstance(exclude_enums, (list, tuple, set)):
            raise TypeError("The exclude_enums must be a list, tuple or set.")

        member_list: List[_TypeBaseEnum] = list(cls)

        if exclude_enums:
            member_list: List[_TypeBaseEnum] = [member for member in member_list if member not in exclude_enums]

        if only_value:
            return tuple(member.value for member in member_list)
        else:
            return tuple(member_list)

    @classmethod
    def names(cls: Type[_TypeBaseEnum]) -> Tuple[str, ...]:
        """
        Returns a tuple with the names of all members of the Enum.
        :return: Tuple with the names of all members of the Enum.
        :rtype: tuple
        """
        return tuple(cls._member_names_)

    @classmethod
    def values(cls: Type[_TypeBaseEnum], exclude_enums: Optional[Sequence] = None) -> Tuple[Any, ...]:
        """
        Returns a tuple with the values of all members of the Enum.

        :param exclude_enums: List of members to exclude from the result.
        :type exclude_enums: Iterable
        :return: Tuple with the values of all members of the Enum.
        :rtype: tuple
        """
        return cls.members(exclude_enums, True)
