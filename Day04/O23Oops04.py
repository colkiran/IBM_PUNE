"""
self - will have the name of the object that called the method

"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized......")

    def get_details(self):
        print(f"Name is :{self.name}\nAge is :{self.age}")

ply1 = Player("Virat", 36)
ply1.get_details()
print("-" * 60)

ply2 = Player('Rohit', 38)
ply2.get_details()

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")     # instance variables

print("-" * 60)
print(f"ply2 :{ply2.__dict__}")     # instance variables

print("-" * 60)
ply2.runs = 250
print(ply2.__dict__)

print("-" * 60)
print(ply1.__dict__)
