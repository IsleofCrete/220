"""
Name: <Sydney Wertz>
traffic.py

Problem: Homework 4 9/30/2021

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""

def main():
    tot_roads = eval(input("How many roads were surveyed?"))
    tot_days = 0
    tot_veh = 0
    for i in range(1, tot_roads + 1):
        days = eval(input("How many days was road " + str(i) + " surveyed?"))
        tot_cars = 0
        tot_days = tot_days + days
        for j in range(1, days + 1):
            cars = eval(input("How many vehicles travelled on day " + str(j) + "?"))
            tot_cars = tot_cars + cars
        tot_veh = tot_veh + tot_cars
        car_avg = tot_cars / days
        print("Road " + str(i) + " average vehicles per day:", round(car_avg, 2))
    print("Total number of vehicles travelled on all roads:", tot_veh)
    tot_avg = tot_veh / tot_roads
    print("Average number of vehicles per road:", round(tot_avg, 2))


if __name__ == '__main__':
    main()
