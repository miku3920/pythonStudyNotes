import urllib.request as httplib
from os import path
import json
import ssl
import pymysql as mysql
import datetime


def createSqlStr(data):
    key = ""
    val = ""
    switch = [
        'pm_name',
        'pm_overview',
        'pm_location',
        'pm_lon',
        'pm_lat'
    ]
    for dataKey, dataVal in data.items():
        if dataKey in switch:
            key += "`"+dataKey.replace("`", "\\`")+"`,"
            val += "'"+dataVal.replace("'", "\\'")+"',"

    sql = "INSERT INTO `parktable` (" + \
        key+"`datetime`) VALUES ("+val+"NOW());"

    return sql


"""
資料來源:
公園基本資料
https://data.taipei/#/dataset/detail?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6

pm_name(公園名稱)、pm_overview(公園概述)、pm_lon (經度)、pm_lat( 緯度)、pm_unit(管理單位)、
pm_construction(建造年度)、pm_location(公園位置)、pm_area(公園面積)、pm_opening_s(開放時間-開始)、
pm_opening_e(開放時間-結束)、pm_libie(里別)、pm_phone(聯絡電話)、pm_sports(體健設施)、
pm_recreation(遊樂設施)、pm_service(服務設施)、pm_other(古蹟設施)、pm_transit(交通資訊)、
pm_name_eng(公園英文名稱)、pm_ecology(是否為生態公園)、pm_type(類別)

"""

if path.exists('park.json'):
    with open('park.json', 'r') as f:
        data = json.load(f)
else:
    url = "https://parks.taipei/parks/api/"
    req = httplib.Request(url)
    context = ssl._create_unverified_context()  # <----
    reponse = httplib.urlopen(url, context=context)  # <----
    contents = reponse.read().decode("utf-8")
    data = json.loads(contents)
    with open('park.json', 'w') as f:
        json.dump(data, f)


db = mysql.connect(host="127.0.0.1", user="admin",
                   passwd="admin", db="mydatabase")
cursor = db.cursor()
for item in data:
    sql = createSqlStr(item)
    cursor.execute(sql)
db.commit()
