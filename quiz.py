import tkinter
from tkinter import *
import random

questions = [
    "What is the output of 'print(5 + 3)'?",
    "Which data type is used to store a single character in Python?",
    "What is the result of '5 // 2' in Python?",
    "Which of the following is a valid Python variable name?",
    "What is the purpose of 'if' statements in Python?",
    "Which operator is used for exponentiation in Python?",
    "What will the expression 'True and False' evaluate to?",
    "In Python, how do you comment out a single line of code?",
    "What is the output of 'len('Python')'?",
    "Which function is used to take user input in Python?",
]

answers_choice = [
    ["7", "8", "53", "Error"],
    ["int", "char", "str", "bool"],
    ["2.5", "2", "2.0", "2.25"],
    ["my_variable", "2ndVar", "global_variable", "for"],
    ["To repeat a block of code", "To define a function", "To check if a condition is True", "To exit a loop"],
    ["**", "^^", "//", "%%"],
    ["True", "False", "None", "Error"],
    ["// This is a comment", "# This is a comment", "/* This is a comment */", "-- This is a comment"],
    ["5", "6", "7", "Error"],
    ["input()", "get_input()", "read_input()", "user_input()"],
]

# Correct answers
answers = [1, 2, 1, 0, 2, 0, 1, 1, 3, 0]

user_answer = []

indexes = []


def generate_random_indexes():
    global indexes
    while len(indexes) < 5:
        x = random.randint(0, len(questions) - 1)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def show_result(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimg = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimg.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Comic sans MS", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="good.png")
        labelimg.configure(image=img)
        labelimg.image = img
        labelresulttext.configure(text="You Are Excellent !!")
    elif 10 <= score < 20:
        img = PhotoImage(file="avg.png")
        labelimg.configure(image=img)
        labelimg.image = img
        labelresulttext.configure(text="You Can Be Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimg.configure(image=img)
        labelimg.image = img
        labelresulttext.configure(text="You Should Work Hard !!")


def calculate_score():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    show_result(score)


current_question = 1


def handle_selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global current_question
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if current_question < 5:
        lblQuestion.config(text=questions[indexes[current_question]])
        r1['text'] = answers_choice[indexes[current_question]][0]
        r2['text'] = answers_choice[indexes[current_question]][1]
        r3['text'] = answers_choice[indexes[current_question]][2]
        r4['text'] = answers_choice[indexes[current_question]][3]
        current_question += 1
    else:
        calculate_score()


def start_quiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Comic sans MS", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Comic sans MS", 12),
        value=0,
        variable=radiovar,
        command=handle_selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Comic sans MS", 12),
        value=1,
        variable=radiovar,
        command=handle_selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Comic sans MS", 12),
        value=2,
        variable=radiovar,
        command=handle_selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Comic sans MS", 12),
        value=3,
        variable=radiovar,
        command=handle_selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def start_button_pressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    generate_random_indexes()
    start_quiz()


root = tkinter.Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(False, False)

img1 = PhotoImage(file="logo.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="QuizMaster",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

img2 = PhotoImage(file="start.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=start_button_pressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background="#ffffff",
    font=("Comic sans MS", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 100))

lblRules = Label(
    root,
    text="Contains 10 questions and There are 20 seconds to solve a question"
         "\nOnce you select a radio button, that will be a final choice\nhence think before you select",
    width=100,
    font=("Times", 14),
    background="#000000",
    foreground="#FACA2F",
)
lblRules.pack()

root.mainloop()
