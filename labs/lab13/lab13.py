"""
Name: <Sydney Wertz>
<lab13>.py
"""

from graphics import *

def is_in_binary(search_val, values):
    left = 0
    right = len(values) - 1
    middle = (right + left) // 2
    middle_value = values[middle]

    while left < right:

        if search_val == middle_value:
            print("Search value is:", middle_value)
            break

        if search_val < middle_value:
            print("Too high")
            right = middle - 1
            middle = (right + left) // 2
            middle_value = values[middle]

        if search_val > middle_value:
            print("Too low")
            left = middle + 1
            middle = (right + left) // 2
            middle_value = values[middle]

def selection_sort(values):
    position = 0
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i+1, len(values)):
            if values[i] > values[j]:
                lowest = values[j]
                position = j
                values[i], values[position] = values[position], values[i]
        print(values)

def rect_sort(rectangles):
    position = 0
    for i in range(len(rectangles)):
        lowest = rectangles[i]
        position = i
        for j in range(i + 1, len(rectangles)):
            if calc_area(rectangles[i]) > calc_area(rectangles[j]):
                lowest = rectangles[j]
                position = j
                rectangles[i], rectangles[position] = rectangles[position], rectangles[i]
        print(rectangles)

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return (dx * dy)

def star_find(filename):
    file = open(filename, "r")
    signals = file.read().split()
    found_signals = []
    pulses = 0
    not_pulses = 0

    for i in range(len(signals)):
        if 4000 <= int(signals[i]) <= 5000:
            found_signals.append(int(signals[i]))
            pulses += 1
        if (int(signals[i]) < 4000) or(int(signals[i]) > 5000):
            not_pulses += 1
        if pulses == 5:
            print(found_signals)
            print(not_pulses, "pulse searches occured before 5 pulses found")
            break

def main():
    #is_in_binary(1, [1, 3, 5, 7, 9])
    #selection_sort([2, 4, 5, 1, 3])
    #star_find("signals.txt")
    rect_list = [Rectangle(Point(0, 0), Point(10, 10)), Rectangle(Point(0, 0), Point(15, 15)), Rectangle(Point(0, 0), Point(5, 5))]
    rect_sort(rect_list)
    pass

main()
