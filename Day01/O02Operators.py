
# arithmetic
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")   # floor div
print(f"10 % 3 = {10 % 3}")
print(f"10 ** 3 = {10 ** 3}")

print("Augmentor Operator".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, >, <, <=, >=
x = 5
y = 3
print(f"x == y :{x == y}")
print(f"x >= y :{x >= y}")
print(f"x != y :{x != y}")

print("logical Operators".center(60, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")

print("-" * 60)
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")

print("-" * 60)
print(f"not(1 == 1 and 2 == 1) :{not(1 == 1 and 2 == 1)}")
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
# integer representation of unicode characters
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")
print(f"ord('A) :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("-" * 60)
print(f"97 :{chr(97)}")
print(f"122 :{chr(122)}")
print(f"65 :{chr(65)}")
print(f"90 :{chr(90)}")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")
print(f"~0 :{~0}")
print(f"~5 :{~5}")

print("ternary".center(60, "-"))
age = 19
print("Eligible" if age > 17 else "Not Eligible")