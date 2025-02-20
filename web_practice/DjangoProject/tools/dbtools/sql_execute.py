import pymysql
from pymysql.connections import Connection
from pymysql.cursors import DictCursor

class MysqlConnection(Connection):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__exit = True

    def close(self):
        super().close()
        self.__exit = False

    @property
    def exit(self):
        return self.__exit

class MysqlCursor(DictCursor):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__exit = True

    def close(self):
        super().close()
        self.__exit = False

    @property
    def exit(self):
        return self.__exit








class SqlTools:

    def __init__(self):
        self.__host = 'localhost'
        self.__port = '3306'
        self.__user = 'root'
        self.__password = '15802995747.m.'
        self.__db_name  = 'user_info'
        self.__charset = 'utf8'

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def db_name(self):
        return self.__db_name

    @property
    def charset(self):
        return self.__charset

    def get_conn(self):
        self.db = MysqlConnection(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            db=self.__db_name,
            charset=self.__charset
            
        )
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def execute(self,sql):
        count = 0
        try:
            self.get_conn()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.cursor.close()
        except Exception as e:
            print('操作失败'+str(e))
            self.db.rollback()
        return count

    def execute_many(self,sql,data):
        pass

    def query(self,sql):
        res = None
        try:
            self.get_conn
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print('查询失败' + str(e))
        return res

    def query_many(self,sql):
        res = None
        try:
            self.get_conn
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print('查询失败' + str(e))
        return res