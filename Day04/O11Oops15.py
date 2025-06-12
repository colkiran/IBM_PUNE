"""
class
object
isinstance
__init__   - constructor
self
__dict__
class attribute
class methods
Operator overloading - __str__, __eq__, __gt__, @total_ordering
arithmetic operators - __add__, __sub__, __mul__, __truediv__
__len__, append, __iter__, __getitem__, __setitem__
private variable = __var
__dict__
property(), @property, setter, deleter
"""

# inheritance

class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.a = 10

    def eat(self):
        print("Animals eat.....")


class Bird(Animal):

    def fly(self):
        print("Birds fly......")


class Fish(Animal):

    def swim(self):
        print("Fishes swim.....")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)
dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 60)
print(cuckoo.__dict__)
print(dolphin.__dict__)

