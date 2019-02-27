#!/usr/bin/python
"""
function    : Get Data from Mysql
"""
import pymysql


class MysqlConnector():
    def __init__(self, dbhost, userid, passwd, dbname, tbname):
        self.dbhost = dbhost
        self.userid = userid
        self.passwd = passwd
        self.dbname = dbname
        self.tbname = tbname
        self.sql = sql

    def ConnectMysql(self):
        ## open database connection ##
        mysql = pymysql.connect(host = self.dbhost,
                                user = self.userid,
                                password = self.passwd,
                                db = self.dbname,
                                charset = 'utf8',
                                autocommit = False, # to protect mysql data
                                cursorclass = pymysql.cursors.DictCursor)

        return mysql

    def ReadMysql(self, sql):
        mysql = self.ConnectMysql()
        result = []
        ## get data as list ##
        with mysql.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def UpdateMysql(self, sql):
        mysql = self.ConnectMysql()
        result = []
        ## execute sql ##
        with mysql.cursor() as cursor:
            cursor.execute(sql)
            mysql.commit()
            mysql.close()

    def GetSellingList():
        mysql = MysqlConnector(DBHOST, USERID, PASSWD, DBNAME, TBNAME)
        on_sale = mysql.ReadMysql(SQL_GET_ALL_ID)
        return on_sale



def
