import pymysql
db=pymysql.connect(
host="localhost",
user="root",
password="password",
database="py")
excussor=db.cursor()
excussor.execute("SELECT*from pythonteam")
res=excussor.fetchall()
print(res)


