"""
Name: <Sydney Wertz>
<lab8>.py
"""

from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+") #creates file if doesn't exist
    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(i) + " " + word + "\n")
            i += 1
    in_file.close()
    out_file.close()

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    for line in in_file:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = wage * int(parts[3])
        out_file.write(parts[0] + " " + parts[1] + " " + str(wage) + "\n")
    in_file.close()
    out_file.close()

def calc_check_sum(isbn):
    isbn_index = 0
    sum = 0
    for i in range(10, 0, -1):
        sum = sum + (int(isbn[isbn_index]) * i)
        isbn_index += 1
    return sum

def send_message(file, friend):
    in_file = open(file, "r")
    out_file = open(friend + ".txt", "w+")

    for line in in_file:
        out_file.write(line)

    in_file.close()
    out_file.close()

def send_safe_message(file, friend, key):
    in_file = open(file, "r")
    out_file = open(friend + ".txt", "w+")

    for line in in_file:
        out_file.write(encode(line, key))

    in_file.close()
    out_file.close()

def send_uncrackable_message(file, friend, pad):
    in_file = open(file, "r")
    out_file = open(friend + ".txt", "w+")
    pad_file = open(pad, "r")
    pad_key = pad_file.read()

    for line in in_file:
        out_file.write(encode_better(line, pad_key))

    in_file.close()
    out_file.close()
    pad_file.close()

def main():
    number_words("Walrus.txt", "W_out.txt")
    hourly_wages("hourly_wages.txt", "hourly_out.txt")
    send_message("message.txt", "Sydney")
    send_safe_message("secret_message.txt", "Red", 3)
    send_uncrackable_message("safest_message.txt", "Blue", "pad.txt")
    calc_check_sum("0072946520")
    pass

main()
