# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 00:56:07 UTC+08:00
"""

from fairylandfuture.core.superclass.enums.enumerate import BaseEnum


class EncodingEnum(BaseEnum):
    """
    Encoding enum.
    """

    utf8 = "UTF-8"
    gbk = "GBK"
    gb2312 = "GB2312"
    gb18030 = "GB18030"

    default = utf8
