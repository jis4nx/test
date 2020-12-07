print("Hello World")
import requests

res = requests.get("http://www.python.org")
print(res.status_code)
