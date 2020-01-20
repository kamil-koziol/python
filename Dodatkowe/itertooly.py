import itertools

counter = itertools.count(start=5, step=5)  # infinite from 5,10,15....

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# data = [100, 200, 300, 400]
# # kiedy data jest długie
# daily_data = list(zip(itertools.count(), data))
# print(daily_data)


# cycler = itertools.cycle([1,2,3])
#
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))

# counter = itertools.repeat(2, times=3)
#
# squares = map(pow, range(10), itertools.repeat(2))
# print(list(squares))

letters = ["a", 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

result = itertools.combinations(letters, 2)
# itertools.permutations są (a,b) i (b,a) w combinations nie
print(list(result))

result2 = itertools.product(numbers, repeat=4)
print(list(result2))

result3 = itertools.combinations_with_replacement(numbers, 4)
print(list(result3))

combined = letters + numbers + names
combined2 = itertools.chain(letters, numbers, names)

for item in combined2:
    print(item)

result4 = itertools.islice(range(10), 1, 5, 2)  # start, stop, step

selectors = [True, True, False, True]

result5 = itertools.compress(letters, selectors)
for item in result5:
    print(item)
