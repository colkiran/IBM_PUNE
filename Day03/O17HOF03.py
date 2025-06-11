
def funLogger(fnc):
    def helper():
        print("My info logged into a service......")
        fnc()
        print("My info logged out......")
        print("-" * 60)

    return helper

def normalFun():
    print("Call me normal function......")

funLogger(normalFun)
print("-" * 60)

funLogger(normalFun)()          # calls the helper function
print("-" * 60)

fun_res = funLogger(normalFun)
fun_res()
print("-" * 60)

# name of the variable is normalFun
normalFun = funLogger(normalFun)
normalFun()
print("-" * 60)

print("-" * 60)
@funLogger          # basicFunc = funLogger(basicFunc)
def basicFunc():
    print("call me basic function.....")

# basicFunc = funLogger(basicFunc)
print(basicFunc.__name__)

print("-" * 60)
basicFunc()         # calls helper function
