kursy = {'Historia', 'Matematyka', 'Fizyka', 'Informatyka', 'Matematyka'}
kursy2 = {'WF', 'Matematyka', 'Sztuka', 'Informatyka', 'Matematyka'}
print(kursy)

# WARTOSCI CIAGLE ZMIENIAJA POLOZENIE
# USUWAJA DUPLIKATY

print("Matematyka" in kursy)  # NAJSZYBCIEJ ZE WSZYSTKICH DZIALA

print(kursy.intersection(kursy2))  # POKAZUJE WSPOLNE WARTOSCI
print(kursy.difference(kursy2))  # POKAZUJE ROZNICE
print(kursy.union(kursy2))  # ŁĄCZY 2 SETY

# pusty_set = {}  # TO NIE SET
pusty_set = set()  # POPRAWNE

pusty_set.add(4)

# print(help(set))
