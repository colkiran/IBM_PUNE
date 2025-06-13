import json

import requests

BASE = "http://127.0.0.1:5000/"

resp = requests.get(BASE + "getproduct/pepsi")

print(resp)
res = resp.json()
print("-" * 60)
print("-" * 60)
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("PUT".center(60, "-"))

resp = requests.put(BASE + "getproduct/coke", data={'cat' :'bevarage'})
res = resp.json()

print(res)

print("POST".center(60, "-"))
fanta = {'item' :'200 ml bottle', 'price' :20, 'qty' :400}

resp = requests.post(BASE + "getproduct/fanta", json=json.dumps(fanta))
res = resp.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print()

print("PATCH".center(60, "-"))
data = {'price' :5000}

resp = requests.patch(BASE + "getproduct/coke", json=json.dumps(data))
res = resp.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("DELETE".center(60, "-"))

resp = requests.delete(BASE + "getproduct/thumbs_up")
res = resp.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print()