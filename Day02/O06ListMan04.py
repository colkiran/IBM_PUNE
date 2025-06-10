"""
sort   - will sort the original list
sorted - will sort a copy of the list
"""

print("sort".center(60, "-"))
l1 = [8, 5, 10, 6, 9, 1, 4, 7, 2, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"res_asc :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"res_desc :{res_desc}")

print("-" * 60)
l1 = [8,'zebra', 'apple', 5, 'yellow', 'xray', 10, 'white', 'blue', 6, 9, 'purple', 'green',  1, 'car', 'egg', 4,
      'hen', 7, 2, 3, 160, 1879, 29, 230, 2740]
print(f"l1 :{l1}")

res = sorted(l1, key = ascii)
print(f"res :{res}")

for i in range(0, len(res)):
    if type(res[i]) == int:
        print(i)
        break

print(res[:i] + sorted(res[i:]))
l1.so