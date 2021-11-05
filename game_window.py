from tkinter import *
import random
import os
import sys


class Game_window:
    def __init__(self, a_list):
        self.a_list = a_list
        self.current_guess = ""
        self.root = Tk()
        self.answer_list = []
        
        self.draw_buttons()
        self.draw_reset()
        self.get_question()
        mainloop()

    def which_button(self, button, data):
        if data == "new":
            self.get_question()
        if data == "res":
            os.execl(sys.executable, sys.executable, *sys.argv)

        elif data == self.current_guess:
            button.config(text=data)
            self.answer_list.pop(self.answer_list.index(self.current_guess))
            self.get_question()

    def show_random(self, message):
        text_string = "Where is: " + message + "?"
        label = Label(self.root, text=text_string)

        label.grid(row=1, column=6, columnspan=4)

    def draw_reset(self):
        button = Button(
            width=7,
            height=2,
            text="New question?",
        )
        button.config(
            highlightbackground="white",
            fg="blue",
        )
        button.config(command=lambda m=button, d="new": self.which_button(m, d))
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
        button.config(command=lambda m=button, d="res": self.which_button(m, d))
        button.grid(row=2, column=9)

    def draw_buttons(self):

        for y in range(9):
            for x in range(18):
                atom = self.a_list.get_xy(x, y)

                color = "yellow"
                color_fg = "black"
                if atom == -1:
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
                    command=lambda m=button, d=atom.name: self.which_button(m, d)
                )
                button.grid(row=y, column=x)
                self.answer_list.append(atom.name)

    def get_question(self):
        self.current_guess = random.choice(self.answer_list)
        self.show_random(self.current_guess)

from atom import *

a_list = Atom_list()
a_list.get_atoms("avikt.txt", "period_coord.txt")
sajk = Game_window(a_list)