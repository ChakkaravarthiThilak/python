import pymysql
db=pymysql.connect(
host="localhost",
user="root",
password="password",
database="py")
excussor=db.cursor()
sql1="update pythonteam SET course='python' where name='Hari'"
try:
    excussor.execute(sql1)
    db.commit()
except:
    db.rollback()

