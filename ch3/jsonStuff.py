# json.load() : reads json data from a file and converts into a python object
# json.dump() : takes python obj and writes its json rep to a file
# the s at the end below stands for STRING
# json.loads(): parses a json-formatteed string and converts to a python object
# json.dumps(): takes a python obj and returns its json representation as a pythong string

import json

try: 
	with open('data.json', 'r') as file:
		python_data = json.load(file)
# load() reads the file handle and parses json data
# python_data is a python dictionary
		print("Success loading JSON data into a python obj: ")
	#	print(python_data) 
# should print everything ^
		print("Name: " + python_data['name'])
		print(f"Version: {python_data['version']}")
		print(f"items list: {python_data['items']}")
		print(f"Type of loaded data: {type(python_data)}")
		
	print("File opened and automatically closed")

except FileNotFoundError:
	print("Blin couldnt find the file")

except Exception as e:
	print("an error occured:" + e)
