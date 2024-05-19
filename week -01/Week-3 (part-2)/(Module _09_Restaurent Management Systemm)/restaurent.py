from menu import Menu


class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu= Menu()

    def add_employee(self,Employee):
        self.employees.append(Employee)
        print(f"Employee {Employee.name} Adding Done...!")

    def view_employee(self):
        print("|=================(Employee List)=================|")
        for emp in self.employees:
            print("name\temail\tphone\taddress")
            print(f"{emp.name}\t{emp.email}\t{emp.phone}\t{emp.address}")