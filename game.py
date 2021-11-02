import random

import file_reader as fr

atoms = {}


def get_question(name):
    weight = atoms[name]
    attempts = 3

    print("Guess the atom weight of", name)
    while attempts > 0:
        answer = input("Guess: ")
        if answer == weight:
            break
        attempts -= 1
        if attempts > 0:
            print(
                "You guessed incorrectly.", attempts, " attempts left"
            ) 
    if attempts > 0:
        print("Good job you guessed it in", 3 - attempts, " attempts!")
    else:
        print("You didn't manage to guess it correctly, the answer was", weight)  
 

def main():
    global atoms
    atoms = fr.read_file("avikt.txt")
    ran_atom = random.choice(list(atoms.keys()))
    get_question(ran_atom)


main()
