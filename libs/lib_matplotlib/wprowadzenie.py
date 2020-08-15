import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

#pd.read_csv("01. Moduł matplotlib/pokemon.csv")


#maxQuad = 100
#plt.plot(list(range(maxQuad)),[i**2 for i in range(maxQuad)])

# dokladnosc = 10000
# totalRange = [i/dokladnosc for i in range(-10 * dokladnosc, 10 * dokladnosc +1)]

#t = np.arange(-5.,5.,0.01)
# arange(poczatek,koniec,krok) dodajemy . jesli float

# plt.plot(t, t**2)
# plt.ylabel("LICZBY")
# plt.show()

#plt.plot(t,t,'r--', t, t**2, 'bs', t, t**3, 'g^')
# 3 wykresy
# r - red , b - blue, g - green, -- - linie, s - square, ^ - trojkat
#plt.show()

x = np.arange(0., 3*math.pi, 0.01)
print(type(x))
y = [math.sin(i) for i in x]
plt.plot(x,y)
plt.show()