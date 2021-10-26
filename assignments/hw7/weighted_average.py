"""
Name: <Sydney Wertz>
weighted_average.py

Problem: Weighted Average Homework 7

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    num_student = 0
    class_average = 0

    for line in in_file:
        names_grades_list = line.split(": ")
        names = names_grades_list[0]
        grades1 = names_grades_list[1]
        grades2 = grades1.split(" ")
        weight_calc = 0
        weight_avg = 0

        for i in range(0, len(grades2), 2):
            weight_calc += int(grades2[i])

        if weight_calc > 100:
            out_file.write(names + "'s average: Error: The weights are more than 100." + "\n")
        elif weight_calc < 100:
            out_file.write(names + "'s average: Error: The weights are less than 100." + "\n")

        elif weight_calc == 100:
            num_student += 1 #this line keeps track of # of students with valid weighted grades for class average
            for i in range(0, len(grades2), 2):
                weight_avg += (int(grades2[i]) * int(grades2[i+1]))
                weight = weight_avg / 100
            out_file.write(names + "'s average: " + str(round(weight, 1)) + "\n")
            class_average += weight
    class_average = class_average / num_student
    out_file.write("Class average: " + str(round(class_average, 1)) )

def main():
    weighted_average("grades.txt", "avg.txt")
main()