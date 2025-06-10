
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 4.0, 5.2, 6.8, 'seven', 'eight', 9 + 2j, 10 + 3j, True,False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = 1,
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 1, 2, 3, 4, 5
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
# print(dir(t1))
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")

lst = list(t1)
lst.extend([6, 7, 8, 9, 10])
print(f"lst :{lst}")
t1 = tuple(lst)
print(f"t1 :{t1}")
print(type(t1))
