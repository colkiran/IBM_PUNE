
from abc import ABC, abstractmethod

class Employee:

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers job.....")


class Developer(Employee):

    def doJob(self):
        print("Write coding.......")


def BankJob(emp):           # polymorphism
    print("Bank job started.....")
    emp.doJob()
    print("Bank job completed......")
    print("-" * 60)


mike = Manager()
david = Developer()

BankJob(mike)
BankJob(david)

