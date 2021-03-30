import pymysql as mysql
import datetime
import json


def createSqlStr(data):
    key = ""
    val = ""
    dt = datetime.datetime.now()
    for dataKey, dataVal in data.items():
        key += "`"+dataKey.replace("`","\\`")+"`,"
        val += "'"+dataVal.replace("'","\\'")+"',"

    sql = "INSERT INTO `ubiketaoyuan` (" + \
        key+"`datetime`) VALUES ("+val+"'"+str(dt)+"');"

    return sql


db = mysql.connect(host="127.0.0.1", user="admin",
                   passwd="admin", db="mydatabase")
cursor = db.cursor()
with open('u-bike.json', 'r', encoding="utf-8") as fp:
    data = json.load(fp)
    # print(data["retVal"]["2001"]["sna"])

    items = data["retVal"]
    for key in items:
        info = items[key]
        sql = createSqlStr(info)
        cursor.execute(sql)

db.commit()
