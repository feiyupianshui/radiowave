#!/use/bin/env python
#_*_coding:utf-8_*_
import mysql.connector
from radiowave import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:
    @classmethod
    def insert_rw_name(cls, dramaname, category, imgurl):
        sql = 'pass'
        value = {}
        cur.execute(sql, value)
        cnx.commit()


    @classmethod
    def select_rw(cls, url):
        sql = 'pass'
        value = {}
        cur.execute(sql, value)
        return cur.fetchall()[0]