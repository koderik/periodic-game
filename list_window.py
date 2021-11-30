import tkinter as tk


class ListFrame(tk.Frame):
    """Frame with atom list
    """

    def __init__(self, container, a_list):
        """Constructor, sets variables and calls functions to draw table

        Args:
            container (tk.Tk): main frame
            a_list (AtomList): list of atoms
        """
        super().__init__(container)
        self.container = container

        self.a_list = a_list

        self.draw_table()

    def draw_table(self):
        """Draws the table of all the atoms with the atom number, name and weight in three columns
        """
        self.counter = 0
        height = 35
        x = 0
        for count in range(3):
            for y in range(height):  # Rows
                self.draw_column(x, y, count)
            x += 3

    def draw_column(self, x, y, count):
        if self.counter < 103:
            self.draw_index(x, y, count)
            self.draw_name(x, y)
            self.draw_weight(x, y)
            self.counter += 1

    def draw_weight(self, x, y):
        """Draws the weight in a label

        Args:
            x (int): x-coordinate in grid
            y (int]): y-coordinate in grid
        """
        atom = self.a_list.get_number(self.counter + 1)
        textvar = atom.weight + "u"
        b = tk.Label(self, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=y, column=x + 2)

    def draw_name(self, x, y):
        """Draws name of atom

        Args:
            x (int): x-coordinate
            y (int): y-coordinate
        """
        atom = self.a_list.get_number(self.counter + 1)
        textvar = atom.name
        b = tk.Label(self, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=y, column=x + 1)

    def draw_index(self, x, y, count):
        """Draws the atom number

        Args:
            x (int): x-coordinate
            count (int): row counter
            y (int): y-coordinate
        """
        if count > 0:
            textvar = "\t" + str(self.counter + 1) + ":"
        else:
            textvar = str(self.counter + 1) + ":"
        b = tk.Label(self, text=textvar)
        b.config(font=("Courier", 20))
        b.grid(row=y, column=x)
