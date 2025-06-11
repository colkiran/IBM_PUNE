def fun(*args):
    print(args)
    print(*args)


fun()
print("-" * 60)

fun(10)
print("-" * 60)

fun(10, 20)
print("-" * 60)

fun(10, 20, 30)
print("-" * 60)

def sum(x, y):
    print("sum function called.....")
    return x + y

def diff(x, y):
    print('diff function called......')
    return x - y

def outerFun(fnc):
    loginfo = "Logging about done....."
    def helperFun(*args):
        print(loginfo)
        print(fnc(*args))       # call back
        print("-" * 60)

    return helperFun

sumlogger = outerFun(sum)
sumlogger(34, 75)

difflogger = outerFun(diff)
difflogger(30, 12)
