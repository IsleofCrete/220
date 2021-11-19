"""
Name: <Sydney Wertz>
button.py

Problem: Homework 11/18/2021

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""
from graphics import Text

class Button:
    """
    Class creating a button, with the shape (rectangle) and button text(Text)
    """

    def __init__(self, shape, text):
        self.shape = shape
        self.text = Text(shape.getCenter(), text)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, user_click):

        user_x = user_click.getX()
        user_y = user_click.getY()

        door_lower_left = self.shape.getP1()
        door_llx = door_lower_left.getX()
        door_lly = door_lower_left.getY()

        door_upper_right = self.shape.getP2()
        door_urx = door_upper_right.getX()
        door_ury = door_upper_right.getY()

        x_max = 0
        x_min = 0

        y_max = 0
        y_min = 0

        if door_urx > door_llx:
            x_max = door_urx
            x_min = door_llx
        else:
            x_max = door_llx
            x_min = door_urx

        if door_ury > door_lly:
            y_max = door_ury
            y_min = door_lly
        else:
            y_max = door_lly
            y_min = door_ury

        return (x_min <= user_x <= x_max) and (y_min <= user_y <= y_max)

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
