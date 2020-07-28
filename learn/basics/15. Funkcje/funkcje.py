def hello_func(greetings, name="Kamil"):  # JESLI DAMY = JEST TO DEFAULTOWA WARTOSC JESLI NIE PODAMY NICZEGO
    return f"{greetings} {name}!"


print(hello_func("Witaj"))  # DAJEMY DANE PO KOLEI

print(hello_func(name="Kuba", greetings="Witam"))  # NIE MUSIMY SIE TRZYMAC KOLEJNOSCI JESLI WSZEDZIE DAMY KEYWORDS

print(hello_func("Witaj", "Maciej").upper())  # FUNKCJA ZWRACA STR WIEC MOZNA ROBIC NA TYM OPERACJE


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Matematyka', "Informatyka", imie="Jan", wiek=18)  # KEYWORDY PRZYJMUJE JAKO kwargs , A WPISANE TAK O JAKO args, args TO TUPLE , a kwargs TO DICTIONARY

kursy = ['Matematyka', 'Informatyka']
info = {'imie': "JAN", 'wiek': '18'}

student_info(*kursy, **info)  # GDYBYSMY DALI BEZ GWIAZDEK TO BY NIE ROZPAKOWALO BY TYCH WARTOSCI ! I DALO BY JE JAKO ARGS , BO NIE BYLO BY KEYWORDS


# LICZBA DNI W MIESIĄCACH
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(rok):
    """ZWRACA True DLA PRZESTEPNYCH , False DLA NIE PRZESTEPNCYH ROKÓW"""

    # WARTO DAWAC """ """ ŻEBY WIADOME BYŁO CO ROBI FUNKCJA

    return rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0)


def days_in_month(rok, miesiac):
    """ZWRACA ILOŚĆ DNI W DANYM MIESIĄCU W DANYM ROKU"""

    if not 1 <= miesiac <= 12:
        return 'Invalid Month'

    if miesiac == 2 and is_leap(rok):
        return 29

    return month_days[miesiac]


print(days_in_month(2017, 2))
