import mysql.connector

conn = mysql.connector.connect(
	host='localhost',
	user='root',
	password='7590',
	database='employee_db'
)

cursor = conn.cursor() #setting up a cursor

cursor.execute("SELECT * FROM tblemployee")
records = cursor.fetchall()

for row in records:
	print(row)

conn.close()
