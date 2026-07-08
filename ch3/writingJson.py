import json

# My data i want to export to json
user_data = {
	"username": "py_dev",
	"theme": "dark",
	"notifications": {
		"email": True,
		"sms": False,
	},
#can alternatively be written as "notifications": {"email": True, "sms": False},
	"projects": ["Project A", "Project B"]
}

try:
	#opening the file in write mode
	with open('user_settings.json', 'w') as file:
		#data will be wwritten here using json.dump()
		#indent=4 makes the output be formatted nicely
		json.dump(user_data, file, indent=4)
	
	print("File opened for writing and automatically closed")

except Exception as e:
	print(f"An errror occurred during file opening: {f}")
	
