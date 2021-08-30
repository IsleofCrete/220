"""
Name: <Sydney Wertz>
lab1.py

Problem: This function calculates the area of a rectangle
"""

#*quietly* I miss Java

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume, "inches cubed")

def shooting_percentage():
    made = eval(input("Enter shots made: "))
    total = eval(input("Enter total shots: "))
    percentage = ((made / total)*100)
    print("The shooting percentage is ", percentage,"%")

def coffee():
    pounds = eval(input("Enter the pounds of coffee ordered: "))
    price = 10.50 #are these lines unnecessary in writing the code exactly how it wants us to?
    shipping = 0.86 #yes, yes they are, but I will get confused if these aren't there
    coffeeImport = (price * pounds) + (shipping * pounds) + 1.50 #hehe camelCase
    #$1.50 is the overhead price for order
    print("The total cost is $", coffeeImport)

def kilometers_to_miles():
    kilometers = eval(input("Enter kilometers travelled: "))
    miles = kilometers / 1.61
    print("The number of miles is:", miles) #discount yet more complicated Google type beat

#calc_rec_area()
#calc_volume()
#shooting_percentage()
#coffee()
#kilometers_to_miles()