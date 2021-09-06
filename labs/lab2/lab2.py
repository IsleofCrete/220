"""
Name: <Sydney Wertz>
lab2.py

Problem: Arithmetic Lab
"""

import math

def sum_of_threes():
    up_bound = eval(input("Input upper bound (exclusive)")) #(does not include upper bound in calculation
    acc_1 = 0
    for i in range(0, up_bound, 3): #range value contains start (0), end (up_bound (not included)), and step(3)
       acc_1 += i
    print(acc_1)

def multiplication_table():
    for H in range (1, 11):
        print(H, ":", end = " ")
        for L in range(1, 11):
            print(H*L, end = " ")
        print()

def triangle_area():
    a = eval(input("Input a"))
    b = eval(input("Input b"))
    c = eval(input("Input c"))
    s = (a+b+c) / 2
    A = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    print(A)

def sumSquares():
    start = eval(input("Input start range"))
    end = eval(input("Input end range"))
    total = 0
    for j in range(start, end + 1):
        total += j*j
    print(total)

def power():
    base = eval(input("Input base value"))
    exponent = eval(input("Input exponent value"))
    exp_total = 1
    for k in range(exponent): #range starts at zero, but we don't need to include the last number (will run one too many times)
        exp_total *= base
    print(exp_total)

#sum_of_threes()
#multiplication_table()
#triangle_area()
#sumSquares()
#power()