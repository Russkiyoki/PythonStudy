# program to figure out how IO stuff works in python
# Elisey Voichishin
f = open("openMe.txt", 'r')

fileData = f.read() # reads entire file and prints as one string
print(fileData)
f.seek(0) #reset reader because reader is at the end of file

fileData = f.readline() # reads line by line
print(fileData)
f.seek(0) #reset reader

fileData = f.readlines() # reads line by line but also returns them as a list of strings
print(fileData)
f.close()


# output file
of = open("outputFile.txt" , "w")
of.write("whats up niggas\n")
of.write("Russ in this hoe\n")
of.write("Russ out this hoe straight up  \n")
of.close()


# another way to oopen file so that it would automatically close
with open('outputFile.txt', "w") as someFile:
	f.write("opened in the fancy way \n")
print("Yo python, did we close that file?: ", someFile.closed) # property closed not method 
