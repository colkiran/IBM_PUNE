
# local scope - lexical scope - scope within block

def fun(x):         # x is a local variable
    print(f"x :{x}")
    y = "Hello world"
    print(f"y inside :{y}")

fun(50)

print(f"After the function : {x}")
print(f"After the function : {y}")
