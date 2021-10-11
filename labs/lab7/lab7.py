"""
Name: <Sydney Wertz>
<lab7>.py
"""

import math

def cash_conversion():
    whole_dollar = eval(input("Enter a dollar amount as an integer: "))
    print('{}{:.2f}'.format("$", whole_dollar))

def encode():
    normal_message = input("Enter the message you wish to be encoded: ")
    key = eval(input("Input the key for the code: "))
    acc = ""
    for i in normal_message:
        x = ord(i) + key
        new_char = chr(x)
        acc += new_char
    print(acc)

def sphere_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return round(surface_area, 3)

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return round(volume, 3)

def sum_n(n):
    acc = 0
    for i in range(1, n+1):
        acc += i
    return acc

def sum_n_cubes(n):
    acc_cube = 0
    for i in range(1, n+1):
        acc_cube += (i**3)
    return acc_cube

def encode_better():
    message = input("Enter the message you wish to encode: ")
    cipher = input("Enter the cipher message (should be equal or longer than message): ")
    acc = ""
    for i in range(len(message)):
        c = chr(ord(message[i]) + ord(cipher[i]) - 97)
        acc += c
    print(acc)

def main():
    cash_conversion()
    encode()
    print(sphere_area(7))
    print(sphere_volume(3))
    print(sum_n(4))
    print(sum_n_cubes(4))
    encode_better()
    pass

main()
