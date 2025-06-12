
class A:

    def fun(self):
        print("Class A")


class B(A):

    def fun(self):
        print("Class B")

class C(A, B):
    pass

c = C()
# c.fun()
# print(C.mro())
