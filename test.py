from bs4 import BeautifulSoup
import requests

res = requests.get("http://python.org")
soup = BeautifulSoup(res, "lxml")
matches = soup.find_all("div")
