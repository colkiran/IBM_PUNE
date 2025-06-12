
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.age = '1 year'

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):             # overriding parent class Ctor
        super().__init__()          # call the parent class Ctor
        print("Bird Ctor......")
        self.weight = '2 kg'

    def fly(self):
        print("Birds fly.......")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

print("-" * 60)
print(cuckoo.__dict__)
