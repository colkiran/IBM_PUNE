
def outerFun(greet):
    def innerFun(gname):
        # simple curry
        print(greet, gname)

    return innerFun

engGrt = outerFun("Good Morning")
hndGrt = outerFun("Namaskar")

engGrt("Virat")
engGrt("Rohit")

hndGrt("Ajay")
