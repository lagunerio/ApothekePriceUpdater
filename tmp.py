"""
function:   open file
"""
import csv
import pymysql

DBHOST = 'localhost'
USERID = 'mymik'
PASSWD = 'geld7914'
DBNAME = 'testumgebung'
TBNAME = 's_articles_attributes'

FILEPATH = "/var/www/vhosts/my-mik.de/Sourcing_File/test.csv"


class FileReader():
    def __init__(self, filepath):
        self.filepath = filepath
        self.filedata = []

    def csvLineByLine(self):
        with open(self.filepath, 'r') as file:
            data = csv.reader(file)
            for d in data:
                self.filedata.append(d)

    def PrintContent(self):
        self.csvLineByLine()
        for d in self.filedata:
            print d

    def GetContent(self):
        self.csvLineByLine()
        return self.filedata

class MysqlConnector():
    def __init__(self, dbhost, userid, passwd, dbname, tbname):
        self.dbhost = dbhost
        self.userid = userid
        self.passwd = passwd
        self.dbname = dbname
        self.tbname = tbname

    def ConnectMysql(self):
        mysql = pymysql.connect(host = self.dbhost,
                                user = self.userid,
                                password = self.passwd,
                                db = self.dbname,
                                charset = 'utf8',
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

    def IsExistingProduct(self, product):
        mysql = self.ConnectMysql()
        sql = "SELECT COUNT(*) FROM s_articles_attributes WHERE id=(SELECT articleID FROM s_articles_details WHERE id=" + product['id'] + ")"
        with mysql.cursor() as cursor:
            cursor.execute(sql)
            count = cursor.fetchall()
        close.mysql()
        return count    # if no matched data exist, return 0
                        # else, return > 0

    def InsertData(self, product):
        mysql = self.ConnectMysql()
        #sql = "UPDATE s_articles_details SET purchaseprice=" + product[1] + " WHERE id=" + product[0]
        sql = "SELECT purchaseprice FROM s_articles_details WHERE id=(SELECT articleID FROM s_articles_details WHERE id=" + product['id'] + ")"
        try:
            with mysql.cursor() as cursor:
                cursor.execute(sql)
        finally:
            mysql.close()



def Test():
    ## read csv file
    reader = FileReader(FILEPATH)
    content = reader.GetContent()

    ## search mysql
    uploader = MysqlConnector(DBHOST, USERID, PASSWD, DBNAME, TBNAME)
    result = uploader.InsertData(content)
    print result

if __name__=='__main__':
    Test()
