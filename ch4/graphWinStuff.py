# had to install https://mcsp.wartburg.edu/zelle/python/graphics.py
# and then I put it into /usr/local/lib/python3.13/dist-packages/
 
from graphics import *

def main():
	win = GraphWin('My Graphics', 250, 250) # specifies size
	win.setBackground('purple')

	#g = Point(125,125) # to make a single point
	g = Circle(Point(125,125),50) 
	g.setFill('Red')
	g.setOutline('Green')
	g.draw(win) # draws to the graphics window

	# can use .getCenter() to return center of obj of x*y location

	o = Oval(Point(80,100), Point(150,150))
	o.draw(win)

	l = Line(Point(80,100), Point(150,150))
	l.setArrow('last')
	l.draw(win)

	t = Text(Point(40,40), "Henlo!")
	t.setText('Other Message now')
	t.setSize(18)
	t.setStyle('bold')
	t.draw(win)


	win.getMouse()
	win.close()

main()

