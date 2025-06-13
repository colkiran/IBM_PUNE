l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")
print(type(l))
# print(dir(l))

iterobj = l.__iter__()
# print(dir(iterobj))

print("-" * 60)
e1 = iterobj.__next__()
print(e1)
e1 = iterobj.__next__()
print(e1)
e1 = iterobj.__next__()
print(e1)
e1 = iterobj.__next__()
print(e1)
e1 = iterobj.__next__()
print(e1)
# stopiteration
# e1 = iterobj.__next__()
# print(e1)
