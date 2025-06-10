
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 9 + 2j, 10 - 0j, True, False, 13.5, 14.0, 15.9]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD
# create
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

print("-" * 60)
# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")

for i in l1:
    print(i, end=" ")
print()

for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

print("-" * 60)
# update => change the existing values, add a new value
print(f"l1 :{l1}")

l1[0] = 100
l1[4] = 500

print(f"l1 :{l1}")

l1[3] = 450
print(f"l1 :{l1}")

# l1[5] = 600
print("-" * 60)
# delete
del l1[2]
del l1[-1]

print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))
