from graphics import *

class Button:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = text

    def get_label(self):
        return self.text

    def draw(self, win):
        self.shape = shape
        shape.draw(win)

    def undraw(self, shape, text):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, user_click, door):
        self.shape = door

        userX = user_click.getX()
        userY = user_click.getY()

        door_lower_left = door.getP1()
        door_llx = door_lower_left.getX()
        door_lly = door_lower_left.getY()

        door_upper_right = door.getP2()
        door_urx = door_upper_right.getX()
        door_ury = door_upper_right.getY()

        if userX < door_urx and userX > door_llx and userY < door_lly and userY > door_ury:
            return True
        else:
            return False

    def color_button(self, color):
        self.color = color_rgb(color)

    def set_label(self, label):
        self.text.setText(label)
