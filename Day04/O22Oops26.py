class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    class Employee:

        def __init__(self, name, role):
            self.name = name
            self.role = role

    def add_employee(self, employee):
        self.employees.append(employee)

comp = Company("IBM")


emp1 = comp.Employee('Kevin', "MGR")
emp2 = comp.Employee("Slater", "TL")


comp.add_employee(emp1)
comp.add_employee(emp2)


for employee in comp.employees:
    print(employee.name, "\t\t", employee.role)



