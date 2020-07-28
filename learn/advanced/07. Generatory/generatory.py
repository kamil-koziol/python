listA = list(range(0, 5))
listB = list(range(0, 5))

# używany gdy mamy dużą ilość danych do przetworzenia

gen = ((a, b) for a in listA for b in listB if a % 2 == 0 and b % 2 == 1)
print(gen)

print(next(gen))
print(next(gen))

print('-' * 30)
for x in gen:
    print(x)

print('-' * 30)
for x in gen:
    print(x)

print('-' * 30)
gen = ((a, b) for a in listA for b in listB if a % 2 == 0 and b % 2 == 1)
for x in gen:
    print(x)

