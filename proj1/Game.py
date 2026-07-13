# Elisey Voichishin 
# Computer Science 113: Programming in Python 
# Project 1: Developing a python program

import json
import re
import random

# A text based game

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
class Enemy(Hero, status): # I wonder if this will inherit everything from hero and add status
    def dialogue(self):
        # defn change later, keep for testing and what not
		print("Hello :3 ! I am an evil person muahaha prepare to die\n")
    def enemyWinDialogue(self):
        print("You fall beneath my feet, once again i am the deliverer of death... \n")
        # maybe add a restart game button? Maybe a checkpoint using json save file?


# this is going to be my first boss
class Roman(Enemy):
    # Name: Discharged Praetorium
	self.health = 37
	self.mana = 12
	self.strength = 10
	self.agility = 1

    # returns nothing, prints an introduction dialogue
    def introDialogue(self):
        print("*thud*...*thud*...*thud*...oh? someone stands infront of a retired general and wont move...")
        print("...so another barbarian thinks they will be the one to topple Rome...\n"
        print(" I've dealt with much worse than you, bring it on!\n")

    # Description below
    """ The roman's special will return the damage dealt,
    and the discoordination debuff to be subtracted from the players agility"""
    def special(self):
        rand = random.uniform(1,2)
        print("DP uses his special: Discharged Praetorium charges at you bashing and slicing you, reducing your coordination.\n"
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
    print("Warror\t15\tX\tX\n")
    print("Bandit\tX\t15\tX\n")
    print("Wizard\tX\tX\t15\n")

    choice = input.toLowerCase()
    print(choice)

main()
