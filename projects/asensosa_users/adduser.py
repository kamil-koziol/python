from asusers import ASUsers
import argparse
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-f", "--file", help="Give file/files of emails to add", nargs="+", required=True)
parser.add_argument('-d', "--destination" , help="Select where the data is stored at", required=True)
args = parser.parse_args()


asusers = ASUsers(args.destination)

for mail in args.file:
    msg = asusers.load_message(mail)
    asusers.add_answer(asusers.parse_answer(msg))
