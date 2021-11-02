# Module contains function for reading content of file and returning it as dictionary
def read_file(file_name):
    atom_dict = {}
    with open(file_name, encoding="utf-8") as file:
        next_name = ""
        for line in file:
            line_data = line.split()
            name, weight = line_data[0], line_data[1]
            atom_dict[name] = weight
    return atom_dict
