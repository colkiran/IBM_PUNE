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
wopm = Company('Wipro')

emp1 = comp.Employee('Kevin', "MGR")
emp2 = comp.Employee("Slater", "TL")
emp3 = wopm.Employee('Kenith', "PM")

comp.add_employee(emp1)
comp.add_employee(emp2)
comp.add_employee(emp3)

for employee in comp.employees:
    print(employee.name, "\t\t", employee.role)



