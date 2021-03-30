import pymysql as mysql

db = mysql.connect(host="127.0.0.1", user="admin",
                 passwd="admin", db="mydatabase")
cursor = db.cursor()
sql="INSERT INTO `mytable` (`value01`, `value02`, `value03`, `value04`) VALUES ('a', 'b', 'c', 'd');"
cursor.execute(sql)
db.commit()