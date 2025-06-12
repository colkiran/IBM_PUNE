
class A:

    def fun(self):
        print("Class A")

class B(A):
    def fun(self):
        print("Class B")

class C(A):

    def fun(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.fun()
print(D.mro())

