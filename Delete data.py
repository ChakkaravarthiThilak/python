import pymysql
db=pymysql.connect(
host="localhost",
user="root",
password="password",
database="py")
excussor=db.cursor()
sql1="delete from python team where name='archana'"
try:
    excussor.execute(sql1)
    db.commit()
except:
    db.rollback()
