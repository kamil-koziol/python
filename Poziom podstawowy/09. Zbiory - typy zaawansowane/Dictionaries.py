
student = {'imie': 'Kamil', 'nazwisko': 'Kozioł', 'wiek': '17', 'kursy': ["Python", "C++"]}
print(student)

print(student['imie'])

print(", ".join(student['kursy']))

print(student.get('imie'))

print(student.get('nr_telefonu'))  # ZWRACA NONE JEZELI NIE MA

print(student.get('nr_telefonu', "Nie znaleziono!"))  # ZWRACA NIE ZNALEZIONO JEZELI NIE ZNALEZIONO

student['nr_telefonu'] = '555-555'
print(student.get('nr_telefonu'))

student['imie'] = 'Kuba'
print(student)

student_update = {'imie': 'Jakub', 'nazwisko': 'Łotysz', 'wiek': '16'}
student.update(student_update)  # ZMIENIA DANE WARTOSCI LUB DODAJE KOLEJNE
print(student)

del student['wiek']  # USUWA DANA WARTOSC
print(student)

kursy = student.pop('kursy')
print(kursy)
print(student)

print(len(student))  # DLUGOSC
print(student.keys())  # ZWRACA KLUCZE
print(student.values())  # ZWRACA WARTOSCI KLUCZY
print(student.items())  # ZWRACA WSZYSTKIE PRZEDMIOTY

for key, value in student.items():
    print(key, ":", value)
