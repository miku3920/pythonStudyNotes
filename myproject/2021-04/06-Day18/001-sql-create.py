import pymysql as mysql

db = mysql.connect(host="127.0.0.1", 
                   user="admin",
                   passwd="admin", 
                   db="mydatabase")
cursor = db.cursor()
sql = """
CREATE TABLE `mydatabase`.`mytable` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `value01` VARCHAR(255) NOT NULL , 
    `value02` VARCHAR(255) NOT NULL , 
    `datetime` DATETIME NOT NULL , 
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;
"""
cursor.execute(sql)
db.commit()
