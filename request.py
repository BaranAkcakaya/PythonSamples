import requests
import json 

res = requests.get("https://jsonplaceholder.typicode.com/todos")
res = res.text
print(res)
res = json.loads(res)
print(res)