import random
import tkinter as tk
import time
import sys
import game_window as g_w
import list_window as a_w
import question_window as q_w
from atom import *


class Meny_frame:
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
        a_win = a_w.Atom_list_window(a_list)

    def meny_practice_numbers(self):
        q_win = q_w.Question_frame(a_list, "number")

    def meny_practice_names(self):
        q_win = q_w.Question_frame(a_list, "name")

    def meny_practice_weights(self):
        w_win = q_w.Question_frame(a_list, "weight")


    def meny_start_game(self):
        Game = g_w.Game_window(a_list)

    def meny_exit(self):
        print("Exiting...")
        sys.exit()


from atom import *

a_list = Atom_list()
a_list.get_atoms("avikt.txt", "period_coord.txt")
awindow = Meny_frame(a_list)
