import pymysql

db = pymysql.connect(host='101.101.210.141',
                     port=3306,
                     user='study',
                     passwd='study!@#$%',
                     db='sks0852',
                     charset='utf8')


# cursor = db.cursor()
# sql = """
# CREATE TABLE sks(
# name varchar(20) NOT NULL,
# math INT NULL,
# english INT NULL,
# PRIMARY KEY(name)
# )
# """
# cursor.execute(sql)
# db.commit()

# cursor = db.cursor()
# sql = """
# INSERT INTO sks (name, math, english)
# VALUES('서강식', 80, 20)
# """
# cursor.execute(sql)
# db.commit()

# sql = """
# UPDATE sks
# SET math = 10, english = 10
# WHERE name = '서강식'
# """
# cursor.execute(sql)
# db.commit()
cursor = db.cursor()
# sql = """
# SELECT *
# FROM sks
# """

sql="""
select *
from classicmodels.orderdetails 
where orderLineNumber > 10;
"""



cursor.execute(sql)
rs = cursor.fetchall()
print(rs)



cursor.close()
db.close()