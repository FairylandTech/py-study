from django.db import models

# Create your models here.
from typing import Dict

from fairylandfuture.structures.builder.db import StructureMySQLExecute
from utils.db import dbtools
from utils.journal import journal


class UserInfoModel(object):

    def __init__(self, _id=None):
        self.id = _id

    def query(self, page: int, size: int, params: Dict[str, ...]):
        journal.info(f"用户模型::查询::{self.__class__.__name__}")
        sql = "select id, name, account, department, created_at, updated_at, existed from example_user_info_1"
        limit_sql = f" limit %(page)s, %(size)s"

        if params:
            where_sql = " and ".join((f"{key} = %({key})s" for key, value in params.items()))
        else:
            where_sql = ""

        if where_sql:
            sql += f" where {where_sql}"
        if limit_sql:
            sql += limit_sql

        sql = sql if sql.endswith(";") else f"{sql};"

        sql_params = {"page": (page - 1) * size, "size": size, **params}

        journal.debug(f"用户模型::查询::SQL:{sql}")
        journal.debug(f"用户模型::查询::SQL Params:{sql_params}")
        result = dbtools.select(StructureMySQLExecute(sql, sql_params))

        return result if result and result is not True else tuple()
