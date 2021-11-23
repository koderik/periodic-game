from tkinter import *
from atom import *


class ListFrame:
    """Frame with atom list
    """

    def __init__(self, a_list):
        """Constructor, draws some graphics

        Args:
            a_list (Atom_list): list of atoms
        """
        self.on = True
        self.a_list = a_list

        self.root = Tk()
        self.root.title("Atom List")
        self.draw_table()
        
        self.root.mainloop()

    def draw_table(self):
        """Draws the table of all the atoms with the atom number, name and weight in three columns
        """
        self.counter = 0
        height = 35
        min = 0
        x = 0
        for count in range(3):
            for y in range(height):  # Rows
                if self.counter < 103:
                    self.draw_index(x, count, y)

                    self.draw_name(x, y)

                    self.draw_weight(x, y)

                    self.counter += 1
            x += 3

    def draw_weight(self, x, y):
        """Draws the weight in a label

        Args:
            x (int): x-coordinate in grid
            y (int]): y-coordinate in grid
        """
        atom = self.a_list.get_number(self.counter + 1)
        textvar = atom.weight + "u"
        b = Label(self.root, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=y, column=x + 2)

    def draw_name(self, x, y):
        atom = self.a_list.get_number(self.counter + 1)
        textvar = atom.name

        b = Label(self.root, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=y, column=x + 1)

    def draw_index(self, x, count, y):
        if count > 0:
            textvar = "\t" + str(self.counter + 1) + ":"
        else:
            textvar = str(self.counter + 1) + ":"
        b = Label(self.root, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=y, column=x)

    def create_button(self):
        button = Button(width=3, height=2, text="Exit?")
        button.config(highlightbackground="white", fg="blue")
        button.config(command=lambda m=button,
                      d="exit": self.which_button(m, d))
        button.grid(row=32, column=7, rowspan=2)

    def which_button(self, button, data):
        if data == "exit":
            self.root.destroy()


'''
a_list = Atom_list()
a_list.get_atoms("avikt.txt", "period_coord.txt")
awindow = Atom_list_window(a_list)
'''
