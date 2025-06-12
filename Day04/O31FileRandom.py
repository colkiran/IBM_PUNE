
FL = open("data.txt", "rb")

pos = FL.seek(100, 0)
print(pos)

pos = FL.seek(-50, 1)
print(pos)

pos = FL.seek(150, 1)
print(pos)

pos = FL.seek(150, 2)
print(pos)

pos = FL.seek(0, 2)
print(pos)

# pos = FL.seek(-10, 0)
# print(pos)

FL.close()