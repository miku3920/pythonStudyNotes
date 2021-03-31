import pymysql as mysql

db = mysql.connect(host="172.19.107.140", 
                   user="powenko", 
                   passwd="powenko", 
                   db="mydatabase")
cursor = db.cursor()
sql = "INSERT INTO `ubiketaoyuan` (`sna`) VALUES ('miku3920');"
cursor.execute(sql)
db.commit()
