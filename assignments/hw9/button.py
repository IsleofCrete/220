from graphics import *

class Button:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = text

    # Am I supposed to use this function in the door game? I have made it but I don't see how this would function in the door game
    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self, shape, text):
        self.shape.undraw()
        self.text.undraw()

    #can I keep the door as a parameter so it can check for each door
    #also, how to I pass in the point in this function if it is not an instance variable
    def is_clicked(self, user_click, shape):
        self.shape = shape
        self.user_click = user_click

        self.userX = self.user_click.getX()
        self.userY = self.user_click.getY()

        self.door_lower_left = self.shape.getP1()
        self.door_llx = self.door_lower_left.getX()
        seflf.door_lly = self.door_lower_left.getY()

        self.door_upper_right = self.shape.getP2()
        self.door_urx = self.door_upper_right.getX()
        self.door_ury = self.door_upper_right.getY()

        if self.userX < self.door_urx and self.userX > self.door_llx and self.userY < self.door_lly and self.userY > self.door_ury:
            return True
        else:
            return False

    def color_button(self, color):
        self.color = color
        self.shape.setFill(color)

    # also, do I need to use this at all? I do not update the text inside the button itself ever and this function only updates the button text
    def set_label(self, label):
        self.text.setText(label)
