from bs4 import BeautifulSoup
import requests

req = requests.get("http://coreyms.com")

if req.status_code != 200:
    print("Nie znaleziono strony")
else:
    source = req.text

# print(source)

soup = BeautifulSoup(source, 'lxml')
