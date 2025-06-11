
import time


def timeCalc(fnc):

    def innerFun(y):
        print("Starting to execute the function......")
        st = time.perf_counter()
        fnc(y)
        et = time.perf_counter()
        print("Completed executing.....")
        print(f"The total time taken to execute is :{round(et -st, 2)}")
    return innerFun

@timeCalc
def fun(x):
    lst = []
    for i in range(1, x):
        for j in range(1, i + 1):
            lst.append(j ** 3)

fun(6500)
