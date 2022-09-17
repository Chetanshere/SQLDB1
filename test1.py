import mysql.connector as connection

mydb = connection.connect(host= "localhost" , user ="root" , passwd ="Ch9611@#")
print(mydb)
cursor= mydb.cursor()
#cursor.execute("create database shere")
cursor.execute("show databases")
s5=(cursor.fetchall())
l=[]
for i in s5:
    l.append(i)

l.sort()
print(l)
