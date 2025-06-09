"""
1. for loop
2. while loop

1. continue
2. break
3. else
"""

for i in range(1, 11):
    print("hello world :", i)

print("-" * 60)
for i in range(1, 11):
    print(i, end = " ")


print("-" * 60)
for i in range(1, 31):
    # if i > 20:
    #     break
    if i % 2 == 0:
        continue
    print(i, end=" ")
else:
    print("\ncompleted generating numbers")