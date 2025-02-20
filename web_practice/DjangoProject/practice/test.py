
# print('{name}今年{age}岁'.format(name='wo',age=18))
# print(repr('{name}今年{age}岁'.format(name='wo',age=18)))
# name = 'wo'
# age = 18
# print('%s今年%s岁'%(name,age))
#
# parms = {"name":'wo',"age":age}
# where_sql = ' and '.join(f'{key}s = %({key})s' for key in parms)
# print(where_sql)


# def query(page: int, size: int, parms):
#     base_sql = 'select id,name,account,department,status,created_at,update_at from user_info'
#     limit_sql = f" limit %(size)s, %(page)s"
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
#     sql_parms = {"page": page, "size": size, **parms}
#     print(sql)
#     print(sql_parms)
#
# query(1,10,parms)