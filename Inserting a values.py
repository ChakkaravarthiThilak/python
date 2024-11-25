import pymysql
db=pymysql.connect(
host="localhost",
user="root",
password="password",
database="py")
excussor=db.cursor()
excussor.execute("""insert into pythonteam(name,course,duration)values('archana','python','two'),('hari','java','one')""")
db.commit()


