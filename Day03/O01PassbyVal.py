
def fun(x):
    print(f"x inside the function before :{x}")
    x += " Tendulkar"
    print(f"x inside the function after :{x}")

a = input("Enter the name :")

print(f"a before the call :{a}")

fun(a)

print(f"a after the call :{a}")
