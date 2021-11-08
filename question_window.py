from atom import *
import random
import tkinter as tk
import file_reader as fr
import time


class Question_frame:
    def __init__(self, a_list, type):
        self.a_list = a_list
        self.type = type
        self.answer = ""
        self.root = tk.Tk()
        # self.attempts = 0
        # self.root.geometry("550x250")

        self.get_question(self.type)
        self.a = tk.Label(self.root)
        self.a.config(font=("Courier", 17))
        self.a.grid(row=4, column=0, padx=0, pady=30, columnspan=3)
        self.root.mainloop()

    def get_alternatives(self, atom, a_list, index):
        guess_list = [atom]
        a_list_temp = []
        for element in a_list:
            a_list_temp.append(element)
        for i in range(index):
            if atom in a_list_temp:
                a_list_temp.pop(a_list_temp.index(atom))
            random_element = random.choice(a_list_temp)
            guess_list.append(random_element)
        return guess_list

    def draw_weight_window(self, guess_list, question_string):

        qvar = question_string
        q = tk.Label(self.root, text=qvar)
        q.config(font=("Courier", 20))
        q.grid(row=0, column=0, columnspan=7, padx=30, pady=30)

        for index, element in enumerate(guess_list):

            text = element.weight
            button = tk.Button(self.root, width=3, height=2, text=text)
            button.config(highlightbackground="white", fg="blue")
            button.config(command=lambda m=button,
                          d="submit": self.which_button(m, d))
            button.grid(row=(index + 1), column=0,
                        columnspan=6, padx=10, pady=0)

    def get_question(self, type):
        if self.type == "name":
            self.attempts = 3
            atom = random.choice(self.a_list)
            index = atom.number

            name = atom.name
            question_string = "Guess the atom name of: " + str(index)
            self.answer = name
            self.draw_window(question_string)

        elif self.type == "number":
            self.attempts = 3
            atom = random.choice(self.a_list)
            index = atom.number

            name = atom.name
            question_string = "Guess the atom number of: " + name
            self.answer = str(index)
            self.draw_window(question_string)

        elif self.type == "weight":
            self.attempts = 2
            atom = random.choice(self.a_list)
            index = atom.number
            weight = atom.weight
            name = atom.name
            question_string = "Guess the atom weight of: " + name
            self.answer = atom.weight

            guess_list = self.get_alternatives(atom, self.a_list, 2)
            random.shuffle(guess_list)

            self.draw_weight_window(guess_list, question_string)

    def draw_window(self, question):
        qvar = question
        q = tk.Label(self.root, text=qvar)
        q.config(font=("Courier", 20))
        q.grid(row=0, column=0, columnspan=6, padx=30, pady=30)

        self.e = tk.Entry(self.root, textvar=self.answer)
        self.e.grid(row=1, column=0, padx=10, pady=0)

        button = tk.Button(self.root, width=3, height=2, text="Submit")
        button.config(highlightbackground="white", fg="blue")
        button.config(command=lambda m=button,
                      d="submit": self.which_button(m, d))
        button.grid(row=1, column=1, padx=10)

    def which_button(self, button, data):
        if data == "submit":
            self.attempts -= 1
            if self.attempts >= 0:

                if self.type not in "weight":
                    guess = self.e.get()
                    self.e.delete(0, "end")
                else:
                    guess = button.cget("text")

                if str(guess) == str(self.answer):

                    output = "Good job you guessed it!"

                    self.get_question(self.type)
                elif self.attempts == 0:
                    output = (
                        "You didn't manage to guess it correctly\nThe answer was "
                        + str(self.answer)
                    )
                    self.a.config(text=output)

                    self.get_question(self.type)
                else:
                    output = (
                        "You guessed incorrectly. "
                        + str(self.attempts)
                        + " attempts left"
                    )
                self.a.config(text=output)

            else:
                output = (
                    "You didn't manage to guess it correctly\nThe answer was "
                    + str(self.answer)
                )

                self.a.config(text=output)
                self.get_question(self.type)


"""
a_list = Atom_list()
a_list.get_atoms("avikt.txt", "period_coord.txt")
awindow = Question_frame(a_list, "number")
"""
