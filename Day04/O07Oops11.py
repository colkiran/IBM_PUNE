
class Employee:

    def __init__(self, name):
        self.__name = name          # Private Variable
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular JS', 'React JS']


    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

emp1 = Employee('Micheal')
print(emp1)

# print("-" * 60)
# print(emp1.__name)

print("-" * 60)
print(emp1.__dict__)

print("-" * 60)
emp1._Employee__name = "Steve"

print("-" * 60)
print(emp1)
