
def outerFun():
    gname = "Sachin"
    def innerFun1():

        print('Hello World')
        print(f"Greetings Mr.{gname}")

    def innerFun2():

        print('Have a great day...')
        print(f"Greetings Mr.{gname}")

    return innerFun1, innerFun2


inref = outerFun()
print(type(inref))


inref[0]()

print("-" * 60)

inref[1]()


# print("-" * 60)
#
# outerFun()()            # calls the innerfun()
