"""
to implement @total_ordering we have to overload two comparison operators
1. equal_to (comparison) is mandatory
2. greater_than or less_than or any other operator

"""


from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"


# works for NOT EQUAL TO also (!=)
    def __eq__(self, other):
        return self.salary == other.salary

# works for LESS THAN also (<)
    def __gt__(self, other):
        return self.salary > other.salary



emp1 = Employee('Kevin', 15000)
print(str(emp1))
print(emp1)

print("-" * 60)
emp2 = Employee("Peter", 20000)
print(emp2)

print("-" * 60)
if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))


print("-" * 60)
# print(emp1 > emp2)

if emp1 < emp2:
    print("{}'s salary of {} is LESS Than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is GREATER Than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
print(emp1 >= emp2)
