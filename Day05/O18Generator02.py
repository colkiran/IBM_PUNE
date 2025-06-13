
def fun():
    x = 1
    print('Apples from Ooty')
    yield 1
    x += 9
    print("Oranges from Kanpur")
    yield x
    x += 10
    print("Grapes from hubli")
    yield x

res = fun()
print(f"res :{res}")

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

# print("-" * 60)
# print(res.__next__())

def fun():
    for i in range(1, 11):
        yield i

print("-" * 60)
fObj = fun()
print(next(fObj))
print(next(fObj))
print(next(fObj))
