# PRZYMIOTNIK + RZECZOWNIK + CZASWONIK + RZECZOWNIK
import random


def losoweSlowo(plik):
    slowa = []
    with open(plik, "r") as f:
        slowa = f.readlines()
    return random.choice(slowa).strip()


print(losoweSlowo("przymiotniki.txt") + " " + losoweSlowo("rzeczowniki.txt"))
