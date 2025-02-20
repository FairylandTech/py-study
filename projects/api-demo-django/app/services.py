# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-19 21:51:21 UTC+08:00
"""

from typing import Dict

from app.models import UserInfoModel

from utils.structutes.user import UserinfoStruct
from utils.journal import journal


class UserInfoService(object):
    __model = UserInfoModel()

    @classmethod
    def query(cls, params: Dict[str, ...]):
        journal.info(f"用户服务::查询::{cls.__name__}")
        page, size = params.pop("page"), params.pop("size")
        user_info = cls.__model.query(page, size, params)

        journal.info(f"用户服务::查询::构建响应体")
        data = [
            UserinfoStruct(
                row.get("id"),
                row.get("name"),
                row.get("account"),
                row.get("department"),
                row.get("existed"),
                row.get("created_at"),
                row.get("updated_at"),
            ).to_dict()
            for row in user_info
        ]

        return data
