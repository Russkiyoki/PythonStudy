# Elisey Voichishin CS113 Study.com 
# A simple text-based adventure game

import re
import json
import random

from matplotlib.pylab import choice

# global list for decisions
decisions = []


# Item object will be equipped to hero to modify stats
# create random objects up to 5 later
class Item():
	def __init__(self, health, mana, strength, agility, intel):
		self.health = health
		self.mana = mana
		self.strength = strength
		self.agility = agility
		self.intel = intel # Intelligence stat	
	
# Base class in which the other hero-type-classes will inherit from
class Hero:
	# initialization 
	""" Im thinking for stats apart from mana and health, they shouldn't exceed 25.
	that way math doesnt get too crazy and it will be easy to understand"""

	""" Skill points will be used to figuring out what the user wants to be their 2nd main stat.
	Basically, based off of what class they choose, 15 points automatically go to that class, 
	and then they get to choose how much for the other 2 traits. Ex:
	User picks Warrior. Strength = 15, "How many points for agility? {skillPoints} remaining:"..."""

	def __init__(self, health, mana, strength, intel, agility, skillPoints=0, exp =0, name="John"):
		self.health = health
		self.mana = mana
		self.strength = strength
		self.intel = intel # intelligence stat
		self.agility = agility
		self.skillPoints = skillPoints # default for 0 so i can use for enemies
		self.name = name
	
	# default attack will be strike, each child class will have their power
	# But I will also be adding other actions for the other classes to have their fun
	def strike(self):
		return (self.strength * 0.4) + (self.agility * 0.2) + (self.intel * 0.1) + random.randint(1, 100)
	
	# default dodge
	""" I will use this based out of 100, agility is the main stat and it will automatically be rolled upon enemy
	attack. i will use it like ' if enemy attacks, random out of 100, if this method returns greater than the random,
	dodge success. If within 10, take 50% damage instead"""
	def dodge(self):
		return ( self.agility * 2) + (self.strength * 0.3) + self.intel + random.randint(1, 100)

	def heal(self):
		return (self.strength*0.2) + (self.agility * 0.4) + (self.intel*0.8) + random.randint(1, 100)

	# method to create a player, to call the class itself and return player
	# found out about it through geeks4geeks
	@classmethod
	def createPlayer(cls, choice):
		if choice == "warrior":
			print("You chose to inhibit the Warrior, he naturally has 15 strength.")

			# if user decides to get 10000000 stats in a trait or something
			while True:
				firstStat = int(input("How many points of agility would you like out of 10: \n"))
				decisions.append(firstStat) # save even if stupid response
				if firstStat < 0 or firstStat > 10:
					print("Cannot be outside of the bounds you crafty one")
				else:
					break

			# same thing but for the second stat
			while True:
				secondStat = int(input("How many stats of Intelligence would you like out of " + str(10-firstStat) + ":\n"))
				decisions.append(secondStat) # save even if stupid response
				if secondStat < 0 or secondStat > 10-firstStat:
					print("Cannot be outside of the bounds you crafty one")
				else:
					break
			# name check
			while True:
				name = input("You awake, by what name will you go by this time?\n")
				decisions.append(name) # save even if stupid response
				if re.match("^[A-Za-z]*$", name):
					break
				else:
					print("Please enter a valid name, only letters are allowed")

			# actual return
			return Hero(health=35, mana=25, strength = 15, agility = firstStat, intel = secondStat, name=name)

		# bandit selction
		elif choice == "bandit":
			print("You chose to inhibit the Bandit, he naturally has 15 agility.")

			# if user decides to get 10000000 stats in a trait or something
			while True:
				firstStat = int(input("How many points of strength would you like out of 10: \n"))
				decisions.append(firstStat) # save even if stupid response
				if firstStat < 0 or firstStat > 10:
					print("Cannot be outside of the bounds you crafty one")
				else:
					break

			# same thing but for the second stat
			while True:
				secondStat = int(input("How many stats of Intelligence would you like out of " + str(10-firstStat) + ":\n"))
				decisions.append(secondStat) # save even if stupid response
				if secondStat < 0 or secondStat > 10-firstStat:
					print("Cannot be outside of the bounds you crafty one")
				else:
					break

			# Name check
			while True:
				name = input("You awake, by what name will you go by this time?\n")
				decisions.append(name) # save even if stupid response
				if re.match("^[A-Za-z]*$", name):
					break
				else:
					print("Please enter a valid name, only letters are allowed")

				# actual return
			return Hero(health=25, mana=25, strength = firstStat, agility = 15, intel = secondStat, name=name)

		# Wizard selection
		elif choice == "wizard":
			print("You chose to inhibit the Wizard, he naturally has 15 intelligence.")

			# if user decides to get 10000000 stats in a trait or something
			while True:
				firstStat = int(input("How many points of strength would you like out of 10: \n"))
				decisions.append(firstStat) # save even if stupid response
				if firstStat < 0 or firstStat > 10:
					print("Cannot be outside of the bounds you crafty one")
				else:
					break
			# same thing but for the second stat

			while True:
				secondStat = int(input("How many stats of agility would you like out of " + str(10-firstStat) + ":\n"))
				decisions.append(secondStat) # save even if stupid response
				if secondStat < 0 or secondStat > 10-firstStat:
					print("Cannot be outside of the bounds you crafty one")
				else:
					break

			# Name check
			while True:
				name = input("You awake, by what name will you go by this time?\n")
				decisions.append(name) # save even if stupid response
				if re.match("^[A-Za-z]*$", name):
					break
				else:
					print("Please enter a valid name, only letters are allowed")

			return Hero(health=25, mana=35, strength = firstStat, agility = secondStat, intel = 15, name=name)

