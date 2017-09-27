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
    def insert_drama_name(cls, dramaid, dramaname, category, imgurl):
        sql = 'INSERT INTO drama_name(dramaid, dramaname, category, imgurl)VALUES(%(dramaid)s,%(dramaname)s,%(category)s,%(imgurl)s)'
        value = {
            'dramaid': dramaid,
            'dramaname': dramaname,
            'category': category,
            'imgurl': imgurl
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_dramaid(cls, dramaid):
        sql = 'SELECT EXISTS(SELECT 1 FROM drama_name WHERE dramaid=%(dramaid)s)'
        value = {
            'dramaid': dramaid
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def insert_baidu_url(cls, dramaid, dramaurl):
        sql = 'INSERT INTO baidu_url (dramaid, dramaurl)VALUES(%(dramaid)s,%(dramaurl)s)'
        value = {
            'dramaid': dramaid,
            'dramaurl': dramaurl
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_url(cls, dramaurl):
        sql = 'SELECT EXISTS(SELECT 1 FROM baidu_url WHERE dramaurl=%(dramaurl)s)'
        value = {
            'dramaurl': dramaurl
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]