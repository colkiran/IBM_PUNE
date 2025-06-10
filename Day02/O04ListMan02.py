# functions to add new values into the list - append, insert, extend

print("append".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

l1.append([9, 10, 11, 12, 13])

print(f"l1 :{l1}")
print(l1[8][1:4])
print(l1[-1][1:4])

print("extend".center(60, "-"))
l2 = [6, 7, 8, 9, 10]
print(f"l2 :{l2}")

l2.extend([11, 12, 13, 14])
print(f"l2 :{l2}")

l2.extend([15])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")
l1.insert(15, 100)
print(f"l1 :{l1}")

# to remove values from the list
print("remove".center(60,"-"))
l1 = [1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

l1.remove(3)
l1.remove(3)
l1.remove(3)

print("pop".center(60, "-"))
# returns the value that was removed from the list
l1 = list(range(1, 11))
print(f"l1 :{l1}")

ret = l1.pop(3)
print(ret)

ret = l1.pop(-1)
print(ret)

ret = l1.pop()          # will remove the last element from the list
print(ret)

print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
