import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

primes = (2,3,5,7,11,13,17,19)
seria2 = pd.Series(primes)
print(seria2)

Spielberg = {
    'Jaws': 1975,
    '1941':1979,
    'Indiana Jones':1981,
    'E.T':1982
    }

seria3 = pd.Series(Spielberg)
print(seria3)

cities = ['London', 'Warsaw', 'Paris', 'Berlin']
seria = pd.Series(cities)
print(seria)

print(seria.size) # wielkosc
print(seria.nbytes) # wielkosc w MB
print(seria.is_monotonic)
print(seria.index)
print(seria.values)
print(seria.dtype)

monotonicList = [1,5,9,11,12,23,89,142]
mSeria = pd.Series(monotonicList)
print(mSeria.sum())
print(mSeria.min())
print(mSeria.max())
print(mSeria.mean()) # srednia
print(mSeria.product()) # mnozy wszystkie przez siebie
print(mSeria.add(10)) # doda do kazdego elementu 10
print(mSeria.index)