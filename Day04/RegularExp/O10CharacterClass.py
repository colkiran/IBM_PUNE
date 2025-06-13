


import re

st = "bbt"

# res = re.match(r'b[a-zA-Z0-9]t', st)
# res = re.match(r'b[aeiou]t', st)
res = re.match(r'b[^aeiou]t', st)

if res:
    print("Match found...")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found...")