import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd="Ch9611@#")
cursor = mydb.cursor()
#cursor.execute("create database chetanshere")
#s = "create table chetanshere.chetancodetails(employee_id int(10) , emp_name varchar(80) , emp_mailid varchar(30) , emp_salary int(6) , emp_attendance int(34))"
#q1 = cursor.execute(s)
q2 = cursor.execute("select * from chetanshere.chetancodetails")
print(q2)



