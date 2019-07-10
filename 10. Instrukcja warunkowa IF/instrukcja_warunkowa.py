language = "Python"

if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Python")
else:
    print("Something went wrong...")

num_1 = 13
num_2 = 38

if num_1 == num_2:
    print("The Same")
else:
    print("Not the same")

logged_in = True
user = "Admin"

if user == "Admin" and logged_in:
    print("Hello")

if not logged_in:
    print("Not logged in")
else:
    print("Logged in")

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

if a == b:
    print("a=b")

if a is b:
    print("a is b")
else:
    print("a is not b")
###
a = b = [1, 2, 3, 4, 5]

if a is b:
    print("a is b")
else:
    print("a is not b")

if id(a) == id(b):  # ROBI TO SAMO CO is
    print("a is b")
else:
    print("a is not b")

input()