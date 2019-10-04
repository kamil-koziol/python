var_x = 10

password = "My password"

source = "password"

globalne = globals().copy()
del globalne['password']

result = eval(source, globalne)
print(result)
