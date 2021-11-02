# Module contains function for reading content of file and returning it as dictionary

atom_list = []


def read_file(file_name):
    atom_dict = {}
    with open(file_name, encoding="utf-8") as file:
        next_name = ""
        for line in file:
            line_data = line.split()
            name, weight = line_data[0], line_data[1]
            atom_dict[weight] = name
    return atom_dict


def switch(index):
    global atom_list
    atom_list[index], atom_list[index + 1] = atom_list[index + 1], atom_list[index]


def generate_atom_list(dict):
    global atom_list

    for key in dict.keys():
        atom_list.append(key)
    atom_list.sort(key=float)
    switchers = [18, 27, 52, 90, 92]
    for n in switchers:
        switch(n - 1)

    return atom_list


def get_atoms(file_name):
    a_dict = read_file(file_name)
    a_list = generate_atom_list(a_dict)
    return a_dict, a_list


def main():
    a_dict = read_file("avikt.txt")
    a_list = generate_atom_list(a_dict)
    for index, element in enumerate(a_list):
        print(index + 1, a_dict[element], element)


# main()
