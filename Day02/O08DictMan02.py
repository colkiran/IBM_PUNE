
print("keys".center(60, "-"))
player = {'name': 'Rohit', 'age': 38, 'runs': 105, 'oppn':"Aus"}
print(f"Player :{player}")

k = player.keys()
print(k)

print("\n")

for k in player.keys():
    print(k, "=>", player[k])

print("values".center(60, "-"))
player = {'name': 'Rohit', 'age': 38, 'runs': 105, 'oppn':"Aus"}
print(f"Player :{player}")

v = player.values()
print(v)

print("items".center(60, "-"))
emp = {
    'emp1': {'empid': 1234, 'ename': 'Jack', 'age': 35, 'desig': 'MGR','dept': 'finance', 'loc': 'del', 'sal': 125000},
    'emp2': {'empid': 2233, 'ename': 'Tina', 'age': 29, 'desig': 'BDE','dept': 'MKT', 'loc': 'Che', 'sal': 75000},
    'emp3': {'empid': 3303, 'ename': 'Kevin', 'age': 40, 'desig': 'GM','dept': 'Procurement', 'loc': 'Pune',
             'sal': 150000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("get".center(60, "-"))
emp1 = {'empid': 1234, 'ename': 'Jack', 'age': 35, 'desig': 'MGR','dept': 'finance', 'loc': 'del', 'sal': 125000}

print(f"emp1 :{emp1}")
print(f"Name :{emp1.get('ename', 'Invalid key, Please enter a valid key.....')}")
print(f"Desig :{emp1.get('desg', 'Invalid key, Please enter a valid key.....')}")

print("fromkeys".center(60, "-"))
# convert a list to a dict
cities = ['blr', 'che', 'hyd', 'pun', 'mum', 'del']
print(f"cities :{cities}")

print("\n")

res = dict.fromkeys(cities)
print(res)

print("\n")

res1 = dict.fromkeys(cities, 24)
print(res1)

print("setdefault".center(60, "-"))
emp2 = {'empid': 2233, 'ename': 'Tina', 'age': 29, 'desig': 'BDE','dept': 'MKT'}
print(f"emp2 :{emp2}")
print(type(emp2))

print("-" * 60)
# modify
emp2.setdefault('ename', 'Maria')
emp2.setdefault('dept', 'DWH')

# new
emp2.setdefault('loc', 'Che')
emp2.setdefault('sal', 75000)

print(f"emp2 :{emp2}")
