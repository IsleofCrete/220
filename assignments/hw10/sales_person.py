"""
Name: <Sydney Wertz>
sales_person.py

Problem: Homework 10

Certificate of Authenticity
I certify that his assignment is entirely my own work
"""

class SalesPerson:
    """
    SalesPerson creates an employee with their id, name, and all of their sales.
    Functions include get functions,add sale to employee, calculate total sales,
    check if employee meets quota, and employee comparison
    """

    def __init__ (self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def get_sales(self):
        return self.sales

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(len(self.sales)):
            total += float(self.sales[i])
        return float(total)

    def met_quota(self, quota):
        return bool(self.total_sales() >= quota)

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        if other.total_sales() == self.total_sales():
            return 0

    def __str__(self):
        info_string = "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
        return info_string
