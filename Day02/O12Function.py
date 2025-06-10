
def greet():
    print(f"Greetings Mr.Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city is a default variable and gname is a non default variable
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event....")


greet()

print("-" * 60)

greetGst("Rahul")
greetGst("Virat")

print("-" * 60)

greetGstCty("Rohit")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
# args and kwargs
def admsn(name, dob, gender, conno, city, emailid, qlf):
    print(f"Name            :{name}")
    print(f"DOB             :{dob}")
    print(f"Gender          :{gender}")
    print(f"Contact No.     :{conno}")
    print(f"City            :{city}")
    print(f"Email ID        :{emailid}")
    print(f"Qualification   :{qlf}")

# args
admsn("Richard", "23/05/1985", "Male", '99324234', 'California', 'richard@gmail.com', 'Engineering Graduate')

print("-" * 60)

# kwargs
admsn(gender="Female", qlf='Commerce Graduate', conno='45234234', dob="07/02/1989", name="Rita", emailid='rita@gmail.com', city="NYK")

print("-" * 60)
# variable length arguments - array, dictionary

def prodAll(*numbers):
    print(numbers)
    print(*numbers)         # unpacking
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(res)

print("-" * 60)

def extractDet(**detials):
    print(detials)
    for k, v in detials.items():
        print(k, "=>", v)


extractDet(name="Rahul", age=30, runs=25, oppn='Aus')

print("-" * 60)
def multiplyMe(x, y):
    return x * y

a = 5
b = 15
print(f"The product of {a} and {b} is :{multiplyMe(a, b)}")

# Recursive calls - function calling itself
# 1. factorial of a number
# 2. fibonacci series

print("-" * 60)

def arithmetic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmetic(20, 8)
print(res)

print("-" * 60)

def fun():
    "this is a doc string"
    # this is a comment
    print("Hello World")

fun()

print(fun.__doc__)             # double underscore -> dunder_doc

print("-" * 60)

def fun1(x, y):
    """
    fun1(X, y)
    ----------
    1. if x and y are integers then the function returns the sum of the numbers
    2. if x and y are strings then the function returns the concatenated string
    3. if x and y are of different data types then it throws an error

    """
    return x + y

print(fun1(199, 345))
print(fun1("Hello ", "World"))
# print(fun1(100, "world"))

print("-" * 60)
help(fun1)