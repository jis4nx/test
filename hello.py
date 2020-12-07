print("Hello World")
import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.python.org")
print(res.status_code)
soup = BeautifulSoup(res, "lxml")
