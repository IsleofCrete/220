"""
Name: <Sydney Wertz>
interest.py

Problem: Homework 9/13/2021 interest

Certificate of Authenticity
This assignment is entirely my own work

The round function in line 29 rounds the answer to two decimal places
Found here:
https://kodify.net/python/math/round-decimals/#round-python-values-to-two-decimals-places-and-more
"""

def main():
    ins_year_rate = eval(input("Input the annual interest rate as a percent"))
    days_bill_cycle = eval(input("Input the number of days in the billing cycle"))
    prev_net_bal = eval(input("Input the previous net balance"))
    pay_amt = eval(input("Input the payment amount"))
    day_pay_made = eval(input("Input the day of the billing cycle that the payment was made"))
    ins_dec_rate = ins_year_rate / 100
    ins_month_rate = ins_dec_rate / 12

    step_1 = prev_net_bal * days_bill_cycle
    #Multiply the net balance shown on the statement by the number of days in the billing cycle.
    step_2 = pay_amt * (days_bill_cycle - day_pay_made)
    #Multiply net payment received by number of days payment received b4 end of billing cycle.
    step_3 = step_1 - step_2
    step_4 = step_3 / days_bill_cycle
    step_5 = step_4 * ins_month_rate
    step_6 = round(step_5, 2)

    print(step_6)

if __name__ == '__main__': #should be how to run programs from now on
    main()
