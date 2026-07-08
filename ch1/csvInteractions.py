import csv

# csv interactions and testing
# Elisey Voichishin

"""
multi line comments can be stored with a triple quotation marks
because it is going to be ignored by the interpretor if not assigned
very nice
"""

#CSV methods  / properties
"""
csv.field_size_limit = returns maximum field size
csv.get_dialect = get the dialect that is associated with the name
csv.list_dialects = show all registered dialects
csv.reaqder = data is read from a CSV file
csv.register_dialect = associated dialect with name
csv.writer = data is written to a CSV file
csv.unregister_dialect = associate dialect with name
csv.QUOTE_ALL = everything is quoted regardless of its type
csv.QUOTE_MINIMAL = fields with special characters are quoted
csv.QUOTE_NONNUMERIC = all fields without numbers are quoted
csv.QUOTE_NONE = nothing is quoted
"""

## READING A CSV FILE
#with open("file.csv", "rt") as f:
	#data = csv.reader(f)
	#for row in data:
		#print(row)

with open("output.csv", "w") as file: # if doesnt work do mode="w"
	writer = csv.writer(file, delimiter=',', quotechar='~', quoting=csv.QUOTE_MINIMAL)
# writing to a csv
	writer.writerow(["Programming language", "extension", "implemented"])
	writer.writerow(["Python",".py","1991"])
	writer.writerow(["java",".java","1995"])
	writer.writerow(["c++",".cpp","1983"])

# dont have to close file because we did the with open as file
# automatically closes upon finishing block
