def goLeft(*args):
    print("Going left with", *args, ",then")

def goRight(*args):
    print("Going right with", *args, ",then")

def goUp(*args):
    print("Going up with", *args, ",then")

def goDown(*args):
    print("Going down with", *args, ",then")

instructions = [goLeft, goRight, goLeft, goUp, goLeft, goDown]

for instr in instructions:
    instr("PIZZA")