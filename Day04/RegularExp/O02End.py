
import re

# print(dir(re))

st = "hello world"

# print(f"st :{st}")
# if the string starts with hello

res = re.search(r'world$', st)

print(f"res :{res}")

if res:
    print("Match found...")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found...")