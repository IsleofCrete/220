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

def main():
    win = GraphWin("Bumper Circles", 350, 350)
    win.setBackground(color_rgb(211, 211, 211)) #light grey

    ball1 = Circle(Point(100, 100), 20)
    color1 = get_random_color()
    ball1.setFill(color1)
    ball1.draw(win)

    x1 = get_random(350)
    y1 = get_random(350)

    ball2 = Circle(Point(125, 125), 20)
    color2 = get_random_color()
    ball2.setFill(color2)
    #ball2.draw(win)

    x2 = get_random(350)
    y2 = get_random(350)

    timer = 0.05
    i = 0

    while timer < 50:
        v1 = hit_vertical(ball1, win)
        h1 = hit_horizontal(ball1, win)
        v2 = hit_vertical(ball2, win)
        h2 = hit_horizontal(ball2, win)

        while i < 1:
            if (hit_vertical(ball1, win) == False) and (hit_horizontal(ball1, win) == False):
                ball1.undraw()
                ball1.move(x1/10, y1/10)
                ball1.draw(win)
                ball2.undraw()
                ball2.move(x2/10, y2/10)
                ball2.draw(win)
                time.sleep(.1)
                timer += 0.05
            else:
                i+=1
                break

        if v1 == True:
            ball1.undraw()
            ball1.move(-x1/10, y1/10)
            ball1.draw(win)
            ball2.undraw()
            ball2.move(x2 / 10, y2 / 10)
            ball2.draw(win)
            time.sleep(.1)
            while v1 == False and h1 == False:
                ball1.undraw()
                ball1.move(-x1/10, y1/10)
                ball1.draw(win)
                ball2.undraw()
                ball2.move(x2 / 10, y2 / 10)
                ball2.draw(win)
                time.sleep(.1)
                timer += 0.05
                if v1 == True or h1 == True or v2 == True or h2 == True:
                    break
                break

        elif h1 == True:
            ball1.undraw()
            ball1.move(x1/10, -y1/10)
            ball1.draw(win)
            ball2.undraw()
            ball2.move(x2 / 10, y2 / 10)
            ball2.draw(win)
            time.sleep(.1)
            while v1 == False and h1 == False:
                ball1.undraw()
                ball1.move(x1/10, -y1/10)
                ball1.draw(win)
                ball2.undraw()
                ball2.move(x2 / 10, y2 / 10)
                ball2.draw(win)
                time.sleep(.1)
                timer += 0.05
                if v1 == True or h1 == True or v2 == True or h2 == True:
                    break
                break

        elif v2 == True:
            ball2.undraw()
            ball2.move(-x2/10, y2/10)
            ball2.draw(win)
            ball1.undraw()
            ball1.move(x2 / 10, y2 / 10)
            ball1.draw(win)
            time.sleep(.1)
            while v2 == False and h2 == False:
                ball2.undraw()
                ball2.move(-x2/10, y2/10)
                ball2.draw(win)
                ball1.undraw()
                ball1.move(x2 / 10, y2 / 10)
                ball1.draw(win)
                time.sleep(.1)
                timer += 0.05
                if v2 == True or h2 == True or v1 == True or h1 == True:
                    break
                break

        elif hit_horizontal(ball2, win) == True:
            ball2.undraw()
            ball2.move(x2/10, -y2/10)
            ball2.draw(win)
            ball1.undraw()
            ball1.move(x2 / 10, y2 / 10)
            ball1.draw(win)
            time.sleep(.1)
            while v2 == False and h2 == False:
                ball2.undraw()
                ball2.move(x2/10, -y2/10)
                ball2.draw(win)
                ball1.undraw()
                ball1.move(x2 / 10, y2 / 10)
                ball1.draw(win)
                time.sleep(.1)
                timer += 0.05
                if v2 == True or h2 == True or v1 == True or h1 == True:
                    break
                break

        elif did_collide(ball1, ball2) == True:
            ball1.undraw()
            ball1.move(-x1 / 10, -y1 / 10)
            ball1.draw(win)
            ball2.undraw()
            ball2.move(-x2 / 10, -y2 / 10)
            ball2.draw(win)
            time.sleep(.1)
            timer += 0.05
            if (v1 == True) or (h1 == True) or (v2 == True) or (h2 == True):
                break
            break

    win.getMouse()
    win.close()

def get_random(move_amount):
    move = randint(-(move_amount), (move_amount))
    return move

def did_collide(ball1, ball2):
    pointa1 = ball1.getP1()
    pointa2 = ball1.getP2()
    pxa1 = pointa1.getX()
    pya1 = pointa1.getY()
    pxa2 = pointa2.getX()
    pya2 = pointa2.getY()

    pointb1 = ball2.getP1()
    pointb2 = ball2.getP2()
    pxb1 = pointb1.getX()
    pyb1 = pointb1.getY()
    pxb2 = pointb2.getX()
    pyb2 = pointb2.getY()

    if (pointa1 == pointb1) or (pointa1 == pointb2) or (pointa2 == pointb1) or (pointa2 == pointb2):
        return True
    else:
        return False

def hit_vertical(ball, win):
    point1 = ball.getP1()
    point2 = ball.getP2()
    px1 = point1.getX()
    py1 = point1.getY()
    px2 = point2.getX()
    py2 = point2.getY()
    if px1 >= 350 or px1 <= 0 or px2 >= 350 or px2 <= 0:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    point1 = ball.getP1()
    point2 = ball.getP2()
    px1 = point1.getX()
    py1 = point1.getY()
    px2 = point2.getX()
    py2 = point2.getY()
    if py1 >= 350 or py1 <= 0 or py2 >= 350 or py2 <= 0:
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
