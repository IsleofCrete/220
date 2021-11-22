"""
Name: <Sydney Wertz>
<lab12>.py
"""

from random import randint

def find_and_remove(list, value):
    try:
        i = list.index(value)
        list[i] = "Sydney"
        print(list)
    except:
        pass

def read_data(file_name):
    f = open(file_name, "r")
    data = f.read()
    data = data.split() #will split on any white space
    print(data)
    return data

def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            print("Value found")
            return True
        i += 1
    print("Value not found")
    return False

def good_input():
    user_number = eval(input("Enter a number: "))
    while user_number > 10 or user_number < 1:
        user_number = eval(input("Bad number. Enter a number: "))
    print("good input")
    return user_number

def num_digits():
    num = eval(input("Enter a number: "))
    while num >= 1:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        print(digits)
        num = eval(input("Enter a number: "))

def hi_lo_game():
    rand_num = randint(1, 100)
    guess = 1
    user_input = eval(input("Enter a number between 1 and 100: "))

    while (user_input != rand_num) and (guess < 7):
        if user_input > rand_num:
            print("Too High")
            guess += 1
        elif user_input < rand_num:
            print("Too Low")
            guess += 1
        user_input = eval(input("Enter a number between 1 and 100: "))

    if user_input == rand_num:
        print("You won in", guess, "guesses!")
    else:
        print("You took too many guesses and lost. The number was", rand_num)

def main():
    #find_and_remove([1, 2, 3, 4, 5], 3)
    #read_data("dataSorted.txt")
    #is_in_linear(3, [1, 2, 3, 4, 5])
    #good_input()
    #num_digits()
    #hi_lo_game()
    pass

main()
