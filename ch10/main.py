# we are going to do some api stuff with the xml data and what not
import xml.sax
# Create a class for the movie handler
# pass in the content handler from SAX

class MovieHandler(xml.sax.ContentHandler):
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
			title = attributes["title"]
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
		elif self.CurrentData == "stars":
			print("Stars:", self.stars)
		elif self.CurrentData == "description":
			print("Description:", self.description)
		# no clue wtf the point of this is but whatever
		self.CurrentData = ""

	def characters(self, content):
		if self.CurrentData == "type":
			self.type = content
		elif self.CurrentData == "format":
			self.format = content
		elif self.CurrentData == "year":
			self.year = content
		elif self.CurrentData == "rating":
			self.rating = content
		elif self.CurrentData == "stars":
			self.stars = content
		elif self.CurrentData == "description":
			self.description = content

if (__name__=="__main__"):
	# creating an XMLReader
	parser = xml.sax.make_parser()
	# turn off namespaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

Handler = MovieHandler()
parser.setContentHandler(Handler)
parser.parse("movies.xml")
