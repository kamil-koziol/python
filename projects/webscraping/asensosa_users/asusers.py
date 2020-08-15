from email import message_from_file
import os
from bs4 import BeautifulSoup
import csv
from typing import List, Dict

class ASUsers:
    def __init__(self, output_file):
        self.output = output_file
        self.headers = ['Date Submitted','Nazwa użytkownika','Imię','Nazwisko','Adres E-mail','Numer telefonu komórkowego','NIP','Nazwa biura projektowego']
        new_file = not os.path.exists(self.output)
        self.writer = csv.DictWriter(open(self.output, "a"), fieldnames=self.headers)
        if new_file:
            self.add_header()

    def load_message(self, path) -> str:
        with open(path, "r") as f:
            msg = message_from_file(f).get_payload(decode=True)
        return msg

    def load_messages(self, path) -> List[str]:
        mails = os.listdir(path)
        mails = [mail for mail in mails if mail.endswith(".eml")]

        messages = []
        for mail in mails:
            with open(os.path.join(path, mail), "r") as f:
                msg = message_from_file(f).get_payload(decode=True)
                messages.append(msg)

        return messages
    

    def clean_answers(self, answers: Dict[str,str]):
        answers.pop("marketing")
        answers.pop("Formularz")
        return answers

    def parse_answer(self, msg: str):
        soup = BeautifulSoup(msg, 'html.parser')
        answers = {}
        for div in soup.find_all("div"):
            if div.text.startswith("Informacje"):
                labels = div.find_all("label")
                spans = div.find_all("span")
                for label, span in zip(labels, spans):
                    label_text = label.text.replace(":", "").strip()
                    span_text = span.text
                    if span_text == '(pusty)':
                        span_text = ""
                    answers[label_text] = span_text
        return self.clean_answers(answers)

    def add_header(self):
        self.clear_output_file()
        self.writer.writeheader()

    def add_answer(self, answer):
        self.writer.writerow(answer)
    
    def clear_output_file(self):
        open(self.output, 'w').close()