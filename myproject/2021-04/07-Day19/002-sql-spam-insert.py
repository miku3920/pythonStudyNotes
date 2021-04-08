# project 4
import pymysql as mysql
from datetime import datetime
import csv

def createSqlStr(head,data):
    key = "`"+head[0].replace("`", "\\`")+"`"
    val = "'"+str(datetime.fromtimestamp(int(data[0]))).replace("'", "\\'")+"'"

    for i in range(1,len(data)):
        key += ",`"+head[i].replace("`", "\\`")+"`"
        val += ",'"+data[i].replace("'", "\\'")+"'"

    sql = "INSERT INTO `spamtable` (" + \
        key+") VALUES ("+val+");"

    return sql

with open('spam-distribution.csv', 'r', newline='', encoding='utf-8') as fp:
    read = csv.reader(fp, delimiter=',')
    header = next(read)
    data = list(read)

db = mysql.connect(host="127.0.0.1", user="admin",
                   passwd="admin", db="mydatabase")
cursor = db.cursor()
for item in data:
    sql = createSqlStr(header,item)
    cursor.execute(sql)
db.commit()
