

wiadomosc = "Hello World"

print(wiadomosc)  # POKAZUJE WIADOMOŚĆ

wiadomosc2 = 'Bobby\'s World'  # UZYWAMY \ ZEBY WYSWIETLIC '

print(wiadomosc2)

print(len(wiadomosc))  # POKAZUJE DŁUGOŚĆ WIADOMOSCI

print(wiadomosc[0])  # POKAZUJE 1 WARTOSC STR

print(wiadomosc[:5])  # POKAZUJE WSZYSTKO DO 5 WARTOSCI

print(wiadomosc[6:])  # POKAZUJE WSZYSTKO OD 6 DO KONCA

print(wiadomosc[3:7])  # POKAZUJE WSZYSTKO OD 3 DO 7

print(wiadomosc.lower())  # ZAMIENIA NA MALE

print(wiadomosc.upper())  # ZAMIENIA NA DUZE

print(wiadomosc.title())  # ZAMIENIA PIERWSZE NA DUZE (AMERYKANSKI TYTUL)

print(wiadomosc.endswith("rld")) # POKAZUJE CZY KOŃCZY SIĘ NA rld 

print(wiadomosc.count("l"))  # POKAZUJE ILE JEST CZEGOS W TYM

print(wiadomosc.find("World"))  # POKAZUJE NA JAKIM MIEJSCU JEST COS

wiadomosc = wiadomosc.replace("World", "Świat")  # ZAMIENIA 1 NA 2

print(wiadomosc)

imie = "Kamil"
nazwisko = "Kozioł"
wiek = 17

wiadomosc = "{:10} {} ma {} lat".format(imie, nazwisko.title(), wiek)  # WARTOSCI OD LEWEJ DO PRAWEJ SA WPISYWANE
print(wiadomosc)

wiadomosc2 = f"{imie.upper():10} {nazwisko.lower()} ma {wiek:.2f} lat"  # LEPSZY , MOZNA W TYM ROBIC NP UPPER
print(wiadomosc2)

wiadomosc = "{0:10} {1} {0}".format("<div>", "Hello World")
print(wiadomosc)

# print(help(str))

input()

