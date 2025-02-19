from django.db import models

# Create your models here.
from typing import Dict

from fairylandfuture.structures.builder.db import StructureMySQLExecute
from utils.db import dbtools


class UserInfoModel(object):

    def __init__(self, _id=None):
        self.id = _id

    def query(self, page: int, size: int, params: Dict[str, ...]):
        sql = "select id, name, account, department, created_at, updated_at, existed from example_user_info_1"
        limit_sql = f" limit %(size)s, %(page)s"

        if params:
            where_sql = " and ".join((f"{key} = %({key})s" for key, value in params.items()))
        else:
            where_sql = ""

        if where_sql:
            sql += f"where {where_sql}"
        if limit_sql:
            sql += limit_sql

        sql_params = {"page": page, "size": (page - 1) * size, **params}

        print(sql)
        print(sql_params)
        result = dbtools.select(StructureMySQLExecute(sql, sql_params))

        return result
