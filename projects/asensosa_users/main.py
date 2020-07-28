from asusers import ASUsers

# for msg in load_messages(self.path):
#     add_answer(parse_answers(msg))
PATH = './users'
asusers = ASUsers('users.csv')

asusers.add_header()
for msg in asusers.load_messages(PATH):
    asusers.add_answer(asusers.parse_answer(msg))
