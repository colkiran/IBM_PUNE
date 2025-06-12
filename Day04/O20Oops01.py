
class Player:        # pascal casing

    def get_runs(self):
        print("Runs scored....")


sachin = Player()           # calls the default constructor
sachin.get_runs()

print("-" * 60)
print(f"isinstance(sachin, Player) :{isinstance(sachin, Player)}")
print(f"isinstance(sachin, object) :{isinstance(sachin, object)}")


