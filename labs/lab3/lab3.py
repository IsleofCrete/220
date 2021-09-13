"""
Name: <Sydney Wertz>
lab3.py

Problem: Arithmetic, Loops
"""

def average():
    num_grades = eval(input("Input the number of grades you will be averaging"))
    total = 0
    for i in range(1, num_grades+1):
        grade = eval(input("Enter grade received on HW" + str(i)))
        total = total + grade
    tot_avg = total / num_grades
    print("The average of your grades is:", tot_avg)

def tip_jar():
    tip_tot = 0
    for i in range(1, 6): #five people
        tip_amt = eval(input("Person " + str(i) + ", input tip amount put into the jar:"))
        tip_tot = tip_tot + tip_amt
    print("The total amount in the tip jar is: $", tip_tot)

def newton():
    x = eval(input("What number would you like to find the square root of?"))
    refine = eval(input("How many times would you like to refine this equation?"))
    approx = x / 2
    for i in range(1, refine+1):
        approx = (approx+ (x/approx)) / 2
    print("The final approximation value is:", approx)

def sequence():
    x = eval(input("Give the number of the terms in this series"))
    for i in range(1, x+1):
        y = 1 + ((i//2) * 2)
        print(y, end = " ")

def pi():
    n = eval(input("Input the number of desired terms for the Wallis Formula"))
    tot = 1
    for i in range(0, n):
        numerator = 2 + (i // 2 * 2)
        denominator = 1 + ((i + 1) // 2 * 2)
        frac = numerator / denominator
        tot = tot * frac
    print("pi / 2 =", tot)

#average()
#tip_jar()
#newton()
#sequence()
#pi()