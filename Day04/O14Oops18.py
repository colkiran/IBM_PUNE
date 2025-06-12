class Animal:

    def eat(self):
        print("Animals eat....")

class Bird(Animal):

    def fly(self):
        print("Birds fly......")

class Chicken(Bird):

    def msg(self):
        print("Chickens are breeded for consumption......")


    def fly(self):
        print("Chickens seldom fly....")


chic = Chicken()
chic.eat()
chic.fly()
chic.msg()
