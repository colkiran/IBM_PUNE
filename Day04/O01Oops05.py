
class Player:

    Team = "India"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Virat", 36)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rohit", 38)
ply2.get_details()

print("-" * 60)
print(f"Player :{Player.Team}")
print(f"ply1   :{ply1.Team}")
print(f"ply2   :{ply2.Team}")

print("-" * 60)
Player.Team = "MI"
print(f"Player :{Player.Team}")
print(f"ply1   :{ply1.Team}")
print(f"ply2   :{ply2.Team}")

print("-" * 60)
ply1.Team = "RCB"
print(f"ply1   :{ply1.Team}")
print(f"Player :{Player.Team}")
print(f"ply2   :{ply2.Team}")

print("-" * 60)
print(ply1.__dict__)

print("-" * 60)
print(Player.__dict__)
