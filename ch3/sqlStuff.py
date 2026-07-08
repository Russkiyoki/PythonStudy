import mysql.connector

conn = mysql.connector.connect(
	host='localhost',
	user='root',
	password='7590',
	database='employee_db'
)

cursor = conn.cursor()

#cursor.execute("CREATE TABLE tblemployee (emp_id INT, name VARCHAR(255), salary INT)")

try: 

	cursor.execute("INSERT INTO tblemployee VALUES(1, 'Amit', 50000), (2, 'Nisha', 60000), (3, 'Ravi', 55000)")
	#cursor.execute("INSERT INTO tblemployee VALUES(1, 'Elisey', 67000)")

	conn.commit() #saving the changes
	print("Records inserted sucessfully...")

except:
	conn.rollback() #revert changes if an error occurs
conn.close()
