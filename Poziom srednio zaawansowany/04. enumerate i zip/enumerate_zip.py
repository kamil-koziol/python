workDays = ["Pn", "Wt", "Śr", "Czw", "P"]

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)

for pos, value in enumeratedDays:
    print(pos, " -> ", value)

months = ['I', 'II', 'III', 'IV', 'V']
monthDays = list(zip(months, workDays))
print(monthDays)

for pos, value in monthDays:
    print(pos, " -> ", value)

for pos, (m, d) in enumerate(monthDays):
    print(pos, " -> ", m, " : ", d)
