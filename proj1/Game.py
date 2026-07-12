# Elisey Voichishin 
# Computer Science 113: Programming in Python 
# Project 1: Developing a python program

import json
import re

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

	def __init__(self, health, mana, strength, intel, agility, skillPoints=0, exp =0, name):
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
	def dialogue:
			print("Hello :3 ! I am an evil person muahaha prepare to die")
	def 

class Roman(Enemy):
	self.health = 37
	self.mana = 12
	self.strength = 10
	self.agility = 1

	
