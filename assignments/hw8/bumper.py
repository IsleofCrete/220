"""
Name: <Sydney Wertz>
bumper.py

Problem: Homework 11/4/2021

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""

from graphics import *
from random import randint
import time
from math import sqrt

def main():
    win = GraphWin("Bumper Circles", 350, 350)
    win.setBackground(color_rgb(211, 211, 211)) #light grey

    ball1 = Circle(Point(100, 100), 20)
    color1 = get_random_color()
    ball1.setFill(color1)
    ball1.draw(win)

    x1 = get_random(30)
    y1 = get_random(30)

    ball2 = Circle(Point(150, 150), 20)
    color2 = get_random_color()
    ball2.setFill(color2)
    ball2.draw(win)

    x2 = get_random(30)
    y2 = get_random(30)

    timer = 0.05

    while timer < 50:

        ball1.move(x1, y1)
        ball2.move(x2, y2)
        time.sleep(.05)
        timer += 0.05

        v1 = hit_vertical(ball1, win)
        h1 = hit_horizontal(ball1, win)

        v2 = hit_vertical(ball2, win)
        h2 = hit_horizontal(ball2, win)

        if v1 == True:
            x1 = -x1

            timer += 0.05

        elif h1 == True:
            y1 = -y1

            timer += 0.05

        elif v2 == True:
            x2 = -x2

            timer += 0.05

        elif h2 == True:
            y2 = -y2

            timer += 0.05

        elif did_collide(ball1, ball2) == True:
            x1 = -x1
            y1 = -y1
            x2 = -x2
            y2 = -y2

            timer += 0.05

    win.getMouse()
    win.close()

def get_random(move_amount):
    move = randint(-(move_amount), (move_amount))
    return move

def did_collide(ball1, ball2):
    rad1 = ball1.getRadius()
    x1 = ball1.getCenter().getX()
    y1 = ball1.getCenter().getY()

    rad2 = ball2.getRadius()
    x2 = ball2.getCenter().getX()
    y2 = ball2.getCenter().getY()

    tot_radius = rad1 + rad2

    distance = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    if distance <= tot_radius:
        return True
    else:
        return False

def hit_vertical(ball, win):
    win_width = win.getWidth()

    point1 = ball.getP1()
    point2 = ball.getP2()
    px1 = point1.getX()
    py1 = point1.getY()
    px2 = point2.getX()
    py2 = point2.getY()
    if px1 >= win_width or px1 <= 0 or px2 >= win_width or px2 <= 0:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    win_width = win.getWidth()

    point1 = ball.getP1()
    point2 = ball.getP2()
    px1 = point1.getX()
    py1 = point1.getY()
    px2 = point2.getX()
    py2 = point2.getY()
    if py1 >= win_width or py1 <= 0 or py2 >= win_width or py2 <= 0:
        return True
    else:
        return False

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rand_color = color_rgb(red, green, blue)
    return rand_color

if __name__ == '__main__':
    main()
