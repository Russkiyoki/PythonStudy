# we can totally do multiple inheritances
class Flyer:

  def fly(self):

    print("Flying")

class Swimmer:

  def swim(self):

    print("Swimming")

class Duck(Flyer, Swimmer):

  pass


f = Flyer()
f.fly()

s = Swimmer()
s.swim()

d = Duck()
d.fly()
d.swim()
