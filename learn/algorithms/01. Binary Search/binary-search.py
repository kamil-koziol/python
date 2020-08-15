import random

lista = []
for _ in range(1000):
    losowa_liczba = random.randint(0,50) # losowa liczba z zakresu 0-50
    lista.append(losowa_liczba)

lista.sort() # sortujemy, ponieważ binary_search działa tylko na posortowanych listach

def binary_search(arr, num):
    start = 0 # pierwszy element listy
    end = len(arr) - 1 # ostatni element listy

    while start <= end:
        half = (start + end)//2 # dzielimy na pół listę
        if num < arr[half]:
            end = half - 1 # skracamy listę od prawej
        elif num > arr[half]:
            start = half + 1 # skracamy listę od lewej
        elif arr[half] == num:
            return half
    return None
      
print(binary_search(lista, 25))

if lista[binary_search(lista, 25)] == 25:
    print("Udało się!")