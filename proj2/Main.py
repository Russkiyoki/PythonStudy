# Elisey Voichishin cs113 study.com
# implementing crud with sqlite
import sqlite3
import re

# TO DO
# 1: fix bug where it doesnt save previous data base
# 2: Finish Delete()

# create an app that creates a students database and then:
# creates a student: id (integer, primary key), name (text), grade(text), and email
# # email has to be a valid one, check via regex for '@'
# provide a simple menu for:
# # creating a student
# # view student records
# # updating a student
# # delete a student
# # exit menu

# have each of the CRUD be their own function for readability
# use try-except blocks
# ensure that db is saved persistently, like saved after multiple runs

# function to create a new student

# Function to check if Grade is valid, returns true or false 
def gradeChecker(grade):
    if not re.match("^[A-F][-+]?$", grade.upper()):
        print("Invalid grade, try again", grade)
        return False
    return True

# Function to check if email is valid, returns true or false
def emailChecker(email):
    emailPattern = re.compile(r"^.+@.+\..+$") 
    # if email doesnt match, exit
    if not re.match(emailPattern, email):
        print("Invalid email, try again")
        return False
    return True

# Function to check if name is valid, returns true or false
def nameChecker(name):
    # if name has something not letters
    if not re.match("^[A-Za-z]+$", name):
        print("Invalid name, try again")
        return False
    return True

# function to create new student and insert into database
def create(cur, name, grade, email):
    # if three pass, insert
    if gradeChecker(grade) and emailChecker(email) and nameChecker(name):
        try:
            cur.execute("INSERT INTO students (name, grade, email) VALUES (?,?,?)", (name,grade,email))
        except sqlite3.Error as e:
            print(f"Error adding: {e}")
    else:
        print("Sorry! Invalid data")

# function to read all students or a specific student via id
def read(cur, id=None):

    # user did not specify, so print all
    if id == None:
        try:
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Error reading: {e}")

    elif id != None:
        try:
            # use the question mark to prevent sql injection 
            cur.execute("SELECT * FROM students WHERE id = ?", (id,))
            row = cur.fetchone()
            print(row)
        except sqlite3.Error as e:
            print(f"Error reading: {e}")

 # function to update a students info
def update(cur, id):
    while True:
        choice = input("What would you to modify? (name, grade, email)\n")
        choice = choice.lower()
        if choice.lower() not in ["id", "name", "grade", "email"]:
            print("Invalid selection, try again\n")

        elif choice == "name":
            newName = input("Please enter new name\n")
            if nameChecker(newName):
                try:
                    cur.execute("UPDATE students SET name = ? WHERE id = ?", (newName,id))
                    break
                except sqlite3.Error as e:
                    print(f"Error updating: {e}")

        elif choice == "grade":
            newGrade = input("Please enter new grade\n")
            if gradeChecker(newGrade):
                try:
                    cur.execute("UPDATE students SET grade = ? WHERE id = ?", (newGrade,id))
                    break
                except sqlite3.Error as e:
                    print(f"Error updating: {e}")

        elif choice == "email":
            newEmail = input("Please enter new email\n")
            if emailChecker(newEmail):
                try:
                    cur.execute("UPDATE students SET email = ? WHERE id = ?", (newEmail,id))
                    break
                except sqlite3.Error as e:
                    print(f"Error updating: {e}")

        
        

# function to delete a student via id 
def delete(id):
    pass



def exit(con):
    print("Have a nice day!\n")
    con.commit()
    con.close()
    return


def main():
    try:
        connection = sqlite3.connect("school.db")
        cursor = connection.cursor()
        cursor.execute("""DROP TABLE IF EXISTS students""")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade TEXT NOT NULL,
                email TEXT NOT NULL
                )
            """)
    except sqlite3.Error as e:
        print(f"Error: {e}")

    # my constant loop until they "exit"()
    while True:
        print("########### Student Records ###########")
        print("Valid options: create, read, update, delete, exit")
        choice = input("what would you like to do?\n")
        choice = choice.lower()

        if choice not in ["create", "read", "update", "delete", "exit"]:
            print("Invalid selection, try again...")

        elif choice == "create":
            name = input("What is the student's name?\n")
            grade = input("What is the student's grade?\n")
            email = input("What is the student's email?\n")
            create(cursor, name, grade, email)

        elif choice == "read":
            id = input("What student via ID would you like to access? or press enter for all students\n")
            if id.strip(): # if they typed something, take of \n at the end
                read(cursor, int(id))
            else: # if they didnt
                read(cursor)

        elif choice == "update":
            id = input("What student via ID would you like to update?\n")
            update(cursor, id)
            pass

        elif choice == "delete":
            pass

        elif choice == "exit":
            exit(connection)
            break


main()


# sources
# https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/ 
