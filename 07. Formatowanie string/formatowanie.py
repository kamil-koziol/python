message = "Proccesing file {0:s}"
print(message.format("file1.txt"))

message2 = "File {0:s} has size {1:d}"
print(message2.format("file1.txt",100))

message3 = "File {1:s} has size {0:d}"
print(message3.format(100,"file1.txt"))

message4 = "file {0:20s} has size {1:10d}"
print(message4.format("file1.txt",100))

# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))


# DODATKOWE ATRYBUTY DO FORMAT

"""
d	| Decimal integer
c	| Corresponding Unicode character
b	| Binary format
o	| Octal format
x	| Hexadecimal format (lower case)
X	| Hexadecimal format (upper case)
n	| Same as 'd'. Except it uses current locale setting for number separator
e	| Exponential notation. (lowercase e)
E	| Exponential notation (uppercase E)
f	| Displays fixed point number (Default: 6)
F	| Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
g	| General format. Rounds number to p significant digits. (Default precision: 6)
G	| Same as 'g'. Except switches to 'E' if the number is large.
%	| Percentage. Multiples by 100 and puts % at the end.
"""

template =  "Hello {0}, your balance is {1:9.3f}"
print(template.format("Adam", 230.23463))

# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))

# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters
# and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letters,
# padding and center alignment
print("{:^5.3}".format("caterpillar"))

person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print("1. ", sentence)

sentence = 'My name is {} and I am {:03} years old.'.format(person['name'], person['age'])
print("2. ", sentence)


sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print("3. ", sentence)


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print("4. ", sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print("5. ", sentence)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print("6. ", sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print("7. ", sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print("8. ", sentence)

for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)


pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)

print("9. ", sentence)


sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)

print("10. ", sentence)

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

print("11. ", my_date)

sentence = '{:%B %d, %Y}'.format(my_date)

print("12. ", sentence)

input()
