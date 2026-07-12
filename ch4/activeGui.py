#!/usr/bin/python3

from tkinter import *
# something doesnt work
class SimpleGraphics:
	def __init__(self,root, canvas):
		# add graphics stuff in here

		self.leftPoint = None
		self.rightPoint = None
		self.mouseClick = None 

		self.root = root
		self.canvas = canvas
		root.title("My Graphics")

		canvas.bind("<Button-1>", self.handleClick) # binding left click of the mouse to method
		canvas.pack() #sets default placement

		root.bind("<Key>", self.drawText) # keyboard

	def handleClick(self, event):
		# set the text position on every left click
		self.mouseClick = event
		# then also draw a rectangle
		self.drawRectangle(event)

	def drawText(self,event):
		if self.mouseClick is not None:
			self.canvas.create_text(self.mouseClick.x, self.mouseClick.y, text = event.keysym)
			self.mouseClick.x += 6 # move over where next letter is drawn
		else:
			#default case
			self.canvas.create_text(100,100, text=event.keysym)

	def drawRectangle(self, event):
		if self.leftPoint is None: #no value so we will assign it
			self.leftPoint = event
		elif self.rightPoint is None: 
			self.rightPoint = event
		if self.leftPoint != None and self.rightPoint != None: # both have points
			self.canvas.create_rectangle(
				self.leftPoint.x, self.leftPoint.y,
				 self.rightPoint.x, self.rightPoint.y,
				 outline="black"
			)
			# reset for next rectangle
			self.leftPoint = None
			self.rightPoint = None
#create rectangle

root = Tk()
canvas = Canvas(root)
SimpleGraphics(root, canvas)

root.mainloop()
