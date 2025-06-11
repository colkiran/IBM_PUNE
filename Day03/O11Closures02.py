
def outerFun(info):     # HOF - higher order function
    inf = "Mr." + info

    def innerFun():
        print(inf)
        print(info)
        return inf

    return innerFun

outerFun("Rahul")

print("-" * 60)
print(outerFun.__name__)
print(outerFun("Rahul").__name__)

print("-" * 60)
print(outerFun("Rahul")())         # calls the innerFun

print("-" * 60)
inref = outerFun("Rohit")
print(inref())
