"""
Name: <Sydney Wertz>
<lab5>.py
"""

from graphics import *
import math

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    pointA = win.getMouse()
    pointA.draw(win)
    pointB = win.getMouse()
    pointB.draw(win)
    pointC = win.getMouse()
    pointC.draw(win)

    usr_triangle = Polygon(pointA, pointB, pointC)
    usr_triangle.draw(win)

    aX = pointA.getX()
    aY = pointA.getY()
    bX = pointB.getX()
    bY = pointB.getY()
    cX = pointC.getX()
    cY = pointC.getY()

    abLength = math.sqrt(((aX-bX)**2) + ((aY-bY)**2))
    bcLength = math.sqrt(((bX-cX)**2) + ((bY-cY)**2))
    caLength = math.sqrt(((cX-aX)**2) + ((cY-aY)**2))
    perimeter = abLength + bcLength + caLength
    peri_pnt = Text(Point(200, 20), "The perimenter is: " + str(round(perimeter, 3)))
    peri_pnt.draw(win)

    s = (perimeter / 2)
    area = math.sqrt(s * ((s-abLength)*(s-bcLength)*(s-caLength)))
    area_pnt = Text(Point(200, 40), "The area is: " + str(round(area, 3)))
    area_pnt.draw(win)

    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 500
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255. Click window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(win_width/2 - 0, win_height/2 + 40), 5)
    red_entry.draw(win)

    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = Entry(Point(win_width/2 - 0, win_height/2 + 70), 5)
    green_entry.draw(win)

    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = Entry(Point(win_width/2 - 0, win_height/2 + 100), 5)
    blue_entry.draw(win)

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    win.getMouse()

    for i in range(0, 5):
        red_rgb = int(red_entry.getText())
        green_rgb = int(green_entry.getText())
        blue_rgb = int(blue_entry.getText())
        color = color_rgb(red_rgb, blue_rgb, green_rgb)

        shape.setFill(color)
        win.getMouse()

    win.getMouse()
    win.close()

def process_string():
    usr_string = input("Input a string:")
    print("1:" + usr_string[0])
    print("2:" + usr_string[-1])
    print("3:" + usr_string[2:6])
    print("4:" + usr_string[0]+usr_string[-1])
    print("5:" + usr_string[0:3]*10)
    print("6:")
    for i in range(len(usr_string)):
        print(usr_string[i])
    print("7:" , len(usr_string))
    print()

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print("1: " + x)
    x = float(values[0]) + float(values[2])
    print("2:" , x)
    x = values[1] * 5
    print("3: " + x)
    x = [values[2], values[3], values[4]]
    print("4:" , x)
    x = [values[2], values[3], values[0]]
    print("5:" , x)
    x = [values[2], values[0], float(values[5])]
    print("6:" , x)
    x = float(values[2]) + float(values[0]) + float(values[5])
    print("7:" , x)
    x = len(values)
    print("8:" , x)

def another_series():
    loop_terms = eval(input("Input the number of times you would like the series to run:"))
    sum = 0
    for i in range(0, loop_terms):
        x = 2 + (2 * (i%3))
        sum = sum + x
        print(x, end=" ")
    print()
    print("The sum is:" , sum)

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    end_rad = win_width / 2
    begin_rad = end_rad / 5

    white_circle = Circle(Point(250, 250), end_rad)
    white_circle.setOutline("black")
    white_circle.draw(win)

    black_circle = Circle(Point(250, 250), begin_rad*4)
    black_circle.setFill("black")
    black_circle.draw(win)

    blue_circle = Circle(Point(250, 250), begin_rad*3)
    blue_circle.setFill("blue")
    blue_circle.draw(win)

    red_circle = Circle(Point(250, 250), begin_rad*2)
    red_circle.setFill("red")
    red_circle.draw(win)

    yellow_circle = Circle(Point(250, 250), begin_rad)
    yellow_circle.setFill("yellow")
    yellow_circle.draw(win)

    win.getMouse()
    win.close()

def main():
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    target()
    pass

main()
