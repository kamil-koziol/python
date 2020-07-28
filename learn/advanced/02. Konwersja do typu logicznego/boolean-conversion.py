# INTERPRETACJA STRING

isOk = 'LOSOWY NAPIS INTERPRETOWANY JAKO TRUE'
print("Variable isOk:",isOk,type(isOk))
if isOk:
  print("TRUE")

# string pusty interpretowany jako FALSE
isOk = ''
print("Variable isOk:",isOk,type(isOk))
if isOk:
  print("TRUE")

# INTERPRETACJA LICZB

# JEŚLI RÓŻNA OD ZERA TO TRUE
isOk = 1
print("Variable isOk:",isOk,type(isOk))
if isOk:
  print("TRUE")

# 0 = False
isOk = 0
print("Variable isOk:",isOk,type(isOk))
if isOk:
  print("TRUE")

# INTERPRETACJA LIST

# TRUE
isOk = [1,2,3]
print("Variable isOk:",isOk,type(isOk))
if isOk:
  print("TRUE")

# FALSE
isOk = []
print("Variable isOk:",isOk,type(isOk))
if isOk:
  print("TRUE")

