import pymysql
db=pymysql.connect(
host="localhost",
user="root",
password="password")
excussor=db.cursor()
excussor.execute("CREATE DATABASE csc")
