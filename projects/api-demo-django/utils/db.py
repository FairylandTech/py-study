# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-18 21:13:45 UTC+08:00
"""

from fairylandfuture.modules.db.mysql import MySQLConnector, MySQLOperator

connector = MySQLConnector(
    host="employ.fairies.ltd",
    port=51004,
    user="root",
    password="7JquBHx3Vm5MrKh7",
    database="py_study"
)

dbtools = MySQLOperator(connector)
