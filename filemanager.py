"""
function:   open file
"""
import data
import reader
import connector
import pymysql
import pymysql.cursors
from time import sleep

def IsExistInShop(list, item):
    for l in list:
        if l['id']==item[0]:
            return True
    return False

def QueryIsMatched(product):
    sql = "SELECT COUNT(*) FROM s_articles_attributes WHERE id=(SELECT articleID FROM s_articles_details WHERE id=" + product[0] + ")"
    return sql

def QueryGetIdFromAttributes():
    sql = "SELECT id FROM s_articles_attributes"
    return sql

def QueryUpdatePurchaseprice(product):
    sql = "UPDATE s_articles_details SET purchaseprice=" + product[1] + " WHERE id=" + product[0]
    return sql

def Test(filepath):
    reader = FileReader(filepath)
    content = reader.csvReadFile()

    db = MysqlConnector(DBHOST, USERID, PASSWD, DBNAME, TBNAME)
    items_on_shop = db.ReadMysql(QueryGetIdFromAttributes())
    for c in content:
        if IsExistInShop(items_on_shop, c):
            db.MysqlUpdate(QueryUpdatePurchaseprice(c))
    """
    for c in content:
        count = db.ReadMysql(QueryIsMatched(c))
        if count[0]['COUNT(*)']:
            db.MysqlUpdate(QueryUpdatePurchaseprice(c))
        sleep(0.001)
    """
def Update():
    shops = {APD, AV, FLC, KST, RKT, SA, ATN, ERP, KHF, PTR, RSM, SCA, VTS, ZR }
    for s in shops:
        print s
        Test(s)

if __name__=='__main__':
    Update()
