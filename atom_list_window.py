from tkinter import *
from tkinter import ttk
import file_reader as fr


class Atom_list_window:
    def __init__(self, a_list, a_dict):
        self.on = True
        self.a_list = a_list
        self.a_dict = a_dict
        self.root = Tk()
        self.root.title("Atom List")
        self.draw_table()
        # self.create_button()
        self.root.mainloop()

    def draw_table(self):
        self.counter = 0
        height = 35
        min = 0
        x = 0
        for count in range(3):
            for i in range(height):  # Rows
                if self.counter < 102:
                    self.draw_index(x, count, i)

                    self.draw_name(x, i)

                    self.draw_weight(x, i)

                    self.counter += 1
            x += 3

    def draw_weight(self, x, i):
        textvar = self.a_list[self.counter] + "u"
        b = Label(self.root, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=i, column=x + 2)

    def draw_name(self, x, i):
        textvar = self.a_dict[self.a_list[self.counter]]
        b = Label(self.root, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=i, column=x + 1)

    def draw_index(self, x, count, i):
        if count > 0:
            textvar = "\t" + str(self.counter + 1) + ":"
        else:
            textvar = str(self.counter + 1) + ":"
        b = Label(self.root, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=i, column=x)

    def create_button(self):
        button = Button(width=3, height=2, text="Exit?")
        button.config(highlightbackground="white", fg="blue")
        button.config(command=lambda m=button, d="exit": self.which_button(m, d))
        button.grid(row=32, column=7, rowspan=2)

    def which_button(self, button, data):
        if data == "exit":
            self.root.destroy()


"""
a_dict, a_list = fr.get_atoms("avikt.txt")
awindow = Atom_list_window(a_list, a_dict)
"""
