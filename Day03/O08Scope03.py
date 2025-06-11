
def outerFun():
    gname = "Rahul"
    def innerFun():
        nonlocal gname      # only if it non-local variable

        print("Hello World")
        gname += " Dravid"
        print(gname)

    innerFun()
    print(f"gname :{gname}")


outerFun()
