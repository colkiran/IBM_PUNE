"""
load  -- is used to read the data from file
loads -- is used to convert json string to python dictionary
"""


import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile)
for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("loads".center(60, "-"))
empdata = '{"name":"Lionel", "age":35, "dept":"HR", "salary": 45000}'
print(empdata)
print(type(empdata))

res = json.loads(empdata)
print(res)
print(type(res))

