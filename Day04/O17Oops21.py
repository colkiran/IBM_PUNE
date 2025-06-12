
class A:

    def fun(self):
        print("Class A")

class B:

    def fun(self):
        print("Class B")

class C(A, B):

    # def fun(self):
    #     print("Class C")
    pass


class D(C, B):
    pass

d = D()
d.fun()
print(D.mro())

