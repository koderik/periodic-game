import random
import tkinter as tk
import time
import sys
import game_window as g_w
import list_window as a_w
import question_window as q_w
from atom import *


class MenyFrame:
    def __init__(self, a_list):
        functions = {
            "Show All": self.meny_print,
            "Practice Numbers": self.meny_practice_numbers,
            "Practice Names": self.meny_practice_names,
            "Practice Weights": self.meny_practice_weights,
            "Start Game": self.meny_start_game,
            "Exit": self.meny_exit,
        }

        self.a_list = a_list
        self.root = tk.Tk()
        self.root.title("Meny")

        label_text = "Meny"
        q = tk.Label(self.root, text=label_text)
        q.config(font=("Courier", 20))
        q.grid(row=0, column=0, padx=30, pady=30)

        row = 1
        for key in functions.keys():
            label_text = key

            button = tk.Button(self.root, width=16, height=4, text=label_text)
            button.config(font=("Courier", 20))
            button.config(highlightbackground="white", fg="blue")
            button.config(command=functions[key])
            button.grid(row=row, column=0, padx=10, pady=5)
            row += 1
        self.root.mainloop()

    def meny_print(self):
        """Creates new window with list of atoms
        """
        a_win = a_w.ListFrame(a_list)

    def meny_practice_numbers(self):
        """Creates new window with question of type "number"
        """
        q_win = q_w.QuestionFrame(a_list, "number")

    def meny_practice_names(self):
        """Creates new window with question of type "name"
        """
        q_win = q_w.QuestionFrame(a_list, "name")

    def meny_practice_weights(self):
        """Creates new window with question of type "number"
        """
        w_win = q_w.QuestionFrame(a_list, "weight")

    def meny_start_game(self):
        """Creates new window with atom guessing game
        """
        Game = g_w.GameFrame(a_list)

    def meny_exit(self):
        """Exits program
        """
        sys.exit()


a_list = AtomList()
awindow = MenyFrame(a_list)
