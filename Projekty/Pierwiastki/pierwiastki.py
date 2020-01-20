elements = []
with open(r"Pierwiastki\elements.txt", "r") as f:
    for line in f:
        elements.append(line.strip())

input()
word = input("Give a Word: ")

fullName = ""
for i, letter in enumerate(word):
    if i != len(word) - 1:
        if letter.upper() in elements or (letter.upper() + word[i+1].lower()) in elements:
            if (letter.upper() + word[i+1].lower()) in elements:
                fullName += letter.upper() + word[i+1].lower()
            else:
                fullName += letter.upper()
    else:
        if letter.upper() in elements:
            fullName += letter.upper()

print(fullName)