#modifying json files

import json

try: 
	with open('inventory.json', 'r') as file:
		inventory_data = json.load(file)

	print("Loaded existing inventory:", inventory_data)

	
except ( FileNotFoundError, json.JSONDecodeError) as e:
	print(f"Error reading file: {e}")
	inventory_data = {} # start empty if error


if inventory_data is not None:
	inventory_data['apples'] = 15 # update value
	inventory_data['banana'] = 5 #adding a new key-pair value
	print("Modified inventory in python:", inventory_data)
else:
	print("Couldnt update data, failure to load")


#writing the modified object back via json.dump()

if inventory_data is not None:
	try:
		with open('inventory.json', 'w') as file:
			json.dump(inventory_data, file, indent=4)
		print("Updated!")
	
	except Exception as e:
		print(f"Failure: {e}")

