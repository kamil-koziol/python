import MODULE as md  # IMPORTUJE CALY PLIK MODULE.py I WYKONUJE TO WSZYSTKO W TEJ KOMENDZIE CO TAM JEST ZMIENNE TEZ PRZECHODZA , ZAMIAST PISAC MODULE.find_index() PISZEMY md.find_index() , BO IMPORTUJEMY TO JAKO md

# import math - importuje cały moduł
# from math import * - importuje cały moduł, ale nie trzeba uprzedzać math.XYZ
# from math import pi - importuje tylko jedną rzecz z modułu

# MOZNA TEZ IMPORTOWAC KONKRETNA RZECZ NP : from MODULE import find_index I NIE MUSIMY WTEDY PISAC MODULE.  , TAK SAMO ZE ZMIENNYMI , JAK CHCEMY WSZYSTKO ZAIMPORTOWAC BEZ PISANIA POTEM MODULE. WPISUJEMY from MODULE import *

kursy = ['Matematyka', 'Informatyka', 'Historia', 'Biologia']

print(md.test)

print(md.find_index(kursy, 'Historia'))
