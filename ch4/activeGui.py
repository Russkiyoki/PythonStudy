#!/usr/bin/python3

from tkinter import *
# something doesnt work
class SimpleGraphics:
	def __init__(self,root, canvas):
		# add graphics stuff in here

		self.leftPoint = None
		self.rightPoint = None

		self.root = root
		self.canvas = canvas
		root.title("My Graphics")

		canvas.bind("<Button-1>", self.drawRectangle) # binding left click of the mouse to method
		canvas.pack() #sets default placement

		root.bind("<Any KeyPress>", lambda event: self.drawText(event.keysym)) # keyboard

	def clicked(self, event):
		if self.mouseClick is None:
			self.mouseClick = event
	
	def drawText(self,key):
		if self.mouseClick is not None:
			canvas.create_text(self.mouseClick.x, self.mouseClick.y, text = key)
			self.mouseClick.x += 6 # move over where next letter is drawn

	def drawRectangle(self, event):
		if self.leftPoint is None: #no value so we will assign it
			self.leftPoint = event
		elif self.rightPoint is None: 
			self.rightPoint = event
		if self.leftPoint != None and self.rightPoint != None: # both have points
			canvas.create_rectangle(self.leftPoint.x, self.leftPoint.y, self.rightPoint.x, self.rightPoint.y)
#create rectangle

root = Tk()
canvas = Canvas(root)
SimpleGraphics(root, canvas)

root.mainloop()
