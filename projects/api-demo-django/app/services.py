# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-19 21:51:21 UTC+08:00
"""

from datetime import datetime
from typing import Dict

from fairylandfuture.enums.chrono import DateTimeEnum

from app.models import UserInfoModel


class UserInfoService(object):
    __model = UserInfoModel()

    @classmethod
    def query(cls, params: Dict[str, ...]):
        page, size = params.pop("page"), params.pop("size")
        print(params)
        user_info = cls.__model.query(page, size, params)
        print(user_info)

        data = []
        if len(user_info) != 1:
            for row in user_info:
                for _id, name, account, dep, cat, uat, existed in row:
                    # cat: datetime
                    # uat: datetime
                    data.append(
                        {
                            "id": _id,
                            "name": name,
                            "account": account,
                            "department": dep,
                            "existed": bool(existed),
                            # "created_at": cat.strftime(DateTimeEnum.datetime.value),
                            "created_at": cat,
                            # "updated_at": uat.strftime(DateTimeEnum.datetime.value),
                            "updated_at": uat,
                        }
                    )
        else:
            ((row),) = user_info
            data = [
                {
                    "id": row.get("id"),
                    "name": row.get("name"),
                    "account": row.get("account"),
                    "department": row.get("department"),
                    "existed": bool(row.get("existed")),
                    "created_at": row.get("created_at").strftime(DateTimeEnum.datetime.value),
                    "updated_at": row.get("updated_at").strftime(DateTimeEnum.datetime.value),
                }
            ]

        return data
