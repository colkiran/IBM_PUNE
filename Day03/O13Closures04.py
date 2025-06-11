
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            tiger = emojis.encode(greet + " :" + sep + ": " + gname)
            print(tiger)

            lion = emojis.encode(greet + " :" + "lion" + ": " + gname)
            print(lion)

            bear = emojis.encode(greet + " :" + "bear" + ": " + gname)
            print(bear)

        return innerMostFun

    return innerFun

hndGrt = outerFun("Namaskar")

tgrhndGrt = hndGrt("tiger")

tgrhndGrt("Prabhakar")




"""
engGrt = outerFun("Good Morning")

sArwengGrt = engGrt("------>")
dblArwengGrt  = engGrt("====>>")

sArwengGrt("Virat")
dblArwengGrt("Rohit")
dblArwengGrt("Rahul")
dblArwengGrt("Gill")
dblArwengGrt("Jadeja")
dblArwengGrt("Sai")

"""