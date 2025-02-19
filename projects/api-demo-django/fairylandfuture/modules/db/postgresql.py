# coding: UTF-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-05 12:12:07 UTC+08:00
"""

import re
from typing import Optional, Sequence, Tuple, NamedTuple, Union

import psycopg2
from psycopg2 import pool
from psycopg2.extras import NamedTupleCursor

from fairylandfuture.exceptions.db import SQLSyntaxException
from fairylandfuture.exceptions.messages.db import SQLSyntaxExceptMessage
from fairylandfuture.abstract.modules.db import AbstractPostgreSQLOperator
from fairylandfuture.structures.builder.db import StructurePostgreSQLExecute


class CustomPostgreSQLConnection(psycopg2.extensions.connection):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._exist = True

    def close(self):
        super().close()
        self._exist = False

    @property
    def exist(self) -> bool:
        return self._exist


class CustomPostgreSQLCursor(NamedTupleCursor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._exist = True

    def close(self):
        super().close()
        self._exist = False

    @property
    def exist(self) -> bool:
        return self._exist


class PostgreSQLConnector:
    """
    PostgreSQLConnector is a class for connecting to PostgreSQL database.

    :param host: The host of PostgreSQL database.
    :type host: str
    :param port: The port of PostgreSQL database.
    :type port: int
    :param user: The user of PostgreSQL database.
    :type user: str
    :param password: The password of PostgreSQL database.
    :type password: str
    :param database: The name of PostgreSQL database.
    :type database: str
    :param schema: The schema of PostgreSQL database.
    :type schema: str

    Usage::
        >>> from fairylandfuture.modules.databases.postgresql import PostgreSQLConnector
        >>> connector = PostgreSQLConnector(host="localhost", port=5432, user="postgres", password="password", database="test")
        >>> connector.cursor.execute("SELECT * FROM users")
        >>> result = connector.cursor.fetchall()
        >>> print(result)
        >>> connector.close()

    """

    def __init__(self, host: str, port: int, user: str, password: str, database: str, schema: Optional[str] = None):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__schema = schema
        self.__dsn = f"host={self.__host} port={self.__port} user={self.__user} password={self.__password} dbname={self.__database}"

        if self.__schema:
            self.__dsn = " ".join((self.__dsn, f"options='-c search_path={self.__schema}'"))

        self.connection: CustomPostgreSQLConnection = self.__connect()
        self.cursor: CustomPostgreSQLCursor = self.connection.cursor(cursor_factory=CustomPostgreSQLCursor)

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
    def dsn(self) -> str:
        return self.__dsn_mark_password()

    def __dsn_mark_password(self):
        return re.sub(r"(password=)\S+", r"\1******", self.__dsn)

    def __connect(self) -> CustomPostgreSQLConnection:
        connection = psycopg2.connect(dsn=self.__dsn, connection_factory=CustomPostgreSQLConnection, cursor_factory=CustomPostgreSQLCursor)

        return connection

    def reconnect(self) -> None:
        """
        Reconnect to PostgreSQL database.

        :return: ...
        :rtype: ...
        """
        if not self.connection.exist:
            self.connection: CustomPostgreSQLConnection = self.__connect()
            self.cursor: CustomPostgreSQLCursor = self.connection.cursor(cursor_factory=CustomPostgreSQLCursor)
        if not self.cursor.exist and self.connection.exist:
            self.cursor: CustomPostgreSQLCursor = self.connection.cursor(cursor_factory=CustomPostgreSQLCursor)

    def close(self) -> None:
        """
        Close the connection to PostgreSQL database.

        :return: ...
        :rtype: ...
        """
        if self.cursor.exist:
            self.cursor.close()

        if self.connection.exist:
            self.connection.close()

    def __del__(self):
        self.close()


class PostgreSQLOperator(AbstractPostgreSQLOperator):
    """
    PostgreSQLOperator is a class for executing SQL queries on PostgreSQL database.

    :param connector: The PostgreSQLConnector instance.
    :type connector: PostgreSQLConnector

    Usage::
        >>> from fairylandfuture.modules.databases.postgresql import PostgreSQLConnector, PostgreSQLOperator
        >>> from fairylandfuture.structures.builder.expression import StructurePostgreSQLExecute
        >>> connector = PostgreSQLConnector(host="localhost", port=5432, user="postgres", password="password", database="test")
        >>> operation = PostgreSQLOperator(connector)
        >>> data = operation.select(StructurePostgreSQLExecute("SELECT * FROM users"))
        >>> print(data)

    **Notice:**
    The `connector` must be an instance of `PostgreSQLConnector`.
    PostgreSQLOperator is singleton class.

    """

    def __init__(self, connector: PostgreSQLConnector):
        if not isinstance(connector, PostgreSQLConnector) or isinstance(connector, type):
            raise TypeError("The connector must be an instance or subclass instance of PostgreSQLConnector.")

        self.connector = connector

    def execute(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        """
        Execute a SQL query on PostgreSQL database.

        :param struct: PostgreSQL execute structure.
        :type struct: StructurePostgreSQLExecute
        :return: PostgreSQL query result.
        :rtype: bool | tuple
        """
        try:
            self.connector.reconnect()
            self.connector.cursor.execute(struct.query, struct.vars)
            data = self.connector.cursor.fetchall()
            self.connector.connection.commit()
            self.connector.close()

            return tuple(data) if data else True
        except Exception as err:
            self.connector.connection.rollback()
            self.connector.close()
            raise err

    def executemany(self, struct: StructurePostgreSQLExecute, /) -> bool:
        """
        Execute multiple SQL queries on PostgreSQL database.
        Generally used for batch insertion, update, and deletion of data.

        :param struct: PostgreSQL execute structure.
        :type struct: StructurePostgreSQLExecute
        :return: Execute status.
        :rtype: bool
        """
        try:
            self.connector.reconnect()
            self.connector.cursor.executemany(struct.query, struct.vars)
            self.connector.connection.commit()
            self.connector.close()

            return True
        except Exception as err:
            self.connector.connection.rollback()
            self.connector.close()
            raise err

    def multiexecute(self, structs: Sequence[StructurePostgreSQLExecute], /) -> bool:
        """
        Execute multiple SQL queries on PostgreSQL database.

        :param structs: Sequence of PostgreSQL execute structures.
        :type structs: Sequence[StructurePostgreSQLExecute]
        :return: Execute status.
        :rtype: bool
        """
        try:
            self.connector.reconnect()
            for struct in structs:
                if struct.query.lower().startswith("select"):
                    raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_NOT_SELECT)
                self.connector.cursor.execute(struct.query, struct.vars)
            self.connector.connection.commit()
            self.connector.close()

            return True
        except Exception as err:
            self.connector.connection.rollback()
            self.connector.close()
            raise err

    def select(self, struct: StructurePostgreSQLExecute, /) -> Tuple[NamedTuple, ...]:
        """
        Select data from PostgreSQL database.

        :param struct: PostgreSQL Query structure.
        :type struct: StructurePostgreSQLExecute
        :return: Query result.
        :rtype: tuple
        """
        if not struct.query.lower().startswith("select"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_SELECT)

        try:
            return self.execute(struct)
        except Exception as err:
            raise err


class PostgreSQLSimpleConnectionPool:

    def __init__(self, host: str, port: int, user: str, password: str, database: str, /):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database

        self.__pool = psycopg2.pool.SimpleConnectionPool(
            2,
            20,
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database,
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

    def execute(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        connection: psycopg2.extensions.connection = self.__pool.getconn()
        cursor: CustomPostgreSQLCursor = connection.cursor(cursor_factory=CustomPostgreSQLCursor)
        try:
            cursor.execute(struct.query, struct.vars)
            data = cursor.fetchall()
            connection.commit()

            cursor.close()
            if connection:
                self.__pool.putconn(connection)

            return tuple(data) if data else True
        except Exception as err:
            connection.rollback()

            cursor.close()
            if connection:
                self.__pool.putconn(connection)

            raise err

    def __del__(self):
        self.__pool.closeall()
