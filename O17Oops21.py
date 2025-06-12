
# MRO - Method Resolution Order

class A:
    def fun(self):
        print("Class A")

class B:

    def fun(self):
        print("Class B")

class C(B, A):
    pass

c = C()
c.fun()

print("-" * 60)
print(C.mro())
