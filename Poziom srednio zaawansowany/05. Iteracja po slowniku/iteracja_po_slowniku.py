student = {
    'imie': 'Kamil',
    'nazwisko': 'Koziol',
    'klasa': 3,
    'wiek': 18
}

for key in student:
    print(key, "->", student[key])

for key, value in student.items():
    print(key, '->', value)
