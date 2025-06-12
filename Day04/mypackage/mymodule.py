
gname = "Sachin"

sports = ['cricket', 'tennis', 'hockey', 'football', 'boxing', 'swimming']

runs = {'odi': 18500, 'test': 12600, 't20': 4300}

def greet(gm):
    print(f"Greetings Mr.{gm}, Welcome to the event.....")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"


