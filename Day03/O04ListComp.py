
squares = [x ** 2 for x in range(1, 11)]
print(f"squares :{squares}")

fruits = [
    ('apple', 285),
    ('orange', 135),
    ('grapes', 120),
    ('mango', 70),
    ('gauva', 110),
    ('watermelon', 30),
    ('strawberry', 350),
    ('banana', 60)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruit" for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[0] for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] * 0.9 for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] * 0.75 for fruit in fruits]
print(price)

print("-" * 60)
expFrts = [fruit for fruit in fruits if fruit[1] > 100]
print(expFrts)

print("-" * 60)
expFrts  = [[fruit[0], fruit[1], fruit[1] * 0.9,  fruit[1] * 0.75]
            for fruit in fruits if fruit[1] > 100]
print(expFrts)

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
words = [word for word in sentence.split()]
print(words)

print("-" * 60)
words = [(word, len(word)) for word in words if word != 'the']
print(words)

print("-" * 60)
boys = ['peter', 'richard', 'kennedy', 'john', 'louis', 'alwin']
girls = ['rita', 'tina', 'mary', 'aliya', 'grace', 'celene']

res = [(boy, girl) for boy in boys for girl in girls]
print(res)
