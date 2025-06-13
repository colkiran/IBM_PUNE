


import re

st = "myfile.py"


res = re.search(r'\.py$', st)

if res:
    print("Match found...")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found...")