values = list(range(10, 31, 10))
print(values)

# upack the list
a, b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

values = list(range(10, 101, 10))
print(values)

print("-" * 60)
a, b, *c = values       # var with a star can store more than one val
print(a, b, c, sep=", ")

print("-" * 60)
a, *b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]
print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

print("-" * 60)
lst3 = [lst1, lst2]
print(len(lst3))
print(f"lst3 :{lst3}")

print("-" * 60)
lst4 = [*lst1, *lst2]       # unpack
print(len(lst4))
print(f"lst4 :{lst4}")

print("-" * 60)
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 60)
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], "\t", letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(index, "\t", letter)

print("-" * 60)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(ind, "\t", lst)

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")
print("-" * 60)
