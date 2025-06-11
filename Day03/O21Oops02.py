
class Player:
    def __init__(self):     # constructor
        print("Player Initialized......")

    def get_runs(self):
        print("Run scored.....")

    def __del__(self):
        print("Object destroyed.....")

sachin = Player()
sourav = Player()
sachin.__init__()
print("-" * 60)
del sourav
print("*" * 60)
