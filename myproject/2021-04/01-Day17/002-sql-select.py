import pymysql as mysql

db = mysql.connect(host="127.0.0.1", 
                   user="admin", 
                   passwd="admin", 
                   db="mydatabase")
cursor = db.cursor()
cursor.execute("SELECT * FROM `parktable`")
result = cursor.fetchall()
print(result[0])