"""
Name: <Sydney Wertz>
greeting.py

Problem: Greeting card Homework 5

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""

import time
from graphics import GraphWin, Line, Circle, Polygon, Point, Text, color_rgb

def main():
    window = GraphWin("Valentine's Day Card", 500, 500)
    window.setCoords(0, 0, 10, 10)
    window.setBackground(color_rgb(204, 204, 255)) #makes the background periwinkle

    arrow = Line(Point(1, 9), Point(9, 2.5))
    arrow.setWidth(5)
    arrow.setArrow("first")
    arrow.setOutline("purple")

    #heart
    circle1 = Circle(Point(6.6, 7), 2.127)
    circle1.setFill("pink")
    circle1.setOutline("pink")
    circle1.draw(window)

    circle2 = Circle(Point(3.4, 7), 2.127)
    circle2.setFill("pink")
    circle2.setOutline("pink")
    circle2.draw(window)

    triangle = Polygon(Point(1.55, 6), Point(5, 1.8), Point(8.45, 6))
    triangle.draw(window)
    triangle.setFill("pink")
    triangle.setOutline("pink")

    hvd_message = Text(Point(5, 6.5), "Happy Valentine's Day <3")
    hvd_message.setFace("arial")
    hvd_message.setSize(15)
    hvd_message.draw(window)

    time.sleep(2.5)
    hvd_message.undraw()
    arrow.draw(window)

    #arrow animation
    arrow.move(9, -9)
    for i in range(9):
        arrow.move(-1, 1)
        arrow.undraw()
        arrow.draw(window)
        time.sleep(0.1)
        i += 1

    #putting the heart and message back on top of the arrow
    circle1.undraw()
    circle2.undraw()
    triangle.undraw()
    circle1.draw(window)
    circle2.draw(window)
    triangle.draw(window)
    hvd_message.draw(window)

    #resting the program before the close message appears
    time.sleep(0.5)

    close_message = Text(Point(5, .5), "Click anywhere to close")
    close_message.draw(window)

    window.getMouse()

if __name__ == '__main__':
    main()