class Enemy:
	def __init__(self, Hero):
		pass
		# idk what would go here tbh yet
	def dialogue():
		dial = {
			"taunt0" : "I've had germanic girls put up more of a fight!\n",
			"taunt1" : "If I wanted to waste my time, I would debate Aristotle about the birds and the bees.\n",
			"taunt2" : "You wouldn't even make for a good beggar...\n" ,
			"win" : "And so my blade claims another soul, rest in piss...\n",
			"death" : "agh-- all these years... i delivered souls over unto death without knowing her face, and now into her arms i go...\n"
		

def print_title():
	print("\t\tAdventures in Abengarde\n")
	print("Welcome oh departed soul, lost one in need of flesh...\n")
	print("You died pre-emptively, and had to do a few more quests before departing...\n")
	print("Choose what flesh you will inhabit\n")
	print("Attributes\tstrength\tagility\tintelligence\n")
	print("Warror\t15\t\tX\t\tX\n")
	print("Bandit\tX\t\t15\t\tX\n")
	print("Wizard\tX\t\tX\t\t15\n")

# create player function, that way my main() doesnt look wicked
def main():
	# my infinite loop for replayability
	while True:
		try:
			# my json stuff
			# check for previous save file, if it exists, load it and ask if they want to continue or start over
			with open('user_settings.json', 'r') as file:
				user_data = json.load(file)
				print(f"Welcome back {user_data['username']}! Your stats are as follows: \n")
				print(f"Health: {user_data['health']}")
				print(f"Mana: {user_data['mana']}")
				print(f"Strength: {user_data['strength']}")
				print(f"Agility: {user_data['agility']}")
				print(f"Intelligence: {user_data['intelligence']}")
				choice = input("Would you like to start over? (y/n): ")
				decisions.append(choice) # save even if stupid response
				if choice.lower() == "n":
					print("Continuing with your previous character...")
					player = Hero(user_data['health'], user_data['mana'], user_data['strength'], user_data['intelligence'], user_data['agility'], name=user_data['username'])
				else:
					print("Starting over...")
		except FileNotFoundError:
			pass # ignore whatever, just means no save file exists yet

		print_title()

		# input loop for valid entry
		while True:
			choice = input("Choose your class: Warrior, Bandit, Wizard\n")
			decisions.append(choice) # save even if stupid response
			choice = choice.lower()			

			if choice in ["warrior", "bandit", "wizard"]:
				player = Hero.createPlayer(choice)
				break
			else:
				print("Please enter a valid class!")


		# output for json stuff
		user_data = {
			"username": player.name,
			"health": player.health,
			"mana": player.mana,
			"strength": player.strength,
			"agility": player.agility,
			"intelligence": player.intel,
			"decisions": decisions
		}

		# try to open file without breaking the program
		try:
			# opening the file in write mode
			with open('user_settings.json', 'w') as file:
				# data will be written here using json.dump()
				# indent=4 makes the output be formatted nicely
				json.dump(user_data, file, indent=4)
		# print why did it fail?
		except Exception as e:
			print(f"An error occurred during file opening: {e}")


		# exit or replay loop
		while True:
			replay = input("Congratulations, you have freed us! Would you like to reincarnate? (y/n): ")
			decisions.append(replay) # save even if stupid response
			replay = replay.lower()
			if replay == "y":
				break
			elif replay == "n":
				print("Farewell traveler, thank you for defeating the evil that lurks in Abengarde!")
				return
			else:
				print("Please enter a valid option!")

main()


# sources
# https://medium.com/data-science/regular-expressions-using-the-re-module-to-extract-information-from-strings-3d0500e8db1c
# https://www.geeksforgeeks.org/python/classmethod-in-python/ 
# https://study.com/academy/lesson/json-files-in-python-opening-updating-and-saving.html
# https://www.w3schools.com/python/python_lists_add.asp
