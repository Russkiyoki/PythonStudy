import mysql.connector

conn = mysql.connector.connect(
	host='localhost',
	user='root',
	password='7590',
	database='employee_db'
	)

cursor = conn.cursor()

try:
	cursor.execute("DELETE FROM tblemployee WHERE emp_id=1")
	conn.commit()
	print("Deleted successfully...")

except:
	conn.rollback() # undo if fail

conn.close()

