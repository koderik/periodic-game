from tkinter import *
import random
import os
import sys


def which_button(button, data):
    if data == "new":
        get_question()
    if data == "res":
        os.execl(sys.executable, sys.executable, *sys.argv)

    elif data == current_guess:
        button.config(text=data)
        answer_list.pop(answer_list.index(current_guess))
        get_question()


def show_random(message):
    text_string = "Where is: " + message + "?"
    label = Label(root, text=text_string)

    label.grid(row=1, column=6, columnspan=4)


def draw_reset():
    button = Button(
        width=7,
        height=2,
        text="New question?",
    )
    button.config(
        highlightbackground="white",
        fg="blue",
    )
    button.config(command=lambda m=button, d="new": which_button(m, d))
    button.grid(row=1, column=8, columnspan=3)

    button = Button(
        width=3,
        height=2,
        text="Reset?",
    )
    button.config(
        highlightbackground="white",
        fg="blue",
    )
    button.config(command=lambda m=button, d="res": which_button(m, d))
    button.grid(row=2, column=9)


def draw_buttons():
    global answer_list, button_list, which_button
    with open("period_coord.txt", encoding="utf-8") as file:
        for y in range(9):
            for x in range(18):
                line_data = file.readline().strip("\n").split(" ")
                color = "yellow"
                color_fg = "black"
                if line_data[2] == "0":
                    continue
                if y > 6:
                    color = "blue"
                button = Button(
                    width=5,
                    height=5,
                    text="???",
                )
                button.config(
                    highlightbackground=color,
                    fg=color_fg,
                )
                button.config(
                    command=lambda m=button, d=line_data[2]: which_button(m, d)
                )
                button.grid(row=y, column=x)
                answer_list.append(line_data[2])


def get_question():
    global current_guess
    current_guess = random.choice(answer_list)
    show_random(current_guess)


answer_list = []
current_guess = ""
root = Tk()


def start():
    draw_buttons()
    draw_reset()
    get_question()
    mainloop()
