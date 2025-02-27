
# print('{name}今年{age}岁'.format(name='wo',age=18))
# print(repr('{name}今年{age}岁'.format(name='wo',age=18)))
# name = 'wo'
# age = 18
# print('%s今年%s岁'%(name,age))
#
# parms = {"name":'wo',"age":age}
# where_sql = ' and '.join(f'{key}s = %({key})s' for key in parms)
# print(where_sql)


# from tools.dbtools.sql_execute import SqlTools
# db = SqlTools()
# # base_sql = 'select id,name,account,department,status,create_at,update_at from user_info'
# # results = db.query(base_sql)
# # print(results)
#
#
#
# parms = {"name":'阿米娅','account':'amy'}
#
# def query( page: int, size: int, parms):
#     base_sql = 'select id,name,account,department,status,create_at,update_at from user_info'
#     limit_sql = f" limit %(page)s, %(size)s"
#
#     if parms:
#         where_sql = ' and '.join(f'{key}=%({key})s' for key in parms)
#     else:
#         where_sql = ''
#     if where_sql:
#         sql = base_sql + f' where {where_sql}'
#     if limit_sql:
#         sql += limit_sql
#
#     sql_parms = {"page": (page-1)*size, "size": size, **parms}
#     print(sql)
#     print(sql_pa+rms)
#     results = db.query(sql, sql_parms)
#     print(results)
#
# query(1,10,parms)

import datetime
data = [{'id': 1, 'name': '阿米娅', 'account': 'amy', 'department': '战斗部', 'status': 1, 'create_at': datetime.datetime(2025, 2, 20, 21, 17, 55), 'update_at': datetime.datetime(2025, 2, 20, 21, 17, 55)}]

key = dict(data)
print(key)
print(type(data))