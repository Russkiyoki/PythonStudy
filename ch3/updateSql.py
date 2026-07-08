import mysql.connector

conn=mysql.connector.connect(
 	host='localhost',
	user='root',
	password='7590',
	database='employee_db'
)

cursor = conn.cursor()

try:
	cursor.execute("UPDATE tblemployee SET name='Rammus', salary=100 WHERE emp_id=1")
	conn.commit() #save change
	print("Record updated successfully...\n")

except:
	conn.rollback() # dont make the changes

conn.close()
