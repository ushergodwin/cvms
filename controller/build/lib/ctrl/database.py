__author__ = "Tumuhimbise Godwin"
__copyright__ = "Copyright 2021, The PY-DB Module Project"
__credits__ = ["Ojok David"]
__license__ = "GNU"
__version__ = "1.0.1"
__maintainer__ = "Tumuhimbise Godwin"
__email__ = "godwintumuhimbise96@gmail.com"
__status__ = "Production"

import re as Regx

from controller.ctrl.controller import String
from controller.ctrl.config import Config

DRIVER = None
DB_DRIVER = Config.get("DB_DRIVER")
if DB_DRIVER == "mysqlclient":
    try:
        import MySQLdb

        DB_DRIVER = MySQLdb
    except ImportError:
        raise ImportError()

if DB_DRIVER == "pymysql":
    try:
        import pymysql

        pymysql.install_as_MySQLdb()

        DRIVER = pymysql
    except ImportError:
        raise ImportError()

if DB_DRIVER == "mysqlconnector":
    try:
        import mysql.connector

        DRIVER = mysql.connector
    except ImportError:
        raise ImportError()
    # any other DB_DRIVER needed


class DB:
    _db_instance = DRIVER.connect(
        host=Config.get("HOST"),
        port=Config.get("PORT"),
        user=Config.get("USER"),
        password=Config.get("PASSWORD"),
        database=Config.get("DATABASE")
    )
    _db = None

    _where = ""
    _wheredata = ()
    _affectedRows = 0
    _orderBy = ""
    _lastId = []
    # _firstid= "" mine

    def __int__(self):
        self._db = self._db_instance.cursor()
        # self._db_instance.cursor()
        # return self._db_instance.cursor()

    @staticmethod
    def getDriver():
        """
        The Database Driver in use
        :return: str
        """
        return DB_DRIVER

    @classmethod
    def __connect(cls):
        """
        Connect to the cursor
        :return: Connection Cursor Instance
        """
        cls._db = cls._db_instance.cursor()

    @classmethod
    def __close(cls):
        """
        Closes the cursor
        """
        return cls._db.close()

    @classmethod
    def _reset(cls):

        """
        Resets the state of data instance
        """
        cls._where = ""
        cls._wheredata = ()
        cls._orderBy = ""
        cls._lastId = []
        return cls

    @classmethod
    def create_db(cls, db_name):
        """
        :param db_name A string of the database name to create
        :return bool
        """
        cls.__connect()
        sql = "CREATE DATABASE " + db_name
        execute = cls._db.execute(sql)
        cls.__close()
        return execute

    @classmethod
    def getAll(cls, columns: str, table: str, limit=None):
        """
        The where method should be called first if a condition is needed while fetching data
        Args:
            columns (str): A string containing column names separated by commas
            table (str): A string of table name
            limit (int): An integer containing the number of rows to be returned
        Returns:
            tuple: Data fetched from the run query
        """

        sql = "SELECT " + columns + " FROM " + table
        if cls._where != "":
            sql += cls._where
        if cls._orderBy != "":
            sql += cls._orderBy
        if limit is not None:
            sql += " LIMIT " + String.to_string(limit)
        cls.__connect()
        cls._db.execute(sql) if len(cls._wheredata) == 0 else cls._db.execute(sql, cls._wheredata)
        cls._reset()
        data = cls._db.fetchall()
        cls.__close()
        return data

    @classmethod
    def where(cls, condition: dict, sec=False):
        """
        Args:
            condition (dict): A dictionary containing column name and value to supply in the condition
            sec (bool): If set to True, the third (3rd) pair of key and value is used as a second AND
        condition hence forming WHERE AND AND, else OR is used hence forming WHERE AND OR
        """

        keys = tuple((condition.keys()))
        values = tuple((condition.values()))
        cls._wheredata += values
        sql = ""
        if len(condition) >= 1:
            sql += " WHERE " + keys[0] + " = %s"
        if len(condition) >= 2:
            sql += " AND " + keys[1] + " = %s"
        if sec is not False:
            if len(condition) >= 3:
                sql += " AND " + keys[1] + " = %s"
        else:
            if len(condition) >= 3:
                sql += " OR " + keys[1] + " = %s"
        cls._where += sql

    @classmethod
    def orderBy(cls, column_name: str, order="ASC"):
        """
        Args:
            column_name (str): The name of the column to use in the order by statement
            order (str): The type of ordering to use. Default is Ascending
        Returns:
            DB instance
        """

        cls._orderBy += " ORDER BY " + column_name + " " + order
        return cls

    @classmethod
    def getOneRow(cls, column: str, table: str, limit=1):
        """
        Args:
            column (str): A string containing column names separated by commas
            table (str):  A string containing the table name to fetch data from
            limit (int):  Number of rows to return 1 (constant)
        Returns:
            tuple:  containing one row of data
        """

        sql = "SELECT " + column + " FROM " + table
        if cls._where != "":
            sql += cls._where
        if cls._orderBy != "":
            sql += cls._orderBy
        sql += " LIMIT " + String.to_string(limit)
        cls.__connect()
        cls._db.execute(sql) if len(cls._wheredata) == 0 else cls._db.execute(sql, cls._wheredata)
        cls._reset()
        data = cls._db.fetchall()
        return data

    @classmethod
    def not_empty(cls, collection):
        """
        Args:
            collection (tuple): A tuple with data from the database
        Returns:
            bool: True if the tuple is not empty
        """

        if collection is None:
            return False
        else:
            return True

    @classmethod
    def getOneValue(cls, column: str, table: str):
        """
        Args:
            column (str): A column name to fetch
            table (str): A table name
        Returns:
            str: String of data
        """
        res = ""
        sql = "SELECT " + column + " FROM " + table
        if cls._where != "":
            sql += cls._where
        cls.__connect()
        cls._db.execute(sql) if len(cls._wheredata) == 0 else cls._db.execute(sql, cls._wheredata)
        cls._reset()
        value = cls._db.fetchone()
        cls.__close()
        if cls.not_empty(value):
            res = value[0]

        return res

    @classmethod
    def insertData(cls, data_values: dict, table: str):
        """
        Args:
            data_values (dict): A dictionary with pairs of key and value representing the column name and its value
            table (str):        The name of the table where to insert the data
        Returns:
            bool: Returns true on success and False on failure.

            You can access the number of affected rows by calling the affectedRows method
        """

        keys = data_values.keys()
        columns = (", ".join(keys))
        placeholder = ""
        place = list()
        values = tuple(data_values.values())
        sql = "INSERT INTO " + table + " (" + columns + ") VALUES ("
        pl = 0
        while pl <= len(keys) - 1:
            place.append("%s")
            pl += 1
        placeholder += ", ".join(tuple(place))
        sql += placeholder + ")"
        cls.__connect()
        cls._db.execute(sql, values)
        cls._db_instance.commit()
        cls._affectedRows = cls._db.rowcount
        cls._lastId.append(cls._db.lastrowid)
        cls._reset()
        row_count = cls._db.rowcount
        cls.__close()
        if row_count > 0:
            return True
        else:
            return False

    @classmethod
    def insertMany(cls, columns: list, table_name: str, table_data: list):
        """
        Args:
            columns (list): A list containing table column names
            table_name (str): The name of the table where to insert the data
            table_date (list): A list of tuples containing data to insert
        Returns:
            bool Returns true on success and False on failure.

            You can access the number of affected rows by calling the affectedRows method
        """

        if type(columns) is not list or type(table_data) is not list:
            raise Exception("Expected the data parsed as columns and table data to be of type list but "
                            "saw " + String.to_string(type(columns)) + " and " + String.to_string(type(table_data)))
        columns_names = (", ".join(tuple(columns)))
        keys = tuple(columns)
        placeholder = ""
        place = list()
        sql = "INSERT INTO " + table_name + " (" + columns_names + ") VALUES ("
        pl = 0
        while pl <= len(keys) - 1:
            place.append("%s")
            pl += 1
        placeholder += ", ".join(tuple(place))
        sql += placeholder + ")"
        cls.__connect()
        cls._db.executemany(sql, table_data)
        cls._db_instance.commit()
        cls._affectedRows = cls._db.rowcount
        cls._lastId.append(cls._db.lastrowid)
        cls._reset()
        row_count = cls._db.rowcount
        cls.__close()
        if row_count > 0:
            return True
        else:
            return False

    @classmethod
    def update(cls, table_data: dict, table_name: str):
        """
        The where method should be called first to supply a condition
        Args:
            table_data (dict): A dictionary of key and value pairs representing column name and value
            table_name (str): The name of the table where to update
        Returns:
            bool: Returns true on success and False on failure.

            You can access the number of affected rows by calling the affectedRows method
        """

        sql = "UPDATE " + table_name + " SET "
        key = table_data.keys()
        column_list = []
        column_values = list(table_data.values())
        ct = 0
        while ct <= len(key) - 1:
            column_list.append(tuple(key)[ct] + " = %s")
            ct += 1
        column_keys = ", ".join(tuple(column_list))
        sql += column_keys
        if cls._where == "":
            raise Exception('Expected the where() method to be called first')
        sql += cls._where
        column_values += list(cls._wheredata)
        update_data = tuple(column_values)
        cls.__connect()
        cls._db.execute(sql, update_data)
        cls._db_instance.commit()
        cls._affectedRows = cls._db.rowcount
        row_count = cls._db.rowcount
        cls.__close()
        if row_count > 0:
            return True
        else:
            return False

    @classmethod
    def deleteAll(cls, table_name: str):
        """
        Args:
            table_name (str): The name of the table to delete data from
        Returns:
            bool: Returns true on success and False on failure.

            You can access the number of affected rows by calling the affectedRows method
        """

        sql = "TRUNCATE TABLE " + table_name
        cls.__connect()
        cls._db.execute(sql)
        cls._affectedRows = cls._db.rowcount
        row_count = cls._db.rowcount
        cls.__close()
        if row_count > 0:
            return True
        else:
            return False

    @classmethod
    def trash(cls, table_name: str):
        """
        The where method should be called first to supply a condition
        Args:
            table_name (str): The name of the table to delete data from
        Returns:
            bool: Returns true on success and False on failure.

            You can access the number of affected rows by calling the affectedRows method
        """

        if cls._where == "":
            raise Exception("Expected the where method to be called first")
        sql = "DELETE FROM " + table_name
        sql += cls._where
        cls.__connect()
        cls._db.execute(sql, cls._wheredata) if len(cls._wheredata) != 0 else cls._db.execute(sql)
        cls._affectedRows = cls._db.rowcount
        row_count = cls._db.rowcount
        cls.__close()
        if row_count > 0:
            return True
        else:
            return False

    @classmethod
    def query(cls, sql: str, query_data: list):

        """
        Exceute a custom query.
        Args:
            sql (str): The correct sql query to execute. Should be a select query of prepared statments
            query_data (list): A list of values for the prepared statement
        Raises: 
            Exception: when the parsed query is not a prepared statement
        Returns:
        tuple
        """

        data_type = type(query_data)
        if data_type is not list:
            raise Exception("Expected the query data to be of type list " + String.to_string(data_type) + " given")
        reg = "%s"
        if Regx.search(reg, sql):
            cls.__connect()
            cls._db.execute(sql, tuple(query_data))
            data = cls._db.fetchall()
            cls.__close()
            return data
        else:
            raise Exception("Expected a prepared query statement with placeholders")

    @classmethod
    def rowCount(cls, column_name: str, table_name: str):
        """
        Count the number of rows for a given column
        Args:
            column_name (str): The name of the column to count from
            table_name (str):  The name of the table where to carry out a transaction
        Returns:
            int: The total count 
        """

        sql = "SELECT COUNT(" + column_name + ") FROM " + table_name
        if cls._where != "":
            sql += cls._where
        cls.__connect()
        cls._db.execute(sql, cls._wheredata) if len(cls._wheredata) != 0 else cls._db.execute(sql)
        c_row = cls._db.fetchone()
        cls.__close()
        return c_row[0]

    @classmethod
    def maxValue(cls, column_name: str, table_name: str):
        """
        Get the maximum value of the data in a specific column

         Args:
            column_name (str): The name of the column to pick the max value
            table_name (str): The name of the table where to carry out a transaction
         Returns:
            Maximum value from the selected data
         """

        sql = "SELECT MAX(" + column_name + ") FROM " + table_name
        if cls._where != "":
            sql += cls._where
        cls.__connect()
        cls._db.execute(sql, cls._wheredata) if len(cls._wheredata) != 0 else cls._db.execute(sql)
        max_row = cls._db.fetchone()
        cls.__close()
        return max_row[0]

    @classmethod
    def minValue(cls, column_name: str, table_name: str):
        """
        Get the minimum value of the data in a specific column

        Args:
            column_name (str): The name of the column to pick the max value
            table_name (str):  The name of the table where to carry out a transaction
        Returns:
            Minimum value from the selected data
        """

        sql = "SELECT MIN(" + column_name + ") FROM " + table_name
        if cls._where != "":
            sql += cls._where
        cls.__connect()
        cls._db.execute(sql, cls._wheredata) if len(cls._wheredata) != 0 else cls._db.execute(sql)
        min_row = cls._db.fetchone()
        cls.__close()
        return min_row[0]

    @classmethod
    def affectedRows(cls):
        """
        Get the number of aaffected rows after query execution

        Returns:
            int The number of affected rows
        """

        return cls._affectedRows

    @classmethod
    def lastInsertId(cls):
        """
        Get the last Insert Id
         Returns:
            int|str The last id from the data being inserted
         """
        return cls._lastId[0]

    @classmethod
    def join(cls, columns: str, tables: dict, type_of_join='INNER JOIN'):

        """
        Join 2 tables and return their data

        Args:
            columns (str): A string of columns seperated with commas
            tables (dict): A dictionary of table name and column name to be used in joining
            type_of_join (str): The type of join to use. default is INNER JOIN
        Returns:
            list: of tuples containing the fetched rows
        
        You can only join 2 table. if you want to join more that 2 tables, use the query() method
        """
        sql = "SELECT " + columns + " FROM "
        table_names = list(tables.keys())
        join_columns = list(tables.values())
        sql += table_names[0] + " " + type_of_join + " " + table_names[1] + " ON " + table_names[0]
        sql += "." + join_columns[0] + " = " + table_names[1] + "." + join_columns[1]
        if cls._where != "":
            sql += cls._where
        cls.__connect()
        cls._db.execute(sql) if len(cls._wheredata) == 0 else cls._db.execute(sql, cls._wheredata)
        cls._reset()
        data = cls._db.fetchall()
        return data
