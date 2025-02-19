from django.contrib.admin.templatetags.admin_list import results
from django.db import models

# Create your models here.
from tools.dbtools.sql_execute import SqlTools

db = SqlTools()

class UserInfoModel():

    def __init__(self,fields=None,):
        if fields is None:
            self.fields = (
                'name','account','department',
                      'status','create_at','update_at'
            )

    def search(self,name,account,page,size,field=None):
        if field is None:
            self.fields = ','.join(self.fields)
            table = 'user_info'
        if not page:
            page = 1
        if not size:
            size = 10
        sql = 'select {field} from {table}'.format(field=self.fields,table=table)

        if name and account:
            sql = sql + ' where name={name} and account={account}'.format(name=name,account=account)
        if name:
            sql = sql + ' where name={name}'.format(name=name)
        if account:
            sql = sql + ' where account={account}'.format(account=account)

        limit = 'order by id desc limit {page},{size}'.format(page=page,size=(page-1)*size)
        sql = sql + limit

        try:
            results = db.query(sql)
            return results
        except Exception as e:
            print('sql执行错误(UserInfoModel.search is None)：'+str(e))
            return  None

        def add(self):
            pass