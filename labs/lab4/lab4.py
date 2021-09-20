"""
Name: <Sydney Wertz>
<lab4>.py
"""

from graphics import *
import math

def squares():
    width = 400
    height = 400
    win = GraphWin("Lab 4 Moving Squares", width, height)

    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add another square")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("black")
    shape.draw(win)

    for i in range(num_clicks):
        p = win.getMouse()

        dx = p.getX()
        dy = p.getY()
        square = Rectangle(Point(dx+10, dy+10), Point(dx-10, dy-10))
        square.setFill("blue")
        square.draw(win)

    instructions.setText("Click to close this window")
    win.getMouse()
    win.close()

def rectangles():
    window = GraphWin("Draw a rectangle", 400, 400)
    messageLoc = Point(200, 390)
    message = Text(messageLoc, "Click twice to create the corners of a rectangle")
    message.draw(window)

    point1 = window.getMouse()
    point1.draw(window)
    point2 = window.getMouse()
    point2.draw(window)

    rect = Rectangle(point1, point2)
    rect.setFill("purple")
    rect.draw(window)

    p1w = point1.getY()
    p1l = point1.getX()
    p2w = point2.getY()
    p2l = point2.getX()

    length = abs(p2l - p1l)
    width = abs(p2w - p1w)
    perimeter = 2 * (length + width)
    area = (length * width)
    area_pnt = Text(Point(200, 10), "The area is: " + str(round(area, 3)))
    area_pnt.draw(window)
    per_pnt = Text(Point(200, 30), "The perimeter is: " + str(round(perimeter, 3)))
    per_pnt.draw(window)

    message.setText("Click to close this window")
    window.getMouse()
    window.close()

def circles():
    windows = GraphWin("Draw a circle", 400, 400)
    messageLoc = Point(200, 390)
    message = Text(messageLoc, "Click twice to create the radius and center of a circle")
    message.draw(windows)

    center = windows.getMouse()
    center.draw(windows)
    ceX = center.getX()
    ceY = center.getY()
    circumference = windows.getMouse()
    circumference.draw(windows)
    ciX = circumference.getX()
    ciY = circumference.getY()

    radius_inner = ((ciX - ceX)**2 + (ciY-ceY)**2)
    radius_final = math.sqrt(radius_inner)
    radius = Text(Point(200, 10), "The radius is: " + str(round(radius_final, 3)))
    radius.draw(windows)
    circle = Circle(center, radius_final)
    circle.setFill("green")
    circle.draw(windows)

    message.setText("Click to close this window")
    windows.getMouse()
    windows.close()

def pi2():
    numerator = 4
    tot = 0
    terms = eval(input("Input the number of sequences desired to calculate pi:"))
    for i in range(0, terms):
        denom = 1 + 2*i
        fraction = (numerator/denom) * ((-1)**i)
        tot = tot + fraction
    print(tot)
    print(math.pi)

def main():
    squares()
    rectangles()
    circles()
    pi2()

main()
