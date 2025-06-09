
st = "Hello World"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f'st :{st}')
print(f"st[0] :{st[0]}")            # stored like an array
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing using indexes
print(f"st[0:5] :{st[0:5]}")
print(f'st[6:11] :{st[6:11]}')
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f'st[0:]   :{st[:11]}')
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]   :{st[-1::-1]}")
print(f"st[:-12:-1 :{st[:-12:-1]}")
print(f"st[::-1] :{st[::-1]}")

print("-" * 60)
# code to check if a string is a palindrome
st = "malayalam"
print("Palindrome" if st[:] == st[::-1] else "Not a Palindrome")

print("-" * 60)
# STRINGS ARE IMMUTABLE
st = 'hello world'
print(f"st :{st}")
print(f"st[0] :{st[0]}")
# st[0] = "H"

print("-" * 60)
# print(dir(st))
st = "hello"
print(f"st: {st}")
res = st.replace("h", "H")
print(res)

print("-" * 60)
st = "hello world"
print(f"st :{st}")
res = st.replace("l", "L")
print(res)

res = st.replace("l", "L", 2)
print(res)

print("-" * 60)
# maketrans, translate
st = "hello world"
print(f"st :{st}")
a = 'helowrd'
b = 'HELOWRD'
# length of a and b should be same
resTbl = st.maketrans(a, b)
print(resTbl)

res = st.translate(resTbl)
print(res)
