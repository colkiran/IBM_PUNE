
a = 10
b = -10

print(f"a :{a}")    # f string for interpolation
print(type(a))      # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.5
d = -10.5

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 10 + 2j
h = 10 - 2j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)

print(2 + 3.5)

x  = 2
y = 3.5
z = x + y

print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(11)       # decimal
print(0b11)     # binary
print(0b101)       # binary
print(0o11)     # octal
print(0o111)    # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(f"a :{a}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
print(f"bin(a) :{bin(a)}")
