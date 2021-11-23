from atom import *
import tkinter as tk
import random
import os
import sys


class GameFrame:
    def __init__(self, a_list):
        """Constructor, draws window and handles button presses

        Args:
            a_list (Atom_list): list of atoms
        """
        self.a_list = a_list
        self.current_question = ""
        self.root = tk.Tk()
        self.root.title("Game")
        self.answer_list = []

        self.draw_buttons()
        self.draw_reset()
        self.get_question()
        self.root.mainloop()

    def which_button(self, button, data):
        """Interpets what button has been pressed and runs functions

        Args:
            button (Button): button that has been pressed
            data (str): button tag info
        """
        if data == "new":
            self.get_question()
        if data == "quit":
            self.root.destroy()

        elif data == self.current_question:
            button.config(text=data, highlightbackground="green")
            self.answer_list.pop(self.answer_list.index(self.current_question))
            self.get_question()

    def show_random(self, message):
        """Draws question label

        Args:
            message (str): name of atom to guess
        """
        text_string = "Where is: " + message + "?"
        label = tk.Label(self.root, text=text_string)

        label.grid(row=1, column=6, columnspan=4)

    def draw_reset(self):
        """Draws reset question label and reset button
        """
        button = tk.Button(self.root,
                           width=7,
                           height=2,
                           text="New question?",
                           )
        button.config(
            highlightbackground="white",
            fg="blue",
        )
        button.config(command=lambda m=button,
                      d="new": self.which_button(m, d))
        button.grid(row=1, column=8, columnspan=3)

        button = tk.Button(self.root,
                           width=3,
                           height=2,
                           text="Quit",
                           )
        button.config(
            highlightbackground="white",
            fg="blue",
        )
        button.config(command=lambda m=button,
                      d="res": self.which_button(m, d))
        button.grid(row=2, column=9)

    def draw_buttons(self):
        """Draws all atom buttons
        """
        for y in range(9):
            for x in range(18):
                atom = self.a_list.get_xy(x, y)
                if atom.name == "":
                    continue
                color = "yellow"
                color_fg = "black"

                if y > 6:
                    color = "blue"
                button = tk.Button(self.root,
                                   width=5,
                                   height=5,
                                   text="???",
                                   )
                button.config(
                    highlightbackground=color,
                    fg=color_fg,
                )
                button.config(
                    command=lambda m=button, d=atom.name: self.which_button(
                        m, d)
                )
                button.grid(row=y, column=x)
                self.answer_list.append(atom.name)

    def get_question(self):
        """ Gets new question 
        """
        try:
            self.current_question = random.choice(self.answer_list)
            self.show_random(self.current_question)
        except IndexError:
            self.show_random("Du är klar, bra jobbat")


"""
a_list = AtomList()
sajk = GameFrame(a_list)
"""
