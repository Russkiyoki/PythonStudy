# using objects and delcaring and what not

class Car:
	def __init__(self, make, color):
		self.make = make
		self.color = color
	
	def whatMake(self):
		print(self.make)
	
	def stats(self):
		return f"{self.make} and it is {self.color}"

class Gavno(Car):
	def whatMake(self):
		print("Obviously bmw")
	def vroom(self):
		print("vroom vroom")

		

car1 = Car("acura", "black")
car2 = Gavno("bmw", "blue")
car3 = Car("toyota", "silver")

car1.whatMake()
car2.whatMake()
print(car2.stats())
print(car3.stats())


