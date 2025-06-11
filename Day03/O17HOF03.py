def funLogger(fnc):
    def helper():
        print("My info logged into a service......")
        fnc()
        print("My info logged out......")
        print("-" * 60)

    return helper

def normalFun():
    print("Call me normal function.....")

funLogger(normalFun)
print("-" * 60)

funLogger(normalFun)()
print("-" * 60)

res_fun = funLogger(normalFun)
res_fun()
print("-" * 60)

print("-" * 60)
normalFun = funLogger(normalFun)
normalFun()

@funLogger              # => basicFun = funLogger(basicFun)
def basicFun():
    print("Call me basic function")

# print("-" * 60)
# basicFun = funLogger(basicFun)
# basicFun()

print("-" * 60)
print(basicFun.__name__)
basicFun()
