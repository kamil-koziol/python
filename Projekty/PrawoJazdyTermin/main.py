from selenium.webdriver.firefox.options import Options
from umdriver import UMDriver

options = Options()
options.headless = True

driver = UMDriver(options)
free_days = driver.get_days()
searched_dates = driver.check_days(free_days)
print(searched_dates)




