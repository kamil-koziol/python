from utils.database import Database
from utils.hasher import Hasher
from utils.user import User
from utils.qrcoder import QRCoder
from utils.totper import TOTPer
from utils.persongen import RandomPerson

import webbrowser

import random
import csv
from tqdm import tqdm

database = Database()
# database.reset()


def addRandomUsers(amount: int):
    for i in tqdm(range(amount)):
        p = RandomPerson()
        randomSecretKey = Hasher.randomSecretKey()
        user = User(p.mail, p.name, p.surname, p.city, p.dateOfBitrh, p.income, randomSecretKey)
        database.addUser(user)


# addRandomUsers(100_000)

# database.addUser(User("panpouran@gmail.com", "Kamil", "K", "Warszawa", "2020-01-01", 120, Hasher.randomSecretKey()))
user = database.getUser("panpouran@gmail.com")
print(user.city)
database.close()
# user = database.getUser("panpouran@gmail.com")
# userTOTP = TOTPer(user)

# qrcodeURL = QRCoder.generate(userTOTP.getURL())
# webbrowser.open(qrcodeURL)

# password = input("Haslo: ")
# passwordsMath = Hasher.checkPassword(password, user.password)
# if passwordsMath:
#     totp = int(input("TOTP: "))
#     if userTOTP.checkCode(totp):
#         print("ZALOGOWANO")
