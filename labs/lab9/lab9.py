"""
Name: <Sydney Wertz>
<lab9>.py
"""

from graphics import *
import math

def addTen(nums):
    #print(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
    #print(nums)

def squareEach(nums):
    #print(nums)
    for i in range(len(nums)):
        nums[i] = round(nums[i] ** 2, 3)
    #print(nums)

def sumList(nums):
    #print(nums)
    sum = 0
    for i in range(len(nums)):
        sum += round(nums[i], 3)
        sum = round(sum, 3)
    #print(sum)
    return sum

def toNumbers(strList):
    #print(strList)
    for i in range(len(strList)):
        strList[i] = float(strList[i])
    #print(strList)

def writeSumOfSquares():
    file_in = input("Enter the in-file name: ")
    file_out = input("Enter the out-file name to be created: ")

    in_file = open(file_in + ".txt", "r")
    out_file = open(file_out + ".txt", "w+")

    for line in in_file:
        numList = line.split()
        toNumbers(numList)
        squareEach(numList)
        summation = sumList(numList)
        line_sum = round(summation, 3)

        out_file.write("Sum of squares = " + str(line_sum) + "\n")

    in_file.close()
    out_file.close()

def starter():
    weight = eval(input("Enter weight: "))
    numWins = eval(input("Enter wins: "))
    if (weight >= 150 and weight < 160) and (numWins >= 5):
        print("This individual is a starter")
    elif (weight > 199) or (numWins > 20):
        print("This individual is a starter")
    else:
        print("This individual is not a starter")

def leapYear(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year")
        return True
    else:
        print(year, "is not a leap year")
        return False

def circleOverLap():
    win = GraphWin("Circle", 400, 400)
    p1a = win.getMouse()
    p2a = win.getMouse()
    radius1 = math.sqrt((p1a.getX() - p2a.getX()) ** 2 + (p1a.getY() - p2a.getY()) ** 2)
    circle1 = Circle(p1a, radius1)
    circle1.draw(win)

    p1b = win.getMouse()
    p2b = win.getMouse()
    radius2 = math.sqrt((p1b.getX() - p2b.getX()) ** 2 + (p1b.getY() - p2b.getY()) ** 2)
    circle2 = Circle(p1b, radius2)
    circle2.draw(win)

    tot_radius = radius1 + radius2
    distance = math.sqrt((p1a.getX() - p1b.getX()) ** 2 + (p1a.getY() - p1b.getY()) ** 2)

    if distance <= tot_radius:
        overlap = Text(Point(200, 20), "The circles overlap")
        overlap.draw(win)
    else:
        overlap = Text(Point(200, 20), "The circles do not overlap")
        overlap.draw(win)

    win.getMouse()
    win.close()

def main():
    addTen([5, 2, -3])
    squareEach([3, 5.7, 2])
    sumList([3, 5.7, 2])
    toNumbers(["3", "5.7", "2"])
    writeSumOfSquares()
    starter()
    leapYear(2000)
    circleOverLap()
    pass

main()
