from sales_person import SalesPerson

class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        open_file = open(file_name, "r")

        for lines in open_file.readlines():
            line = lines[:-1]
            self.sales_people.append(line)

        open_file.close()

    def quota_report(self, quota):
        quota_list = []

        for i in range(len(self.sales_people)):
            person_list = self.sales_people[i]
            person_list = person_list.split(", ")

            person = SalesPerson(person_list[0], person_list[1])
            indiv_list = []
            indiv_list.append(person.get_id())
            indiv_list.append(person.get_name())

            sales = person_list[2].split()
            for i in range(len(sales)):
                person.enter_sale(sales[i])
            total = person.total_sales()
            indiv_list.append(float(total))

            indiv_quota = person.met_quota(quota)
            indiv_list.append(bool(indiv_quota))

            quota_list.append(indiv_list)

        return quota_list

    def top_seller(self):
        highest_list = []
        for i in range(len(self.sales_people)):
            person_list = self.sales_people[i]
            person_list = person_list.split(", ")

            person = SalesPerson(person_list[0], person_list[1])

            sales = person_list[2].split()
            for i in range(len(sales)):
                person.enter_sale(sales[i])
            total = person.total_sales()

            highest_list.append(person)

        for i in range(len(highest_list)):
            if len(highest_list) <= 1:
                break

            comparing = highest_list[0]
            compare = comparing.compare_to(highest_list[1])

            if compare == 1:
                highest_list.pop(1)
            elif compare == -1:
                highest_list.pop(0)

        # for i in range(len(highest_list)):
        #     highest_list[i].__str__()

        return highest_list

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            person_list = self.sales_people[i]
            person_list = person_list.split(", ")

            person = SalesPerson(person_list[0], person_list[1])

            sales = person_list[2].split()
            for i in range(len(sales)):
                person.enter_sale(sales[i])
            total = person.total_sales()

            if person.get_id() == int(employee_id):
                return person.get_name()
