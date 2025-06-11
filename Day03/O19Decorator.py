
def doubleMesh(fnc):
    def helper(*args):
        print("=" * 60)
        fnc(*args)
        print("#" * 60)
    return helper


def startSingle(fnc):
    def helper(*args):
        print("*" * 60)
        fnc(*args)
        print("_" * 60)
    return helper

@startSingle
@doubleMesh
def fun1():
    print("fun1 called")


fun1()
