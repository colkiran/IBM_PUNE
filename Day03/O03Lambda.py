
def add(x, y):
    return x + y

a = add         # a and add are the same
res = a(43, 56)
print(res)

print("-" * 60)

l = lambda a, b : a + b
res = l(78, 28)
print(res)

# lambdas are best used with  - MAP, FILTER, REDUCE
print("map".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x : x ** 2,  l1))
print(f"squares :{squares}")

# expenses = [500, 200, 1500, 2500, 850, 5000]   # dollars convert it into rupees

print("filter".center(60, "-"))
# expression should return a True or False

l2 = list(range(1, 31))
print(f"l2 :{l2}")

print("-" * 60)
res = list(filter(lambda x : x % 3 == 0, l2))
print(res)

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
words = list(filter(lambda x : x != 'the', sentence.split()))
print(f"words :{words}")

print("-" * 60)
words = list(filter(lambda x : len(x) == 3 , sentence.split()))
print(f"words :{words}")

print(f"reduce".center(60, "-"))
# reduce the list to a single value
from functools import reduce

l1 = [4, 9, 6, 1, 3, 5, 8, 10, 7, 2]
print(f"l1 :{l1}")

print("-" * 60)
res = reduce(lambda x, y : x if x < y else y, l1)
print(f"res :{res}")

print("-" * 60)
res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

