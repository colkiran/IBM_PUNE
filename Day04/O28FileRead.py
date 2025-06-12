"""
r - read mode
you can read the contents of the file
if the file is not present then throws an error
"""

FL = open("data.txt", "r")

# st = FL.read()
#st = FL.read(5000)

# reads one line at a time
# st = FL.readline()
# print(st)
# st = FL.readline()

# st = FL.readlines()
# print(st)

# for line in FL.readlines():
#     print(line)

st = FL.readlines(860)
print(st)


FL.close()