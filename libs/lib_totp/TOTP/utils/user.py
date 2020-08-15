from datetime import date

class User:
    def __init__(self, email:str, name: str, surname: str, city: str, dateOfBirth: str, income: int ,secretKey: str):
        self.email = email
        self.name = name
        self.surname = surname
        self.city = city
        self.dateOfBitrh: date = dateOfBirth
        self.income = income
        self.secretKey = secretKey