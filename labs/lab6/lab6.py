"""
Name: <Sydney Wertz>
<lab6>.py
"""

def name_reverse():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    print("THe name switch is {0}, {1}".format(last_name, first_name))

def company_name():
    web_domain = input("Input an internet domain in www.x.com(org, net) format: ")
    company = web_domain.split('.')
    print("The company/domain is: " + company[1])

def initials():
    students = eval(input("How many students are in the class: "))
    for i in range(1, students+1):
        first_name = input("Enter the first name of student " + str(i) + ": ")
        last_name = input("Enter " + str(first_name) + "'s last name: ")
        initial = str(first_name[0]) + str(last_name[0])

        print(str(first_name) + "'s initials are " + str(initial))

def names():
    name_list = input("Enter a list of first and last names separated by commas: ")
    full_name = name_list.split(", ")
    print("The initials are", end = " ")
    for i in range(len(full_name)):
        first_name, last_name = full_name[i].split(" ")
        print(first_name[0] + last_name[0], end = " ")
    print()

def thirds():
    sentence = input("Enter a sentence: ")
    for i in range(2, len(sentence), 3):
        third_letter = sentence[i]
        print(str(third_letter), end = "")
    print()

def word_average():
    sentence = input("Enter a sentence: ")
    sentence = sentence.split(" ")
    acc = 0
    for i in range(len(sentence)):
        acc += len(sentence[i])
    average = acc / len(sentence)
    print(round(average, 4))

def pig_latin():
    sentence = input("Enter a sentence: ")
    sentence = sentence.lower()
    indiv_word = sentence.split(" ")
    for word in indiv_word:
        pig = word[1:] + word[0] + str("ay")

        print(pig, end = " ")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

main()
