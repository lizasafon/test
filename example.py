import graphics
from graphics import *

win = GraphWin("Test1", 300, 300)	#create window of size 300x300


c = Circle(Point(50, 50), 50)		#create object c - circle with center in (50, 50) and radius 50
c.setFill("#e0474c")	#set color of c '#e0474c'
l = Line(Point(2,4), Point(100, 100))	#create l - line that starts in (2,4) and ends in (100, 100)
l.setWidth(10)	#set width of line 10
r = Rectangle(Point(200, 10), Point(250, 40))	#create object r - rectangle with left high angle at (200, 10) and right low angle at (250,40)
o = Oval(Point(100, 100), Point(250, 210))	#create o - oval
o.setFill("yellow")	#set color of oval as yellow
o.setOutline("blue")	#set borders of oval as blue
p = Polygon(Point(50,50), Point(100,120), Point(100,180),
			Point(80, 200))	#create p - polygon with points at (50,50), (100,120), (100,180), (80,200)
p1 = p.clone()	#copy polygon 'p' to 'p1'
p.move(100, 50)	#move polygon 'p' to coordinates (100,50)
t = Text(Point(150, 150), "lala")	#create object t - text at coordinates (150,150) and content "lala"


# To draw all above on your window type name of the object and '.draw(win)'. The objects will appear in order you've typed them.
r.draw(win)
c.draw(win)
l.draw(win)
o.draw(win)
p.draw(win)
p1.draw(win)
t.draw(win)
print('change')
# Use this and window will close only when you click with your mouse on it
win.getMouse()
win.close()
