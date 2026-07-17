import json
import re
import random

# A text based game
# CURRENT ISSUE: 
# need to cast input for stats in main method to int

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
		return (self.strength * 0.4) + (self.agility * 0.2) + (self.intel * 0.1)
	
	# default dodge
	""" I will use this based out of 100, agility is the main stat and it will automatically be rolled upon enemy
	attack. i will use it like ' if enemy attacks, random out of 100, if this method returns greater than the random,
	dodge success. If within 10, take 50% damage instead"""
	def dodge(self):
		return ( self.agility * 2) + (self.strength * 0.3) + self.intel

	def heal(self):
		return (self.strength*0.2) + (self.agility * 0.4) + (self.intel*0.8)
		
# Why not
class Enemy(Hero): # I wonder if this will inherit everything from hero and add status
	def __init__(self, health, mana, strength, intel, agility, skillPoints=0, exp=0, name="John"):
		super().__init__(health, mana, strength, intel, agility, skillPoints, exp, name)
		self.defeated = False # is beaten?
	def dialogue(self):
		# defn change later, keep for testing and what not
		print("Hello :3 ! I am an evil person muahaha prepare to die\n")
	def enemyWinDialogue(self):
		print("You fall beneath my feet, once again i am the deliverer of death... \n")
		# maybe add a restart game button? Maybe a checkpoint using json save file?


# this is going to be my first boss
class Roman(Enemy):
	# Name: Discharged Praetorium
	def __init__(self):
		self.health = 37
		self.mana = 12
		self.strength = 10
		self.agility = 1

	# returns nothing, prints an introduction dialogue
	def introDialogue(self):
		print("*thud*...*thud*...*thud*...oh? someone stands infront of a retired general and wont move...")
		print("...so another barbarian thinks they will be the one to topple Rome...\n")
		print(" I've dealt with much worse than you, bring it on!\n")

	# Description below
	""" The roman's special will return the damage dealt,
	and the discoordination debuff to be subtracted from the players agility"""
	def special(self):
		rand = random.uniform(1,2)
		print("DP uses his special: Discharged Praetorium charges at you bashing and slicing you, reducing your coordination.\n")
		dmg = int(strength * 1.2 * rand)
		dc = int(strength * 1.4 * rand) # dc = discoordination debuff
		return dmg, dc
		# strength *1.2 + agility *2?

	# Returns nothing, prints out randomly 1 of 3 dialogue lines
	def randomDialogue():
		randint = random.randint(1,3)
		if randint == 1:
			print("I've had germanic girls put up more of a fight!\n")
		elif randint == 2:
			print("If I wanted to waste my time, I would debate Aristotle about the birds and the bees\n")
		elif randint == 3:
			print("You wouldn't even make for a good peasant!")

			
def main():
	print("\t\tAdventures in Abengarde\n")
	print("Welcome oh departed soul, lost one in need of flesh...\n")
	print("You died pre-emptively, and had to do a few more quests before departing...\n")
	print("Choose what flesh you will inhabit\n")
	print("Attributes\tstrength\tagility\tintelligence\n")
	print("Warror\t15\t\tX\t\tX\n")
	print("Bandit\tX\t\t15\t\tX\n")
	print("Wizard\tX\t\tX\t\t15\n")


	while True:
		choice = input("Choose your class: Warrior, Bandit, Wizard\n")
		choice = choice.lower()
		
		if choice in ["warrior", "bandit", "wizard"]:
			break
		else:
			print("Please enter a valid class")	
		

	# Player "customization"
	# Warriro selection
	if choice == "warrior":
		print("You chose to inhibit the Warrior, he naturally has 15 strength.")
		# if user decides to get 10000000 stats in a trait or something
		while True:
			firstStat = input("How many points of agility would you like out of 10: \n")
			if firstStat < 0 or firstStat > 10:
				print("Cannot be outside of the bounds you crafty one")
			else:
				break
		# same thing but for the second stat
		while True:
			secondStat = input("How many stats of Intelligence would you like out of" + 10-firstStat+ "\n")
			if secondStat < 0 or secondStat > 10-firstStat:
				print("Cannot be outside of the bounds you crafty one")
			else:
				break

	# bandit selction
	elif choice == "bandit":
		print("You chose to inhibit the Bandit, he naturally has 15 agility.")
		# if user decides to get 10000000 stats in a trait or something
		while True:
			firstStat = input("How many points of strength would you like out of 10: \n")
			if firstStat < 0 or firstStat > 10:
				print("Cannot be outside of the bounds you crafty one")
			else:
				break
		# same thing but for the second stat
		while True:
			secondStat = input("How many stats of Intelligence would you like out of" + 10-firstStat+ "\n")
			if secondStat < 0 or secondStat > 10-firstStat:
				print("Cannot be outside of the bounds you crafty one")
			else:
				break

	# Wizard selection
	elif choice == "wizard":
		print("You chose to inhibit the Wizard, he naturally has 15 intelligence.")
		# if user decides to get 10000000 stats in a trait or something
		while True:
			firstStat = input("How many points of strength would you like out of 10: \n")
			if firstStat < 0 or firstStat > 10:
				print("Cannot be outside of the bounds you crafty one")
			else:
				break
		# same thing but for the second stat
		while True:
			secondStat = input("How many stats of agility would you like out of" + 10-firstStat+ "\n")
			if secondStat < 0 or secondStat > 10-firstStat:
				print("Cannot be outside of the bounds you crafty one")
			else:
				break
