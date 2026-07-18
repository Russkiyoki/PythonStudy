# we are going to do some api stuff with the xml data and what not
import xml.sax
# Create a class for the movie handler
# pass in the content handler from SAX

class MovieHandler(sml.sax.ContentHandler):
	def __init__(self):
		self.CurrentData =""
		self.type = ""
		self.format = ""
		self.year = ""
		self.rating = ""
		self.stars = ""
		self.description = ""
	
	# Function to get called when an element starts
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "movie":
			print("\n")
			print("*****Movie Database*****")
			print("\n")
			title = attribute["attribute"]
			print("Movie Title:", title)

	def endElement(self, tag):
		if self.CurrentData == "type":
			print("Genre:", self.type)
		elif self.CurrentData == "format":
			print("Format:", self.format)
		elif self.CurrentData == "year":
			print("Year:", self.year)
		elif self.CurrentData == "rating":
			print("Rating:", self.rating)
# more to be done, lunch is about to finish :(
