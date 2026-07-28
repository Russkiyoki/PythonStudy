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


# Function to check if Grade is valid, returns true or false 
def grade_checker(grade):
    if not re.match("^[A-F][-+]?$", grade.upper()):
        print("Invalid grade, try again")
        return False
    return True

# Function to check if email is valid, returns true or false
def email_checker(email):
    emailPattern = re.compile(r"^.+@.+\..+$") 
    # if email doesnt match, exit
    if not re.match(emailPattern, email):
        print("Invalid email, try again")
        return False
    return True

# Function to check if name is valid, returns true or false
def name_checker(name):
    # if name has something not letters
    if not re.match("^[A-Za-z]+$", name):
        print("Invalid name, try again")
        return False
    return True

# function to create new student and insert into database
def create(cur, name, grade, email):
    # if three pass, insert
    if grade_checker(grade) and email_checker(email) and name_checker(name):
        try:
            cur.execute("INSERT INTO students (name, grade, email) VALUES (?,?,?)", (name,grade,email))
        except sqlite3.Error as e:
            print(f"Error adding: {e}")
    # Dont think ill need an else since my checkers print what fails

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
    cur.execute("SELECT * FROM students WHERE id = ?", (id,))
    row = cur.fetchone()
    print(row)
    while True:
        choice = input("What would you to modify? (name, grade, email, cancel)\n")
        choice = choice.lower()
        if choice.lower() not in ["id", "name", "grade", "email", "cancel"]:
            print("Invalid selection, try again\n")

        elif choice == "name":
            newName = input("Please enter new name\n")
            if name_checker(newName):
                try:
                    cur.execute("UPDATE students SET name = ? WHERE id = ?", (newName,id))
                    break
                except sqlite3.Error as e:
                    print(f"Error updating: {e}")

        elif choice == "grade":
            newGrade = input("Please enter new grade\n")
            if grade_checker(newGrade):
                try:
                    cur.execute("UPDATE students SET grade = ? WHERE id = ?", (newGrade,id))
                    break
                except sqlite3.Error as e:
                    print(f"Error updating: {e}")

        elif choice == "email":
            newEmail = input("Please enter new email\n")
            if email_checker(newEmail):
                try:
                    cur.execute("UPDATE students SET email = ? WHERE id = ?", (newEmail,id))
                    break
                except sqlite3.Error as e:
                    print(f"Error updating: {e}")

        elif choice == "cancel":
            print("Cancelling, returning to menu")
            break

# function to delete a student via id 
def delete(cur, id):
    try:
        cur.execute("SELECT * FROM students WHERE id = ?", (id,))
        row = cur.fetchone()
        print(row)
    except sqlite3.Error as e:
        print(f"Error: {e}")

    while True:
        confirm = input("Are you sure you want to delete this record? (yes, no)\n")
        if confirm.lower() == "yes":
            try:
                cur.execute("DELETE FROM students WHERE id = ?", (id,))
                print("Deleted student!")
                break
            except sqlite3.Error as e:
                print(f"Error deleting student: {e}")
                break
        elif confirm.lower() == "no":
            print("Cancelling, returning to menu...")
            break
        else:
            print("Invalid entry, try again\n")
    

def exit(con):
    print("Have a nice day!\n")
    con.commit()
    con.close()
    return


def main():
    try:
        connection = sqlite3.connect("school.db")
        cursor = connection.cursor()
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
        print()
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

        elif choice == "delete":
            id = input("What student via ID would you like to delete?\n")
            delete(cursor, id)
            

        elif choice == "exit":
            exit(connection)
            break


main()


# sources
# https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/ 
