# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-26 23:16:19 UTC+08:00
"""

import functools
from typing import Union, Dict, Tuple, Any, Sequence

import pymysql
from dbutils.pooled_db import PooledDB
from pymysql.connections import Connection
from pymysql.cursors import DictCursor

from fairylandfuture.abstract.modules.db import AbstractMySQLOperator
from fairylandfuture.exceptions.db import SQLSyntaxException
from fairylandfuture.exceptions.messages.db import SQLSyntaxExceptMessage
from fairylandfuture.structures.builder.db import StructureMySQLExecute


class CustomMySQLConnection(Connection):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__exist = True

    def close(self):
        super().close()
        self.__exist = False

    @property
    def exist(self):
        return self.__exist


class CustomMySQLCursor(DictCursor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__exist = True

    def close(self):
        super().close()
        self.__exist = False

    @property
    def exist(self):
        return self.__exist


class MySQLConnector:
    """
    This class is used to connect to MySQL database and execute SQL statements.

    It is a subclass of AbstractMySQLConnector and implements the methods of AbstractMySQLOperator.

    :param host: The host name of the MySQL server.
    :type host: str
    :param port: The port number of the MySQL server.
    :type port: int
    :param user: The user name used to connect to the MySQL server.
    :type user: str
    :param password: The password used to connect to the MySQL server.
    :type password: str
    :param database: The name of the database to connect to.
    :type database: str
    :param charset: The character set used to connect to the MySQL server.
    :type charset: str, optional

    Usage:
        >>> from fairylandfuture.modules.databases.mysql import MySQLConnector
        >>> connector = MySQLConnector(host="localhost", port=3306, user="root", password="password", database="test")
        >>> connector.cursor.execute("SELECT * FROM users")
        >>> result = connector.cursor.fetchall()
        >>> print(result)
        [{'id': 1, 'name': 'John', 'age': 25}, {'id': 2, 'name': 'Mary', 'age': 30}]
        >>> connector.close()
    """

    def __init__(self, host: str, port: int, user: str, password: str, database: str, charset: str = "utf8mb4"):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__charset = charset
        self.connection: CustomMySQLConnection = self.__connect()
        self.cursor: CustomMySQLCursor = self.connection.cursor()

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port

    @property
    def user(self) -> str:
        return self.__user

    @property
    def database(self) -> str:
        return self.__database

    @property
    def charset(self) -> str:
        return self.__charset

    def __connect(self) -> CustomMySQLConnection:
        """
        This method is used to connect to the MySQL server.

        :return: Connection object.
        :rtype: CustomMySQLConnection
        """
        connection = CustomMySQLConnection(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database,
            charset=self.__charset,
            cursorclass=CustomMySQLCursor,
        )

        return connection

    def reconnect(self) -> None:
        """
        This method is used to reconnect to the MySQL server.

        :return: ...
        :rtype: ...
        """
        if not self.connection.exist:
            self.connection: CustomMySQLConnection = self.__connect()
            self.cursor: CustomMySQLCursor = self.connection.cursor()
        if not self.cursor.exist and self.connection.exist:
            self.cursor: CustomMySQLCursor = self.connection.cursor()

    @staticmethod
    def reload(func):
        """
        This method is used to reload the connection and cursor object if they are closed.

        :param func: Decorated function.
        :type func: MethodType
        :return: ...
        :rtype: ...
        """

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            self.reconnect()
            return func(self, *args, **kwargs)

        return wrapper

    def close(self) -> None:
        """
        This method is used to close the connection and cursor object.

        :return: ...
        :rtype: ...
        """
        if self.cursor.exist:
            self.cursor.close()
        if self.connection.exist:
            self.connection.close()

    def __del__(self):
        self.close()


class MySQLOperator(AbstractMySQLOperator):
    """
    This class is used to execute SQL statements for MySQL database.
    It is a subclass of AbstractMySQLOperator and implements the methods of AbstractMySQLOperator.

    :param connector: The MySQLConnector object.
    :type connector: MySQLConnector

    Usage:
        >>> from fairylandfuture.modules.databases.mysql import MySQLConnector, MySQLOperator
        >>> connector = MySQLConnector(host="localhost", port=3306, user="root", password="password", database="test")
        >>> operation = MySQLOperator(connector)
        >>> operation.execute("SELECT * FROM users")
        [{'id': 1, 'name': 'John', 'age': 25}, {'id': 2, 'name': 'Mary', 'age': 30}]
    """

    def __init__(self, connector: MySQLConnector):
        if not isinstance(connector, MySQLConnector) or isinstance(connector, type):
            raise TypeError("The connector must be an instance or subclass instance of MySQLConnector.")

        self.connector = connector

    def execute(self, struct: StructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        """
        This method is used to execute a SQL statement.

        :param struct: StructureMySQLExecute object.
        :type struct: StructureMySQLExecute
        :return: Query result or execution result.
        :rtype: bool | tuple
        """
        try:
            self.connector.reconnect()
            self.connector.cursor.execute(struct.query, struct.args)
            result = self.connector.cursor.fetchall()
            self.connector.connection.commit()
            self.connector.close()

            return result if result else True
        except Exception as err:
            self.connector.connection.rollback()
            self.connector.close()
            raise err

    def executemany(self, struct: StructureMySQLExecute, /) -> bool:
        """
        This method is used to execute multiple SQL statements.

        :param struct: StructureMySQLExecute object.
        :type struct: StructureMySQLExecute
        :return: Execution result.
        :rtype: bool
        """
        try:
            self.connector.reconnect()
            self.connector.cursor.executemany(struct.query, struct.args)
            self.connector.connection.commit()
            self.connector.close()
            return True
        except Exception as err:
            self.connector.connection.rollback()
            self.connector.close()
            raise err

    def multiexecute(self, structs: Sequence[StructureMySQLExecute], /) -> bool:
        """
        This method is used to execute multiple SQL statements.

        :param structs: StructureMySQLExecute object sequence.
        :type structs: Sequence
        :return: Execution result.
        :rtype: bool
        """
        try:
            self.connector.reconnect()
            for struct in structs:
                if struct.query.lower().startswith("select"):
                    raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_NOT_SELECT)

                self.connector.cursor.execute(struct.query, struct.args)
            self.connector.connection.commit()
            self.connector.close()
            return True
        except Exception as err:
            self.connector.connection.rollback()
            self.connector.close()
            raise err

    def select(self, struct: StructureMySQLExecute, /) -> Tuple[Dict[str, Any], ...]:
        """
        This method is used to execute a select statement.

        :param struct: Query structure.
        :type struct: StructureMySQLExecute
        :return: Query result
        :rtype: tuple
        """
        if not struct.query.lower().startswith("select"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_SELECT)

        try:
            return self.execute(struct)
        except Exception as err:
            raise err


class MySQLSQLSimpleConnectionPool:

    def __init__(self, host: str, port: int, user: str, password: str, database: str, charset: str = None, /):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__charset = charset if charset else "utf8mb4"

        self.__pool = PooledDB(
            creator=pymysql,
            maxconnections=50,
            mincached=3,
            maxcached=5,
            maxshared=5,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database,
            charset=self.__charset,
            cursorclass=CustomMySQLCursor,
        )

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
        return "".join(["*" for _ in range(len(self.__password))])

    @property
    def database(self):
        return self.__database

    @property
    def charset(self):
        return self.__charset

    def __open(self) -> Tuple[Connection, CustomMySQLCursor]:
        connection: Connection = self.__pool.connection()
        cursor: CustomMySQLCursor = connection.cursor(CustomMySQLCursor)
        return connection, cursor

    def __close(self, conn: Connection, cur: CustomMySQLCursor) -> None:
        cur.close()
        conn.close()

    def execute(self, struct: StructureMySQLExecute) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        connection, cursor = self.__open()
        try:
            cursor.execute(struct.query, struct.args)
            data = cursor.fetchall()
            connection.commit()
            self.__close(connection, cursor)

            return tuple(data) if data else True
        except Exception as err:
            connection.rollback()
            self.__close(connection, cursor)
            raise err

    def executemany(self, struct: StructureMySQLExecute) -> bool:
        connection, cursor = self.__open()
        try:
            cursor.executemany(struct.query, struct.args)
            connection.commit()
            self.__close(connection, cursor)

            return True
        except Exception as err:
            connection.rollback()
            self.__close(connection, cursor)
            raise err

    def multiexecute(self, structs: Sequence[StructureMySQLExecute]) -> bool:
        connection, cursor = self.__open()
        try:
            for struct in structs:
                if sql.query.lower().startswith("select"):
                    raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_NOT_SELECT)
                cursor.execute(struct.query, struct.args)
            connection.commit()
            self.__close(connection, cursor)

            return True
        except Exception as err:
            connection.rollback()
            self.__close(connection, cursor)
            raise err
