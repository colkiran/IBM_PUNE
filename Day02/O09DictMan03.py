print("pop".center(60, "-"))
emp1 = {'empid': 1234, 'ename': 'Jack', 'age': 35, 'desig': 'MGR','dept': 'finance', 'loc': 'del', 'sal': 125000}

print(f"emp1 :{emp1}")

res = emp1.pop('desig')
print(res)

res = emp1.pop('loc')
print(res)

# res = emp1.pop()
# print(res)

print(f"emp1 :{emp1}")


print("popitem".center(60, "-"))
emp1 = {'empid': 1234, 'ename': 'Jack', 'age': 35, 'desig': 'MGR','dept': 'finance', 'loc': 'del', 'sal': 125000}

print(f"emp1 :{emp1}")

res = emp1.popitem()
print(res)

res = emp1.popitem()
print(res)

res = emp1.popitem()
print(res)

print(f"emp1: {emp1}")

print("update".center(60, "-"))
emp1 = {'empid': 1234, 'ename': 'Jack', 'age': 35, 'desig': 'MGR', 'loc': 'del'}

emp2 = {'empid': 2233, 'ename': 'Tina',  'desig': 'BDE','dept': 'MKT',  'sal': 75000}

print(f"emp1 :{emp1}")
print("-" * 60)

print(f"emp2 :{emp2}")

# update emp1 with emp2's values

print("-" * 60)

emp1.update(emp2)

print(f"emp1 :{emp1}")
