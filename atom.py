class Atom:
    """Atom class that contains specific data about atom such as name, weight, atomic number and x,y coordinates.
    """

    def __init__(self, name="", weight=""):
        """Constructor

        Args:
            name (str, optional): Scientific abbreviation of atom name. Defaults to "".
            weight (str, optional): Atom weight in unit u. Defaults to "".
        """
        self.name = name
        self.weight = weight

    def set_xy(self, x, y):
        """Sets coordinates in periodic table context

        Args:
            x (Int): x-coordinate
            y (Int): y-coordinate
        """
        self.x, self.y = x, y

    def set_number(self, num):
        """Sets atomic number of atom

        Args:
            num (str): Atomic number of atom
        """
        self.number = num

    def __lt__(self, other):
        """Comparator

        Args:
            other (Atom): other Atom

        Returns:
            Boolean: True if this Atom has lesser weight than other atom, else False
        """
        return float(self.weight) < float(other.weight)


class AtomList:
    """List of Atoms
    """

    def __init__(self, file_weight="avikt.txt", file_coord="period_coord.txt"):
        """Constructor, creates empty list
        """
        self.a_list = []
        self.fill_list(file_weight)

        self.set_numbers()
        self.set_coords(file_coord)

    def __iter__(self):
        """Makes object iterable

        Yields:
            Atom: yields all atoms in atom_list
        """
        for atom in self.a_list:
            yield atom

    def __len__(self):
        """Gives object length

        Returns:
            Int: length of atom_list
        """
        return len(self.a_list)

    def __getitem__(self, index):
        """Makes object callable like a list

        Args:
            index (Int): requested index

        Returns:
            Atom: Atom at index in atom_list
        """
        return self.a_list[index]

    def get_name(self, name):
        """Getter for atom at specifik name, linear search

        Args:
            name (str): name of Atom to search for

        Returns:
            Atom: Atom with specified name, or empty Atom if no such atom exists
        """
        for atom in self.a_list:
            if name == atom.name:
                return atom
        return -1

    def get_weight(self, weight):
        """Getter for atom at specifik weight, linear search

        Args:
            weight (str): weight of Atom to search for

        Returns:
            Atom: Atom with specified weight, or empty Atom if no such atom exists
        """
        for atom in self.a_list:
            if weight == atom.weight:
                return atom
        return Atom()

    def get_number(self, num):
        """Getter for atom at specifik number, linear search

        Args:
            number (str): number of Atom to search for

        Returns:
            Atom: Atom with specified number, or empty Atom if no such atom exists
        """
        for atom in self.a_list:
            if num == atom.number:
                return atom
        return Atom()

    def get_xy(self, x, y):
        """Getter for atom at specifik x, y coords, linear search

        Args:
            x (int): specific x coord
            y (int): specific y coord

        Returns:
            Atom: Atom with specified x, y coord, or empty Atom if no such atom exists
        """
        for atom in self.a_list:
            if atom.x == x and atom.y == y:
                return atom
        return Atom()

    def switch(self, index):
        """Switches places of index and item in front of index, inplace

        Args:
            index (Int): index to switch
        """
        self.a_list[index], self.a_list[index + 1] = (
            self.a_list[index + 1],
            self.a_list[index],
        )

    def fill_list(self, file_name):
        """Reads atom weights and names from file to atom_list

        Args:
            file_name (str): name of file to read from
        """
        with open(file_name, encoding="utf-8") as file:
            next_name = ""
            for line in file:
                line_data = line.split()
                name, weight = line_data[0], line_data[1]
                atom = Atom(name, weight)
                self.a_list.append(atom)

    def set_coords(self, file_name):
        """Sets coords for atoms from file

        Args:
            file_name (str): name of file to read from
        """
        with open(file_name) as file:
            for y in range(9):
                for x in range(18):
                    line_data = file.readline().strip("\n").split(" ")
                    if line_data[2] == "0":
                        continue

                    self.get_name(line_data[2]).set_xy(x, y)

    def set_numbers(self):
        """Sorts atom_list and assings atomic numbers, specficik numbers to match the real periodic table
        """
        self.a_list.sort()
        switchers = [18, 27, 52, 90, 92]
        for n in switchers:
            self.switch(n - 1)
        for index, atom in enumerate(self.a_list):
            atom.set_number(index + 1)
