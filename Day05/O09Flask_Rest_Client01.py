
import requests

BASE = "http://127.0.0.1:5000/"

resp = requests.get(BASE + "helloworld")

# print(resp)

res = resp.json()

print(res)
