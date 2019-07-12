import datetime

data = datetime.date(2018, 7, 12)  # WYŚWIETLA DATĘ W POSTACI "2018-07-12"
print(data)
print("--------------------------------------------")

tday = datetime.date.today()
print(tday)  # WYŚWIETLA DZISIEJSZĄ DATĘ
print(tday.year)  # WYŚWIETLA OBECNY ROK
print(tday.month)  # WYŚWIETLA OBECNY MIESIĄC
print(tday.day)  # WYŚWIETLA OBECNY DZIEŃ
print(tday.isoweekday())  # WYŚWIETLA NUMER DNIA TYGODNIA : PON = 1 , ND = 7
print("--------------------------------------------")

# WYZNACZA ILOŚĆ DNI DO DODANIA/ODJĘCIA OD DATY
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)  # WYŚWIETLA TYDZIEŃ PO
print(tday - tdelta)  # WYŚWIETLA TYDZIEŃ PRZED
print("--------------------------------------------")

# date2 = date1 + timedelta
# timedelta = date1 + date2

new_year = datetime.date(tday.year + 1, 1, 1)  # DATA DO NOWEGO ROKU

till_newyear = new_year - tday
print(till_newyear)  # WYŚWIETLA CZAS DO NOWEGO ROKU
print(till_newyear.total_seconds())  # WYŚWIETLA ILE SEKUND DO NOWEGO ROKU
print("--------------------------------------------")
print("--------------------------------------------")

t = datetime.time(9, 30, 45, 100000)  # time(hour, minute, second, microsecond)
print(t)
print(t.hour)

print("--------------------------------------------")

# year, month, day, hour, minute, second, microsecond
dt = datetime.datetime(2018, 7, 12, 15, 45, 10, 100000)
print(dt)  # DATA Z CZASEM
print(dt.year)  # ROK
print(dt.date())  # DATA
print(dt.time())  # CZAS
print("--------------------------------------------")

tdelta = datetime.timedelta(hours=14)
print(dt + tdelta)
print("--------------------------------------------")

dt_today = datetime.datetime.today() #CZAS LOKALNY
dt_now = datetime.datetime.now() #CZAS LOKALNY LUB MOZEMY ZMIENIĆ STREFĘ CZASOWĄ
dt_utcnow = datetime.datetime.utcnow() #CZAS UTC

print(dt_today)
print(dt_now)
print(dt_utcnow)
print("--------------------------------------------")

import pytz

dt = datetime.datetime(2018,7,12,12,30,45,tzinfo = pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz = pytz.UTC)
print(dt_utcnow)

dt_war = dt_utcnow.astimezone(pytz.timezone("Europe/Warsaw")) #LISTA STREF CZASOWYCH :
#pytz.all_timezones
print(dt_war)

dt = datetime.datetime.today()
print(dt.strftime('%B %d, %Y - %A'))

dt_str = 'December 28, 2018 - Friday'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y - %A')
print(dt)






