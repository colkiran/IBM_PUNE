
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'Sachin', 'age': 36, 'runs': 125, 'oppn': 'WI'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'Rahul'), ('age', 32), ('runs', 85), ('oppn', 'Nzl')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name="Virat", age=36, runs=95, oppn='Eng')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD
# create
player = {'name': 'Sachin', 'age': 35, 'runs': 150, 'oppn': 'WI'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("\n")

for x in player:
    print(x + " => " + str(player[x]))

print("-" * 60)
# Update
# modify the existing data
print(f"player :{player}")
player['name'] = "Tendulkar"
player['runs'] = 65

print(f"player :{player}")

player['year'] = 2012
player['venue'] = 'Sabina Park'

print(f"player :{player}")

print("-" * 60)
# delete
print(f"player :{player}")

del player['age']
del player['runs']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
