import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd="Ch9611@#")
cursor = mydb.cursor()
cursor.execute("select employee_id , emp_mailid from chetanshere.chetancodetails")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))