# project 4
import pymysql as mysql

db = mysql.connect(host="127.0.0.1", 
                   user="admin",
                   passwd="admin", 
                   db="mydatabase")
cursor = db.cursor()
sql = """
CREATE TABLE `mydatabase`.`spamtable` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `time` DATETIME NOT NULL , 
    `spam` BOOLEAN NOT NULL , 
    `user_id` VARCHAR(32) NOT NULL , 
    `chat_id` VARCHAR(32) NOT NULL , 
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;
"""
cursor.execute(sql)
db.commit()