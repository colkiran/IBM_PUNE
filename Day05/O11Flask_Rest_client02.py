
import requests

BASE = "http://127.0.0.1:5000/"

resp = requests.get(BASE + "getproduct/pepsi")

print(resp)

res = resp.json()
print(res)

print("-" * 60)
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
