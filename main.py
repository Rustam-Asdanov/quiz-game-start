from question_model import Question
from data import question_data, show_data
from prettytable import PrettyTable

question_bank = []

for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)

