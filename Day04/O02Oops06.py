
class Player:

    Team_Head = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        # Factory pattern
        print("Factory....")
        return cls(f"{fname} {lname}", age)            # calls the constructor

    @classmethod
    def Set_Name(cls, name):
        cls.Team_Head = name

    @classmethod
    def Get_Name(cls):
        return cls.Team_Head


ply1 = Player("Yuvraj Singh", 35)
ply1.get_details()
print("-" * 60)

# Accept Name like - FirstName and LastName
ply2 = Player.CreatePlayer("Virat", "Kholi", 36)
ply2.get_details()

print("-" * 60)
Player.Set_Name("Mark")
print(Player.Get_Name())





