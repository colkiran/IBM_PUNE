
class A:
   def fun(self):
       print("class A")

class B(A):
    # def fun(self):
    #     print("class B")
    pass


class C(A):

    def fun(self):
        print("class C")

class D(B, C):
    pass

d = D()
d.fun()
print(D.mro())

