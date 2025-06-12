
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        # return self.tech.__iter__()
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, idx, val):
        self.tech[idx] = val


emp1 = Employee("Jack", 30000)
print(emp1)

print("-" * 60)
print(len(emp1))

print("-" * 60)
print([emp for emp in emp1])

print("-" * 60)
emp1.append("Python")
print([emp for emp in emp1])

print("-" * 60)
x = emp1[2]
print(x)

print("-" * 60)
emp1[2] = 'JSP'
print([emp for emp in emp1])

