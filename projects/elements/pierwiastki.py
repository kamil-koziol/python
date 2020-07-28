elements = []
with open(r"elements.txt", "r") as f:
    for line in f:
        elements.append(line.strip())

word = input("Give a Word: ")

def elementsName(name: str, curr_words, check_one:bool):
    if(len(name) <= 0):
        print(curr_words)
        return True
    
    if name[:1].capitalize() in elements and check_one:
        curr_words.append(name[:1])
    elif name[:2].capitalize() in elements and not check_one:
        curr_words.append(name[:2])
    else:
        return False
    

    elementsName(name[1:], curr_words, True)
    if(len(name) >=2):
        elementsName(name[2:], curr_words, False)

elementsName(word, [], True)
elementsName(word, [], False)