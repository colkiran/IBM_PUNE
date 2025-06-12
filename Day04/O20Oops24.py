
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account Ctor.....")

    @abstractmethod
    def getBalance(self):
        pass

    def deposit(self):
        pass


class Savings(Account):

    def withdraw(self):
        print("Debited from the account")

    def getBalance(self):
        print("Balance in the account ending is #######.##")


sav = Savings()
sav.getBalance()
sav.withdraw()
