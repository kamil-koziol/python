listA = list(range(0, 5))
listB = list(range(0, 5))

products = []
for a in listA:
    for b in listB:
        products.append((a, b))

# ekwiwalent
products2 = [(a, b) for a in listA for b in listB]

# print(products)
# print(products2)

products3 = [(a, b) for a in listA for b in listB if a % 2 == 0 and b % 2 == 1]
print(products3)

# dict
products4 = {a: b for a in listA for b in listB if a % 2 == 0 and b % 2 == 1}
print(products4)