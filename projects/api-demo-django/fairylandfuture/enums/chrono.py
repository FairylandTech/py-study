# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 00:55:09 UTC+08:00
"""

from fairylandfuture.core.superclass.enums.enumerate import BaseEnum


class DateTimeEnum(BaseEnum):
    """
    Date time enum.
    """

    date = "%Y-%m-%d"
    time = "%H:%M:%S"
    datetime = "%Y-%m-%d %H:%M:%S"

    date_cn = "%Y年%m月%d日"
    time_cn = "%H时%M分%S秒"
    datetime_cn = "%Y年%m月%d日 %H时%M分%S秒"

    default = datetime
    default_cn = datetime_cn


class TimeZoneEnum(BaseEnum):
    """
    Time zone enum.
    """

    shanghai = "Asia/Shanghai"
    beijing = "Asia/Shanghai"
    singapore = "Asia/Singapore"