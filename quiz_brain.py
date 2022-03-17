from question_model import Question
from data import question_data
from prettytable import PrettyTable

question_bank = []


def show_data():
    table = PrettyTable()
    table.field_names = ["Questions", "Answers"]
    table._max_width = {"Questions": 50, "Answers": 25}
    table.align = "l"
    table.valign = "m"
    for data in question_data:
        table.border = True
        table.add_row([data['text'], data['answer']])
        table.add_row(["-" * 50, "-" * 25])

    print(table)


show_data()
