from selenium.webdriver.firefox.options import Options
from umdriver import UMDriver
import time
import smtplib
import os

options = Options()
options.headless = True

searching = True
while searching:
    driver = UMDriver(options, 1, 29)
    free_days = driver.get_days()
    matching_dates = driver.check_days(free_days)
    if len(matching_dates) > 0:
        searching = False
        break

EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

receivers = ["panpouran@gmail.com", "patryk1wroblewski@wp.pl"]

with smtplib.SMTP('asprodukt.nazwa.pl', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    msg = "==== FOUND ====\n" + str(matching_dates)
    for receiver in receivers:
        smtp.sendmail(EMAIL_ADDRESS, receiver, msg)




