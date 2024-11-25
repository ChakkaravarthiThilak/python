import pymysql
db=pymysql.connect(
host="localhost",
user="root",
password="password",
database="py")
excussor=db.cursor()
excussor.execute("""CREATE table pythonteam(name varchar(20),course varchar(20)  ,duration varchar(3))""")


