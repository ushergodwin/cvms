from decouple import config as env


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

Config = {
    "HOST": env("HOST"),
    "USER": env("USER"),
    "PASSWORD": env("PASSWORD"),
    "DATABASE": env("DATABASE"),
    "DB_DRIVER": env("DB_DRIVER"),
    "PORT": int(env("PORT"))
}
