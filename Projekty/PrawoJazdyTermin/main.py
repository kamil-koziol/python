from selenium.webdriver.firefox.options import Options
from umdriver import UMDriver
from datetime import date

options = Options()
options.headless = True

# driver = UMDriver(options)
# free_days = driver.get_days()
# searched_dates = driver.check_days(free_days)
# print(searched_dates)

days_in_current_month = UMDriver.month_days(date.today().month)
wolne_dni = [i for i in range(1, days_in_current_month)]
print(wolne_dni)




