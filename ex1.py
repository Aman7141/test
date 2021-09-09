import mysql.connector
from mysql.connector import Error

try:

	con=mysql.connector.connect(host='localhost',user='root',password='',database='university')

	create_table = """ CREATE TABLE institutes (col_id int(20) NOT NULL, colgname varchar(20) NOT NULL,
	principal varchar(30) NOT NULL, contactno int(10) NOT NULL, PRIMARY KEY(col_id)) """
	cursor=con.cursor()
	result=cursor.execute(create_table)
	print("Created Successfully!!!!")


except mysql.connector.Error as e:
	print("Table not created ",e)

finally:
	cursor.close()
	conn.close()
