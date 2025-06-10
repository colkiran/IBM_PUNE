# emulate printf of C language

format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "superb")       # tuple
print(values)

print(format % values)
print("-" * 60)

format = "Welcome %s, your rating of %.3f what a %s player"


print(format % ("Sachin", 4, "superb"))
print(format % ("Sachin", 4.8, "superb"))
print(format % ("Sachin", 4.83245, "superb"))
print(format % ("Sachin", 4.8435345234, "superb"))

print("-" * 60)
# emulate unix shell scripting
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name="Sachin", adj="class"))

print("-" * 60)
# format from string functions of python

print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))

print("Welcome {1}, what a {2} player for {0}".format("Sachin", "class", "India"))

print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))

print("Welcome {name}, what a {adj} player for {cntry}".format(name="Sachin", adj="class", cntry="India"))

print("Welcome {name} with a {rating:.3f}, what a {adj} player".format(name ="Sachin", rating = 4.832847, adj = "class"))

print("-" * 60)
# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers Constant = {e}")

print("PI = {} and Eulers Constant = {}".format(pi, e))

print("-" * 60)
full_name = ['Sachin', "Tendulkar"]
print(full_name)

print("Mr.{name}".format(name=full_name))
print("Mr. {name[0]} {name[1]}".format(name = full_name))

print("-" * 60)
import math
print(__name__)     # current module name __main__
print(math.__name__)

print("The {mod.__name__} module gives the value of pi={mod.pi}  and Eulers constant {mod.e}".format(mod=math))
