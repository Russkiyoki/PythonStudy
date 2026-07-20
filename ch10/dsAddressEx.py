# THIS EXAMPLE IS NOT MY WORK, AND IS TO BE USED FOR NOTES
import sqlite3

class MiniAddressBook:
	def __init__(self, db_name="miniAddressBook.db"):
		self.conn = sqlite3.connect(db_name)
		self.cursor = self.conn.cursor()

		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS addressBookTable (
				name TEXT PRIMARY KEY,
				phone TEXT NOT NULL,
				email TEXT,
				address TEXT
			)
		""")
		self.conn.commit()
		print("Mini Address Book Database and Table Created.")

	def addContact(self, name, phone, email=None, address=None):
		try:
			self.cursor.execute(
				"INSERT INTO addressBookTable (name, phone, email, address) VALUES (?, ?, ?, ?)",
				(name, phone, email, address)
			)
			self.conn.commit()
			print(f"Contact '{name}' added successfully.")
		except sqlite3.Error as e:
			print(f"Error adding contact: {e}")

	def viewContacts(self):
		self.cursor.execute("SELECT * FROM addressBookTable")
		contacts = self.cursor.fetchall()

		if contacts:
			print("\n******** Mini Address Book ********")
			for contact in contacts:
				print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2] or 'N/A'}, Address: {contact[3] or 'N/A'}")
			print("****************************************")
		else:
			print("Mini Address Book- No Contacts to Display.")

	def updateContact(self, contactName, name=None, phone=None, email=None, address=None):
		update_fields = []
		update_values = []

		if name is not None:
			update_fields.append("name = ?")
			update_values.append(name)
		if phone is not None:
			update_fields.append("phone = ?")
			update_values.append(phone)
		if email is not None:
			update_fields.append("email = ?")
			update_values.append(email)
		if address is not None:
			update_fields.append("address = ?")
			update_values.append(address)

		if not update_fields:
			print("No fields to update.")
			return

		query = f"UPDATE addressBookTable SET {', '.join(update_fields)} WHERE name = ?"
		update_values.append(contactName)

		try:
			self.cursor.execute(query, update_values)
			self.conn.commit()

			if self.cursor.rowcount > 0:
				print(f"Contact with name {contactName} updated successfully.")
			else:
				print(f"Contact with name {contactName} not found.")
		except sqlite3.Error as e:
			print(f"Error updating contact: {e}")

	def deleteContact(self, contactName):
		try:
			self.cursor.execute("DELETE FROM addressBookTable WHERE name = ?", (contactName,))
			self.conn.commit()

			if self.cursor.rowcount > 0:
				print(f"Contact with name {contactName} deleted successfully.")
			else:
				print(f"Contact with name {contactName} not found.")
		except sqlite3.Error as e:
			print(f"Error deleting contact: {e}")

	def closeConnection(self):
		self.conn.close()

if __name__ == "__main__":
	addressBook = MiniAddressBook()

	while True:
		print("\nWelcome to the Mini Address Book!!")
		print("\nChoose an action:")
		print("1. Add Contact")
		print("2. View Contacts")
		print("3. Update Contact")
		print("4. Delete Contact")
		print("5. Exit")

		choice = input("Enter your choice: ")

		if choice == '1':
			name = input("Enter name: ")
			phone = input("Enter phone: ")
			email = input("Enter email (optional): ")
			address = input("Enter address (optional): ")
			addressBook.addContact(name, phone, email, address)

		elif choice == '2':
			addressBook.viewContacts()

		elif choice == '3':
			contactName = input("Enter the name of the contact to update: ")
			name = input("Enter new name (leave blank to keep current): ") or None
			phone = input("Enter new phone (leave blank to keep current): ") or None
			email = input("Enter new email (leave blank to keep current): ") or None
			address = input("Enter new address (leave blank to keep current): ") or None
			addressBook.updateContact(contactName, name, phone, email, address)

		elif choice == '4':
			contactName = input("Enter the name of the contact to update: ")
			addressBook.deleteContact(contactName)

		elif choice == '5':
			addressBook.closeConnection()
			print("Exiting Mini Address Book....")
			break

		else:
			print("Invalid choice. Please try again.")
