"""
Name: <Sydney Wertz>
threeDoorGame.py

Problem: Homework 11/18/2021

Certificate of Authenticity
I certify that his assignment is entirely my own work
For Test:
Button is (1, 2) (3, 4)
X range = (1-3) Y range = (2-4)
"""
from button import Button
from random import choice
from graphics import *

def main():
    win = GraphWin("Three Button Game", 600, 300)

    upper_text = Text(Point(300, 75), "There is a secret door")
    upper_text.draw(win)
    lower_text = Text(Point(300, 275), "Click any door")
    lower_text.draw(win)

    door1_pt = Rectangle(Point(75, 175), Point(175, 130))
    text1 = "Door 1"
    door1 = Button(door1_pt, text1)
    door1.draw(win)

    door2_pt = Rectangle(Point(250, 175), Point(350, 130))
    text2 = "Door 2"
    door2 = Button(door2_pt, text2)
    door2.draw(win)

    door3_pt = Rectangle(Point(425, 175), Point(525, 130))
    text3 = "Door 3"
    door3 = Button(door3_pt, text3)
    door3.draw(win)

    secret_door = choice([1, 2, 3])

    lower_lose_text = "The secret door is Door {0}".format(secret_door)

    user_click = win.getMouse()

    door1_check = door1.is_clicked(user_click)
    door2_check = door2.is_clicked(user_click)
    door3_check = door3.is_clicked(user_click)

    if door1_check is True and secret_door == 1:
        door1.color_button("green")
        upper_text.setText("You win!")
        lower_text.setText("Click anywhere to close")
    elif door1_check is True and secret_door != 1:
        door1.color_button("red")
        upper_text.setText("You lose!")
        lower_text.setText(lower_lose_text)

    elif door2_check is True and secret_door == 2:
        door2.color_button("green")
        upper_text.setText("You win!")
        lower_text.setText("Click anywhere to close")
    elif door2_check is True and secret_door != 2:
        door2.color_button("red")
        upper_text.setText("You lose!")
        lower_text.setText(lower_lose_text)

    elif door3_check is True and secret_door == 3:
        door3.color_button("green")
        upper_text.setText("You win!")
        lower_text.setText("Click anywhere to close")
    elif door3_check is True and secret_door != 3:
        door3.color_button("red")
        upper_text.setText("You lose!")
        lower_text.setText(lower_lose_text)

    else:
        upper_text.setText("Please pick a door next time")
        lower_text.setText(lower_lose_text)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
