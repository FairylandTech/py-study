# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-24 17:30:13 UTC+08:00
"""


class SQLSyntaxExceptMessage:
    SQL_SYNTAX_ERROR = "SQL syntax error."

    SQL_MUST_SELECT = "SQL syntax error. The query must be a select statement."
    SQL_MUST_NOT_SELECT = "SQL syntax error. The query must not be a select statement."
    SQL_MUST_INSERT = "SQL syntax error. The query must be an insert statement."
    SQL_MUST_NOT_INSERT = "SQL syntax error. The query must not be an insert statement."
    SQL_MUST_UPDATE = "SQL syntax error. The query must be an update statement."
    SQL_MUST_NOT_UPDATE = "SQL syntax error. The query must not be an update statement."
    SQL_MUST_DELETE = "SQL syntax error. The query must be a delete statement."
    SQL_MUST_NOT_DELETE = "SQL syntax error. The query must not be a delete statement."
