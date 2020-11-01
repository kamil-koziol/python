import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import csv

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

EMAIL_ADDRESS  = "asenso@asensosa.com"
EMAIL_PASSWORD = input()

HOST = 'smtp.asprodukt.nazwa.pl'
PORT = 587

mails = []

# user_nicename, user_email
# with open('mails.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for mail in reader:
#         mails.append((mail[0], mail[1]))


# mails = [('agnieszka','a.zaworska@asprodukt.com'), ('hiszpanpedro', 'd.pasturek@asprodukt.com'), ('admin', 'kamil.koziol@asprodukt.com')]


with smtplib.SMTP(HOST, 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for mail in mails:
        print('Sending mail to', mail)
        message = MIMEMultipart()
        message["Subject"] = "Dzień dobry! Mamy coś specjalnie dla Ciebie"
        message["From"] = f"ASENSO Saunowa Awangarda <{EMAIL_ADDRESS}>"
        message["To"] = mail[1]

        html = open('message.html', 'r', encoding='utf-8').read()
        html = html.replace('{{ user_profile_link }}', "https://asensosa.com/user/" + mail[0])
        mainPart = MIMEText(html, 'html', 'utf-8')
        message.attach(mainPart)
        smtp.sendmail(EMAIL_ADDRESS, mail, message.as_string())

