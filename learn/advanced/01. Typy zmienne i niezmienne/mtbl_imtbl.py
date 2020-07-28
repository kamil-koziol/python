# immutable
num = 10
print("Variable num:",num,id(num))
num += 2
print("Variable num:",num,id(num))

# immutable
text = "Africa"
print("Variable text:",text,id(text))
text += "is hot"
print("Variable text:",text,id(text))

# mutable
lista = [1,2,3]
print("Variable list: ", lista, id(lista))
lista.append(4)
print("Variable list: ", lista, id(lista))

lista2 = lista
lista2.append(5)
print("Variable list: ", lista, id(lista))
print("Variable list2: ", lista2, id(lista2))

# poprawny sposob
lista3 = lista.copy()


# ZADANIE
days = ['mon','tue','wed','thu','fri','sat','sun']
workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print(workdays)

