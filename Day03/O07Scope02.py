
# global scope

glbX = 100

def fun(x):
    global glbX

    print(f"x :{x}")
    glbX = 1000
    print(glbX)

print(f"glbX  before :{glbX}")

fun(10)

print(f"glbX after :{glbX}")
