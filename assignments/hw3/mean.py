"""
Name: <Sydney Wertz>
mean.py

Problem: Homework 9/23/2021 Means

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""
import math

def main():
    x_n = eval(input("How many terms will you be finding the average of?"))
    tot_rms = 0
    tot_harm = 0
    tot_geo = 1
    for i in range(1, x_n+1): #if not using i in the code, can replace i with _ in for loop so linting doesn't get mad
        usr_val = eval(input("Enter value " + str(i) + ":"))
        tot_rms = tot_rms + usr_val**2
        tot_harm = tot_harm + (1/usr_val)
        tot_geo = tot_geo * usr_val
    rms_avg = math.sqrt((tot_rms / x_n))
    print(round(rms_avg, 3))
    harm_mean = x_n / tot_harm
    print(round(harm_mean, 3))
    geo_mean = tot_geo ** (1/x_n)
    print(round(geo_mean, 3))

if __name__ == '__main__':
    main()
