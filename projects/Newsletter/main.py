import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import csv
from typing import List
from MailReciever import MailReciever

# EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

EMAIL_ADDRESS = "asenso@asensosa.com"
EMAIL_PASSWORD = input()

HOST = 'smtp.asprodukt.nazwa.pl'
PORT = 587

ATTACHMENTS_PATH = "attachments"

mail_recievers: List[MailReciever] = [
]

attachments: List[str] = [os.path.join(
    ATTACHMENTS_PATH, f) for f in os.listdir(ATTACHMENTS_PATH)]

with smtplib.SMTP(HOST, 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    html = open('message.html', 'r', encoding='utf-8').read()

    for mail_reciever in mail_recievers:
        print('Sending mail to', mail_reciever)
        message = MIMEMultipart()
        message["Subject"] = "Prezent świąteczny od Asenso!"
        message["From"] = f"ASENSO Saunowa Awangarda <{EMAIL_ADDRESS}>"
        message["To"] = mail_reciever.address

        prepared_html = mail_reciever.get_prepared_html(html)

        mainPart = MIMEText(prepared_html, 'html', 'utf-8')
        message.attach(mainPart)

        for file_path in attachments:
            with open(file_path, "rb") as f:
                attachment_part = MIMEApplication(f.read())
                attachment_part.add_header(
                    'Content-Disposition', 'attachment', filename=os.path.basename(file_path))
                message.attach(attachment_part)

        smtp.sendmail(EMAIL_ADDRESS, mail_reciever.address,
                      message.as_string())
