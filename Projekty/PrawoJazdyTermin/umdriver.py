from selenium import webdriver
import time
from datetime import date
from typing import List

class UMDriver(webdriver.Firefox):

    URI = "https://rezerwacja.um.torun.pl/#/"

    def __init__(self, options, DAYA=1, DAYB=31):
        super().__init__(options=options)
        self.SLEEP_TIME = 3
        self.DAY_AFTER = DAYA
        self.DAY_BEFORE = DAYB

    @staticmethod
    def month_days(month: int) -> int:
        DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
        return DAYS[month-1]
    
    def get_days(self) -> List[int]:

        self.get(UMDriver.URI)

        steps = [
        r'//*[@id="app"]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/button[2]',
        r'//*[@id="app"]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/button[2]'
            ]
            
        for xpath in steps:
            time.sleep(self.SLEEP_TIME)
            search = self.find_element_by_xpath(xpath)
            search.click()

        time.sleep(self.SLEEP_TIME)
        daty = self.find_elements_by_class_name("v-btn--disabled")
        daty.pop(0)
        print(daty)

        days_in_current_month = UMDriver.month_days(date.today().month)
        wolne_dni = [i for i in range(1, days_in_current_month)]

        for data in daty:
            wolne_dni.remove(int(data.text))

        return wolne_dni

    def check_days(self, free_days: List[int]) -> List[int]:
        days = []
        for day in free_days:
            if day >= self.DAY_AFTER and day <= self.DAY_BEFORE:
                days.append(day)
        return days
