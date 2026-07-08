import random

def randint():
	return random.randint(1,100)

random_number = randint()

print("I have thought of a number between 1 and 100, can you guess it?")

while True:
	guess = int(input("Enter your guess: "))
	
	if guess == random_number:
		print("You win!")
		break
	difference = abs(random_number - guess)

	if difference > 10:
		print("Cold! More than 10 away")
	elif difference > 3:
		print("warm! more than 3 away!")
	else: # difference is <= 3 away
		print("Hot! less than or equal to 3 away!")
		
