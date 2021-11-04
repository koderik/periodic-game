import random
import tkinter as tk
import file_reader as fr
import time


class Question_frame:
    def __init__(self, a_list, a_dict):
        self.a_list = a_list
        self.a_dict = a_dict
        self.answer = ""
        self.root = tk.Tk()
        # self.attempts = 0
        # self.root.geometry("300x200")

        self.get_question()

        # self.root.title("Atom List")
        self.root.mainloop()

    def get_question(self):

        self.attempts = 3
        weight = random.choice(self.a_list)
        index = self.a_list.index(weight)

        name = self.a_dict[weight]
        question_string = "Guess the atom name of: " + str(index + 1)
        self.answer = name
        self.draw_window(question_string)

    def draw_window(self, question):
        qvar = question
        q = tk.Label(self.root, text=qvar)
        q.config(font=("Courier", 20))
        q.grid(row=0, column=0, padx=30, pady=30)

        self.e = tk.Entry(self.root, textvar=self.answer)
        self.e.grid(row=1, column=0, padx=10, pady=0)

        button = tk.Button(width=3, height=2, text="Submit")
        button.config(highlightbackground="white", fg="blue")
        button.config(command=lambda m=button, d="submit": self.which_button(m, d))
        button.grid(row=1, column=1, padx=10)

        self.a = tk.Label(self.root)
        self.a.config(font=("Courier", 17))
        self.a.grid(row=3, column=0, padx=30, pady=30)

    def which_button(self, button, data):
        if data == "submit":
            if self.attempts > 1:
                guess = self.e.get()
                if guess == self.answer:
                    if self.attempts > 0:
                        output = "Good job you guessed it!"

                        self.a.config(text=output)
                        self.get_question()
                self.attempts -= 1

                if self.attempts > 0:
                    output = (
                        "You guessed incorrectly. "
                        + str(self.attempts)
                        + " attempts left"
                    )
                    self.a.config(text=output)
            else:
                output = (
                    "You didn't manage to guess it correctly, the answer was "
                    + str(self.answer)
                )

                self.a.config(text=output)

                self.get_question()
            self.e.delete(0, "end")


a_dict, a_list = fr.get_atoms("avikt.txt")
awindow = Question_frame(a_list, a_dict)
