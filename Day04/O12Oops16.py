
class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"First Name ={self.fname} \nLast Name = {self.lname}"

emp1 = Employee("Virat", "Kholi")
print(repr(emp1))