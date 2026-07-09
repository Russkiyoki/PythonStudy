#!/usr/bin/python3
# above is used to specify to the OS what interpreter to use for this file

from tkinter import * 

class SimpleGui:
	def __init__(self,master):
	# all widgets must be added here
		# main window itself
		self.master = master
		master.title('Simple Gui')
		master.geometry('400x300') # width x height

		# name label
		self.labelName = Label(master,text='Name')
		self.labelName.grid(row=1, column=1)

		# textbox 
		self.name = Entry(master)
		self.name.grid(row=1, column=2)

		# age label
		self.labelAge = Label(master, text='year of birth')
		self.labelAge.grid(row=2, column=1)

		# age textbox
		self.age = Entry(master)
		self.age.grid(row=2, column=2)

		# age calculation label
		self.ageCalc = Label(master,text='Age =')
		self.ageCalc.grid(row=3, column=1)


#main
master = Tk() #creates instance of gui
SimpleGui(master)
master.mainloop() #makes the graphics window stay up

