
class Animal:

    def __init__(self):
        print('Animal Ctor......')
        self.a = 10


    def eat(self):
        print("Animals eat.....")


    def fun(self):
        print("Fun method of Animal class......")

class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20


    def walk(self):
        print("Person Walks......")

    def fun(self):
        print("Fun method of Person class......")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor.....")
        self.g = 30

    def talk(self):
        print("Girl talks......")

grace = Girl()
grace.eat()
grace.walk()
grace.talk()

print("-" * 60)
grace.fun()

print("-" * 60)
print(grace.__dict__)
