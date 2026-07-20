import sqlite3

connection = sqlite3.connect("cars.db")
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS cardata""")
cursor.execute("""
	CREATE TABLE IF NOT EXISTS cardata(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		make TEXT NOT NULL,
		model TEXT NOT NULL,
		year INTEGER,
		mpg DECIMAL(3,2)
		)
	""")

# it checks if cars.db exists as to not overwrite it 

# next section will use placeholders "?". This helps us prevent sql injection attacks

cursor.execute("INSERT INTO cardata (make, model, year, mpg) VALUES (?,?,?,?)", ("Honda","Pilot",2025,20.25))
cursor.execute("INSERT INTO cardata (make, model, year, mpg) VALUES (?,?,?,?)", ("ford", "mustang", 1975, 8))
# the place holders are important because if we decided to do it like:
# query = f"INSERT INTO cardata {userdata}" or whatever then it would
# pass as one string into the sql, and then the dickheads could be like
# "where 1 = 1" and skip checkers for password or whatever.

connection.commit()

# retrieving all rows
cursor.execute("SELECT * FROM cardata")
rows = cursor.fetchall()
for row in rows:
	print(row)

# fetchign a single row
# has to have that "," at the end because its not a "single tuple"
cursor.execute("SELECT * FROM cardata WHERE make = ?", ("ford",))
row = cursor.fetchone()
print(row)

# must be closed to free up system resources and finalize transactions
connection.close()


