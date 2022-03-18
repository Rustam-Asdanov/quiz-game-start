from prettytable import PrettyTable

question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                      "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "&quot;Windows NT&quot; is a monolithic kernel.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                      "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                       "question": "MacOS is based on Linux.", "correct_answer": "False",
                                       "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "AMD created the first consumer 64-bit processor.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "hard",
                                       "question": "DHCP stands for Dynamic Host Configuration Port.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows ME operating system was released in the year 2000.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                       "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The first dual-core CPU was the Intel Pentium D.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                                      "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "Linus Sebastian is the creator of the Linux kernel, which went on to be used in Linux, Android, and Chrome OS.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "A Boolean value of &quot;0&quot; represents which of these words?", "correct_answer": "False",
     "incorrect_answers": ["True"]}
]


def show_data():
    """This command helps to show our questions and their answers in table"""
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
