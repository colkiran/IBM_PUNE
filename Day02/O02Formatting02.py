# Conversions
print("Conversion".center(60,"-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=368234723))

print("-" * 60)
print("{num:15} Tendulkar".format(num=3))
print("{num:15} Tendulkar".format(num="Sachin"))
print("{num:>15} Tendulkar".format(num="Sachin"))       #right align
print("{num:^15} Tendulkar".format(num="Sachin"))       #center align
print("{num:<15} Tendulkar".format(num="Sachin"))       #left align

print("-" * 60)
print("{:.6}".format("Sachin Tendulkar"))

from math import pi, e
print("{pi:10.2}".format(pi = 13.1))
print("{pi:10.3}".format(pi = pi))
print("{pi:10.4}".format(pi = pi))
print("{pi:10.5}".format(pi = pi))

print("-" * 60)
print("{pi:10.3}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=3.145635345))

print("-" * 60)
print("{:-^60}".format("Sachin"))
print("Sachin".center(60,"-"))

print("-" * 60)
print("{0}\n{1}".format(pi, e))
print("{0:.2}\n{1:.2}".format(pi, e))


