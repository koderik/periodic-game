class Atom:
    def __init__(self, name="", weight=""):
        self.name = name
        self.weight = weight

    def set_xy(self, x, y):
        self.x, self.y = x, y

    def set_number(self, num):
        self.number = num

    def __lt__(self, other):
        return float(self.weight) < float(other.weight)


class Atom_list:
    def __init__(self):
        self.a_list = []

    def get_atoms(self, file_weight, file_coord):
        self.fill_list(file_weight)

        self.set_numbers()
        self.set_coords(file_coord)

    def __iter__(self):
        for atom in self.a_list:
            yield atom

    def __len__(self):
        return len(self.a_list)

    def __getitem__(self, index):
        return self.a_list[index]

    def get_name(self, name):
        for atom in self.a_list:
            if name == atom.name:
                return atom
        return -1

    def get_weight(self, weight):
        for atom in self.a_list:
            if weight == atom.weight:
                return atom
        return -1

    def get_number(self, num):
        for atom in self.a_list:
            if num == atom.number:
                return atom
        return Atom()

    def get_xy(self, x, y):
        for atom in self.a_list:
            if atom.x == x and atom.y == y:
                return atom
        return -1

    def switch(self, index):
        self.a_list[index], self.a_list[index + 1] = (
            self.a_list[index + 1],
            self.a_list[index],
        )

    def fill_list(self, file_name):
        with open(file_name, encoding="utf-8") as file:
            next_name = ""
            for line in file:
                line_data = line.split()
                name, weight = line_data[0], line_data[1]
                atom = Atom(name, weight)
                self.a_list.append(atom)

    def set_coords(self, file_name):
        with open(file_name) as file:
            for y in range(9):
                for x in range(18):
                    line_data = file.readline().strip("\n").split(" ")
                    if line_data[2] == "0":
                        continue

                    self.get_name(line_data[2]).set_xy(x, y)

    def set_numbers(self):
        self.a_list.sort()
        switchers = [18, 27, 52, 90, 92]
        for n in switchers:
            self.switch(n - 1)
        for index, atom in enumerate(self.a_list):
            atom.set_number(index + 1)
