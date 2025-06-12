
import mypackage.mymodule as m
from mypackage.mymodule import Employee, greet, sports

m.greet(m.gname)

print("-" * 60)

emp1 = Employee("Slater", 85000)
print(emp1)

print("-" * 60)
greet("Virat")

print("-" * 60)
print(sports)
