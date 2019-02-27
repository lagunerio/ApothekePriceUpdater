"""
function:   open file
"""
import data
import reader
import connector
import pymysql
from time import sleep

SQL_GET_ALL_ID = "SELECT id FROM s_articles_attributes"

def IsExistInShop(list, item):
    for l in list:
        if l['id']==item[0]:
            return True
    return False

## not in use; mysql overload error ##
def QueryIsMatched(product):
    sql = "SELECT COUNT(*) FROM s_articles_attributes WHERE id=(SELECT articleID FROM s_articles_details WHERE id=" + product[0] + ")"
    return sql

def QueryUpdatePurchaseprice(product):
    sql = "UPDATE s_articles_details SET purchaseprice=" + product[1] + " WHERE id=" + product[0]
    return sql

## get list of 'id' from s_articles_attributes from mysql ##
def GetSellingList(mysql):
        #mysql = connector.MysqlConnector(DBHOST, USERID, PASSWD, DBNAME, TBNAME)
        on_sale = mysql.ReadMysql(SQL_GET_ALL_ID)
        return on_sale

## depress mysql overload error by using less mysql query ##
def IsExistingInSellingList(item, on_sale):
    for s in on_sale:
        if s == item:
            return True
    return False

def Update(filepath):
    mysql = connector.MysqlConnector(DBHOST, USERID, PASSWD, DBNAME, TBNAME)
    filemanager = reader.FileReader(filepath)

    itemlist = filemanager.csvReadFile()
    updated_n = 0

    for i in itemlist:
        if IsExistingInSellingList(i, itemlist):
            mysql.UpdateMysql(QueryUpdatePurchaseprice(i))
            updated_n += 1  ## count updated items to check

    return updated_n

def main():
    for s in data.shops:
        print s
        updated_n = Update(s)
        print updated_n

if __name__=='__main__':
    main()
