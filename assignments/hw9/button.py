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

        return (door_llx <= user_x <= door_urx) and (door_ury <= user_y <= door_lly)

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
