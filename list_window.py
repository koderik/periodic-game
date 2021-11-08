from tkinter import *
from atom import *


class Atom_list_window:
    def __init__(self, a_list):
        self.on = True
        self.a_list = a_list

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
                if self.counter < 103:
                    self.draw_index(x, count, i)

                    self.draw_name(x, i)

                    self.draw_weight(x, i)

                    self.counter += 1
            x += 3

    def draw_weight(self, x, i):
        atom = self.a_list.get_number(self.counter + 1)
        textvar = atom.weight + "u"
        b = Label(self.root, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=i, column=x + 2)

    def draw_name(self, x, i):
        atom = self.a_list.get_number(self.counter + 1)
        textvar = atom.name

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

'''
a_list = Atom_list()
a_list.get_atoms("avikt.txt", "period_coord.txt")
awindow = Atom_list_window(a_list)
'''