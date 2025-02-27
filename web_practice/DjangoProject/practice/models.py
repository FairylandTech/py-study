from typing import Dict
from datetime import datetime
from django.contrib.admin.templatetags.admin_list import results
from django.db import models

# Create your models here.
from tools.dbtools.sql_execute import SqlTools

db = SqlTools()

# class UserInfoModel():
#
#     def __init__(self,fields=None,):
#         if fields is None:
#             self.fields = (
#                 'name','account','department',
#                       'status','create_at','update_at'
#             )
#
#     def search(self,name,account,page,size,field=None):
#         if field is None:
#             self.fields = ','.join(self.fields)
#             table = 'user_info'
#         if not page:
#             page = 1
#         if not size:
#             size = 10
#         sql = 'select {field} from {table}'.format(field=self.fields,table=table)
#
#         if name and account:
#             sql = sql + ' where name={name} and account={account}'.format(name=name,account=account)
#         if name:
#             sql = sql + ' where name={name}'.format(name=name)
#         if account:
#             sql = sql + ' where account={account}'.format(account=account)
#
#         limit = 'order by id desc limit {page},{size}'.format(page=page,size=(page-1)*size)
#         sql = sql + limit
#
#         try:
#             results = db.query(sql)
#             return results
#         except Exception as e:
#             print('sql执行错误(UserInfoModel.search is None)：'+str(e))
#             return  None
#
#         def add(self):
#             pass









class UserInfoModelSimple():

    def __init__(self,_id=None):
        self.id = _id

    def query(self,page:int,size:int,parms:Dict[str,...]):
        base_sql = 'select id,name,account,department,status,create_at,update_at from user_info'
        limit_sql = f" limit %(page)s, %(size)s"

        if parms:
            where_sql = ' and '.join(f'{key}=%({key})s' for key in parms)
        else:
            where_sql = ''
        if where_sql:
            sql =base_sql + f' where {where_sql}'
        if limit_sql:
            sql += limit_sql

        sql_parms = {"page":(page-1)*size,"size":size,**parms}
        print(sql)
        print(sql_parms)
        results = db.query(sql,sql_parms)

        print(results)
        return results


    def update(self,parms):
        if 'update_at' not in parms.keys():
            parms['update_at'] = datetime.now()

        sql = 'updata user_info set name = %({name})s,account=%(account)s,status=%(staus)s,update_at=%(update_at)s where id=%(id)s'
        results = db.execute(sql,parms)
        return results