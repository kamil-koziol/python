import csv
import random
import json
from datetime import date

def deletePolishLetters(word: str):
        return word.replace("ą","a").replace("ć","c").replace("ł", "l").replace("ó","o").replace("ę", "e").replace("ń", "n").replace("ż", "z").replace("ź", "z").replace("ś", "s")


class RandomPerson:
    def __init__(self):
        self.name = self.getRandomName()
        self.surname = self.getRandomSurname()
        self.city = self.getRandomCity()
        self.dateOfBitrh: date = str(self.getRandomDate())
        self.income = random.randint(1000, 30000)
        self.mail = deletePolishLetters(self.name.lower() + "." + self.surname.lower() + self.dateOfBitrh[:4] + "@gmail.com")

    @staticmethod
    def getRandomName() -> str:
        return random.choices(names, weights=namesWeights)[0]

    @staticmethod
    def getRandomSurname() -> str:
        return random.choices(surnames, weights=surnamesWeights)[0]
    
    @staticmethod
    def getRandomCity():
        return random.choices(miasta, weights=miastaWeights)[0]["name"]
    
    @staticmethod
    def getRandomDate() -> date:
        return date(random.randint(1950,2020), random.randint(1,12), random.randint(1,28))

with open("data/imiona.csv", "r") as f:
        reader = csv.reader(f)
        records = [i for i in reader]
        names = [record[0].title() for record in records]
        namesWeights = [int(record[2]) for record in records]

with open("data/nazwiska.csv", "r") as f:
        reader = csv.reader(f)
        records = [i for i in reader]

        surnames = [record[0].title() for record in records]
        surnamesWeights = [int(record[1]) for record in records]

miasta = json.loads(open("data/miasta.json").read())
miastaWeights = [miasto["population"]["total"] for miasto in miasta]

del records
