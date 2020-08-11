import csv
import random

with open("imiona.csv", "r") as f:
    reader = csv.reader(f)
    names = [i for i in reader]

with open("nazwiska.csv", "r") as f:
    reader = csv.reader(f)
    nazwiska = [i for i in reader]

def getRandomNames(count: int):
    return random.choices([name[0].title() for name in names], weights=[int(count[2]) for count in names], k=count)

def getRandomSurnames(count: int):
    return random.choices([name[0].title() for name in nazwiska], weights=[int(count[1]) for count in nazwiska], k=count)

print(getRandomSurnames(100))