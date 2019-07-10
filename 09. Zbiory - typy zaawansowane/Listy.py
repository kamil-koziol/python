lista = [1, 2, 3, "JAN", "KAMIL"]

lista[0] = "KUBA"  # ZAMIENIA 1 ELEMENT NA DANY (KUBA)

print(lista[0])  # POKAZUJE 1 ELEMENT LISTY

print(lista[-1]) # POKAZUJE 1 OD KONCA

lista.append(1)  # DODAJE NA SAM KONIEC DANA DANĄ
print(lista)

lista.insert(2, "JAKUB")  # DODAJE NA DANE MIEJSCE DANĄ DANĄ
print(lista)

lista.remove("KAMIL")  # USUWA DANĄ DANĄ Z LISTY
print(lista)

lista.reverse()  # ODWRACA LISTE
print(lista)

print(lista.pop(0))  # USUWA DANY MIEJSCE LISTY I GO WYSWIETLA
print(lista)

print(lista.index("JAN"))  # POKAZUJE MIEJSCE NA LISCIE DANEJ DANEJ

print(lista.count("KAMIL"))  # WYPISUJE ILE RAZY WYSTEPUJE TO NA LISCIE

lista2 = ["MARCIN", "PATRYK"]

lista.extend(lista2)  # POSZERZA DANĄ LISTE DANĄ LISTĄ (GDYBY APPEND TO BYLA BY TABLICA W TABLICY)
print(lista)

listaKopia = lista.copy()  # TWORZY KOPIĘ DANEJ LISTY (NIE ZADZIALA SAMO NAPISANIE list)

lista.clear()  # WYCZYSZCZA DANĄ LISTĘ
print(lista)

print(listaKopia)

kursy = ["Historia", "Matematyka", "Fizyka", "Informatyka"]

kursy_str = ', '.join(kursy)  # ZAMIANA TABLICY NA STR , ', ' - ROZDZIELACZ MIEDZY NIMI
print(kursy_str)

nowa_lista = kursy_str.split(', ')  # ZAMIANA STR NA TABLICE , ', ' - ROZDZIELA NA FRAGMENTY
print(nowa_lista)

cyfry = [2, 5, 3, 4, 1]

cyfry.sort()  # SORTUJE OD NAJMNIEJSZEJ DO NAJWIEKSZEJ (SORTUJE ALFABETYCZNIE W PRZYPADKU STR)
print(cyfry)

cyfry.sort(reverse=True)  # SORTUJE OD NAJWIEKSZEJ DO NAJMNIEJSZEJ (SORTUJE ALFABETYCZNIE W PRZYPADKU STR)
print(cyfry)

print(max(cyfry))  # POKAZUJE MAX WARTOSC

print(min(cyfry))  # POKAZUJE MINIMALNA WARTOSC

print(sum(cyfry))  # POKAZUJE SUME

c = input("\nPRESS ENTER TO CONTINUE...")
