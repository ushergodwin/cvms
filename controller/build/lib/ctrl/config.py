"""
If you use pymysql or mysqlclient or MySQLdb drivers, then the
ENGINE: 'django.db.backends.mysql'
put this code bellow before any python code, recommended in manage.py
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass

If you use mysql connector/python, then the
ENGINE: mysql.connector.django
"""
""" DB DRIVERS USE ONE"""
""" MAKE SURE THAT THE DRIVER IS INSTALLED FIRST"""
DB_DRIVER_01 = "mysqlclient"

DB_DRIVER_02 = "pymysql"

DB_DRIVER_03 = "mysqlconnector"

Config = {
    "HOST": 'localhost',
    "USER": 'root',
    "PASSWORD": 'groupc',
    "DATABASE": 'gema',
    "DB_DRIVER": DB_DRIVER_02,
}
