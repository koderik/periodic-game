import tkinter as tk
import random


class QuestionFrame:
    """Frame that handles and displays all three types of atom questions
    """

    def __init__(self, a_list, type):
        """Constructor, draws base window 

        Args:
            a_list (Atom_list): list with atoms to extract data from
            type (str): Type of question, "name", "number", or "weight"
        """
        self.a_list = a_list
        self.type = type
        self.answer = ""
        self.root = tk.Tk()
        self.root.title("Guess the "+type.capitalize())
        self.get_question(self.type)
        self.result_label = tk.Label(self.root)
        self.result_label.config(font=("Courier", 17))
        self.result_label.grid(row=4, column=0, padx=0, pady=30, columnspan=3)
        self.root.mainloop()

    def draw_weight_window(self, guess_list, question_string):
        """Draws graphics specific for weight question.

        Args:
            guess_list (list): List of three atoms to display weight of
            question_string (str): String of question to display in label
        """
        qvar = question_string
        question_label = tk.Label(self.root, text=qvar)
        question_label.config(font=("Courier", 20))
        question_label.grid(row=0, column=0, columnspan=7, padx=30, pady=30)
        for index, element in enumerate(guess_list):
            text = element.weight
            submit_button = tk.Button(self.root, width=3, height=2, text=text)
            submit_button.config(highlightbackground="white", fg="blue")
            submit_button.config(command=lambda m=submit_button,
                                 d="submit": self.which_button(m, d))
            submit_button.grid(row=(index + 1), column=0,
                               columnspan=6, padx=10, pady=0)

    def get_question(self, type):
        """Generates question and answer depending on type

        Args:
            type (str): Type of question, "name", "number", or "weight"
        """
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
            # The last argument can be changed if more alternatives are needed
            guess_list = self.get_alternatives(atom, self.a_list, 2)
            random.shuffle(guess_list)
            self.draw_weight_window(guess_list, question_string)

    def draw_window(self, question):
        """Draws graphics for name and number questions

        Args:
            question (str): String of question to display in label
        """
        qvar = question
        question_label = tk.Label(self.root, text=qvar)
        question_label.config(font=("Courier", 20))
        question_label.grid(row=0, column=0, columnspan=6, padx=30, pady=30)
        self.answer_field = tk.Entry(self.root, textvar=self.answer)
        self.answer_field.grid(row=1, column=0, padx=10, pady=0)
        submit_button = tk.Button(self.root, width=3, height=2, text="Submit")
        submit_button.config(highlightbackground="white", fg="blue")
        submit_button.config(command=lambda m=submit_button,
                             d="submit": self.which_button(m, d))
        submit_button.grid(row=1, column=1, padx=10)

    def which_button(self, button, tag):
        """Function that is called when a button is pressed and handles the guessing game mechanic

        Args:
            button (Button): Button object that was pressed
            tag (str): special data that was sent with button press.
        """
        if tag == "submit":
            self.attempts -= 1
            if self.attempts >= 0:
                if self.type not in "weight":
                    guess = self.answer_field.get()
                    self.answer_field.delete(0, "end")
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
                    self.result_label.config(text=output)
                    self.get_question(self.type)
                else:
                    output = (
                        "You guessed incorrectly. "
                        + str(self.attempts)
                        + " attempts left"
                    )
                self.result_label.config(text=output)
            else:
                output = (
                    "You didn't manage to guess it correctly\nThe answer was "
                    + str(self.answer)
                )
                self.result_label.config(text=output)
                self.get_question(self.type)

    def get_alternatives(self, atom, a_list, index):
        """Helper function that generates a list of three
        atom weights to display when guessing weight

        Args:
            atom (Atom): Atom that correspond to the right answer
            a_list (Atom_list): Atom_list to grab two other atoms from
            index (Int): amount of other alternatives to display, in this case index=2

        Returns:
            list: returns list of three atoms to display in weight question
        """
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
