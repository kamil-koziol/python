from bs4 import BeautifulSoup
import requests
from typing import Tuple, List
import json

# class Populacja:
#     def __init__(self, men: int, women: int):
#         self.men = men
#         self.women = women

# class Wspolrzedne:
#     def __init__(self, szerokosc: float, wysokosc: float):
#         self.szerokosc = szerokosc
#         self.wysokosc = wysokosc

# class Miasto:
#     def __init__(self, nazwa: str, populacja: Populacja, powiat: str, wojewodztwo: str, wspolrzedne: Wspolrzedne, powierzchnia: float, tablice: Tuple[str], prezydent: str):
#         self.nazwa = nazwa
#         self.population = populacja
#         self.powiat = powiat
#         self.wspolrzedne = wspolrzedne
#         self.powierzchnia = powierzchnia
#         self.tablice = tablice
#         self.prezydent = prezydent
    
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, ensure_ascii=False)

with open("miasta.html", "r") as f:
    source = f.read()

soup = BeautifulSoup(source, "html.parser")
rows = soup.tbody.find_all("tr")

miasta = []

# SCRAPING
for row in rows:
    columns = row.find_all("td")
    _miasto = {}
    _miasto["name"] = columns[1].a.text
    _miasto["nazwa_uri"] = columns[1].a["href"]

    _miasto["population"] = {
        "total": int(columns[2].text.replace(" ","")),
        "men":int(columns[3].text.replace(" ","")), 
        "women": int(columns[4].text.replace(" ",""))
    }
    _miasto["powiat"] = columns[5].text
    _miasto["wojewodztwo"] = columns[6].a.text


    resp = requests.get(_miasto["nazwa_uri"])
    resp = BeautifulSoup(resp.text, "html.parser")

    # POLOZENIE
    polozenie = resp.find("div", {"id": "polozenie"})
    polozenie = polozenie.find_all("div")[1]
    polozenie = polozenie.li.find_all("span")
    _miasto["coordinates"] = {
        "lat": float(polozenie[0].text), 
        "lon": float(polozenie[1].text)
        }

    # POWIERZCHNIA, TABLICE, PREZYDENT
    powierzchnia = resp.find("div", {"class": "cp-main"})
    powierzchnia = powierzchnia.find_all("div")[1]
    powierzchnia = powierzchnia.find("div", {"class": "row"})
    powierzchnia = powierzchnia.div.ul.find_all("li")

    _miasto["area"] = None
    _miasto["plates"] = None
    _miasto["president"] = None

    for li in powierzchnia:
        if "Powierzchnia" in li.text:
            _miasto["area"] = float(li.span.text[:-4].replace(",",".").replace(" ",""))
        if "Tablice rejestracyjne" in li.text:
            _miasto["plates"] = li.span.text.split(", ")
        if "Prezydent miasta" in li.text or "Burmistrz miasta" in li.text:
            _miasto["president"] = li.span.text

    del _miasto["nazwa_uri"]

    miasta.append(_miasto)
    print(len(miasta))

with open ("text.json","w",encoding="utf-8") as f:
    f.write(json.dumps(miasta, ensure_ascii=False))



