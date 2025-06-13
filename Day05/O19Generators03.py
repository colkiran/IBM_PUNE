
def get_name(surname):
    print(f"surname is {surname}")

    while True:
        name = yield
        print(f"received :{name}")
        print("-" * 60)
        if surname in name:
            print(f"Surname found :{surname} in {name}")

cObj = get_name("Pillai")
print(cObj)

cObj.__next__()
cObj.send("Sachin Tendulkar")
cObj.send("Virat Kholi")
cObj.send("Dhanraj Pillai")
