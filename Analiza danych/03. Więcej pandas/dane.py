import pandas as pd

waluty = ["USD", "EUR", "PLN", "EUR"]
kraje = ["USA", "HISZPANIA", "POLSKA", "PORTUGALIA"]
curSeries = pd.Series(waluty, kraje)
print(curSeries)

monotonicList = [1, 5, 9, 11, 12, 23, 89, 142]

x = pd.Series(monotonicList)
print(x > 10)
print(x % 2)

print(x.where(x > 10).dropna())
print(x.filter(items=[0, 1, 2]))
print(x.where(x.between(1, 11)))
