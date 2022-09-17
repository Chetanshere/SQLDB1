import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd="Ch9611@#")
cursor = mydb.cursor()
s3= "insert into chetanshere.chetancodetails values(101 , 'chetan shere' , 'chetanshere24@gmail.com', 40000, 30)"
cursor.execute(s3)
mydb.commit()
cursor.execute("select * from chetanshere.chetancodetails")
for i in cursor.fetchall():
    print (i)
cursor.execute(s3)
cursor.execute(s3)
#cursor.execute("create database chetan")
cursor.execute("show databases")


