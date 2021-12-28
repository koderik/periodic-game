import tkinter as tk
import sys
import game_window as g_w
import list_window as a_w
import question_window as q_w
from atom import *


class MenyFrame(tk.Frame):
    """Frame that displays menu
    """

    def __init__(self, container, a_list):
        """Constructor, initalizes frame with buttons

        Args:
            container (tk.Tk): main frame
            a_list (AtomList): list of atoms
        """

        super().__init__(container)
        self.container = container

        self.functions = {
            "Show All": self.meny_print,
            "Practice Numbers": self.meny_practice_numbers,
            "Practice Names": self.meny_practice_names,
            "Practice Weights": self.meny_practice_weights,
            "Start Game": self.meny_start_game,
            "Exit": self.meny_exit,
        }
        self.a_list = a_list

        label_text = "Meny"
        q = tk.Label(self, text=label_text)
        q.config(font=("Courier", 20))
        q.grid(row=0, column=0, padx=30, pady=30)
        self.row = 1
        for key in self.functions:
            self.draw_button(key)

    def draw_button(self, key):
        """Draws specific meny button

        Args:
            key (key): name of button
        """
        label_text = key
        button = tk.Button(self, width=16, height=4, text=label_text)
        button.config(font=("Courier", 20))
        button.config(highlightbackground="white", fg="blue")
        button.config(command=self.functions[key])
        button.grid(row=self.row, column=0, padx=10, pady=5)
        self.row += 1

    def meny_print(self):
        """Sends list_frame to main frame
        """

        a_win = a_w.ListFrame(self.container, self.a_list)
        self.container.display_frame(a_win)

    def meny_practice_numbers(self):
        """Sends question_frame to main frame of type "number"
        """
        q_win = q_w.QuestionFrame(self.container, self.a_list, "number")
        self.container.display_frame(q_win)

    def meny_practice_names(self):
        """Sends question_frame to main frame of type "name"
        """
        q_win = q_w.QuestionFrame(self.container, self.a_list, "name")
        self.container.display_frame(q_win)

    def meny_practice_weights(self):
        """Sends question_frame to main frame of type "number"
        """
        q_win = q_w.QuestionFrame(self.container, self.a_list, "weight")
        self.container.display_frame(q_win)

    def meny_start_game(self):
        """Creates new window with atom guessing game
        """
        g_win = g_w.GameFrame(self.container, self.a_list)
        self.container.display_frame(g_win)

    def meny_exit(self):
        """Exits program
        """
        sys.exit()