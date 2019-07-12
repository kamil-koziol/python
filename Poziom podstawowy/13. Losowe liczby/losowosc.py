import random

# losowa liczba z zakresu od 1 do 100
randNum = random.randint(1,100) # 1 <= randNum <= 100 
print(randNum)

# wybieranie losowej pozycji z listy
imiona = ["Kamil","Kuba","Marcin","Patryk"]
losoweImie = random.choice(imiona)
print(losoweImie)

# stworzenie losowej listy z liczbami od 1 do 9 z 20 elementami
lista1 = []
for _ in range(20):
  lista1.append(random.randint(1,9))

# skrócona wersja
lista2 = [random.randint(1,9) for _ in range(20)]
# ^ o tym zapisie więcej w # DOTATKOWE MATERIAŁY, COMPREHENSIONS

# utworzenie listy 1,2,3....,20
lista3 = list(range(1,21))

# mieszanie listy
print(random.shuffle(lista3))

# losowy float
print(random.random())