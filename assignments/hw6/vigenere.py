"""
Name: <Sydney Wertz>
vigenere.py

Problem: Vigenere Homework 6

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""

from graphics import *

def code(message, keyword):
    new_message = message.upper()
    new_message = new_message.replace(" ", "") #removes spaces
    new_message_list = list(new_message) #turning the combined and uppercase string into a list of letters

    new_keyword = keyword.upper()
    new_keyword = new_keyword.replace(" ", "")
    new_keyword_list = list(new_keyword)

    total_keyword_reps = len(new_message) // len(new_keyword)
    tot_keyword_remain = len(new_message) % len(new_keyword)
    #creating the proper length keyword list according to message length
    x = (new_keyword_list * total_keyword_reps)
    y = x + new_keyword_list[0:tot_keyword_remain]

    encoded_message = ""

    for i in range(0, len(new_message_list)):
        ord_mess = ord(new_message_list[i])
        ord_key = ord(y[i])
        new_ord = (ord_mess + ord_key) - 65
        if new_ord > 90:
            new_ord = new_ord - 26
        encoded_message = encoded_message + chr(new_ord)
    return encoded_message

def main():
    window = GraphWin("Vigenere", 650, 400)

    message_text = Text(Point(150, 75), "Message to code")
    message_text.draw(window)
    message_entry = Entry(Point(350, 75), 25)
    message_entry.draw(window)

    keyword_text = Text(Point(150, 150), "Enter Keyword")
    keyword_text.draw(window)
    keyword_entry = Entry(Point(350, 150), 25)
    keyword_entry.draw(window)

    encode = Text(Point(325, 250), "Encode it")
    encode.draw(window)
    encode_rect = Rectangle(Point(275, 230), Point(375, 270))
    encode_rect.draw(window)

    window.getMouse()

    encode.undraw()
    encode_rect.undraw()

    message_str = message_entry.getText()
    keyword_str = keyword_entry.getText()

    final_message = code(message_str, keyword_str)

    result_message = Text(Point(325, 250), "Resulting Message")
    result_message.draw(window)

    output_message = Text(Point(325, 275), final_message)
    output_message.draw(window)

    close_message = Text(Point(325, 375), "Click Anywhere to Close Window")
    close_message.draw(window)

    window.getMouse()

if __name__ == '__main__':
    main()
