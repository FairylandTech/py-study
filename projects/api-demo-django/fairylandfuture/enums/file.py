# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 00:57:31 UTC+08:00
"""

from fairylandfuture.core.superclass.enums.enumerate import BaseEnum


class FileModeEnum(BaseEnum):
    """
    file mode enum.
    """

    r = "r"
    rb = "rb"
    r_plus = "r+"
    rb_plus = "rb+"

    w = "w"
    wb = "wb"
    w_plus = "w+"
    wb_plus = "wb+"

    a = "a"
    ab = "ab"
    a_plus = "a+"
    ab_plus = "ab+"

    default = r
