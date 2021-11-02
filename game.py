import random
import sys
import file_reader as fr

atoms = {}


def get_question_weight(name):
    weight = atoms[name]
    attempts = 3

    print("Guess the atom weight of", name)
    while attempts > 0:
        answer = input("Guess: ")
        if answer == weight:
            break
        attempts -= 1
        if attempts > 0:
            print("You guessed incorrectly.", attempts, " attempts left")
    if attempts > 0:
        print("Good job you guessed it in", 3 - attempts, " attempts!")
    else:
        print("You didn't manage to guess it correctly, the answer was", weight)


def get_question_name(weight):
    name =""
    # TODO add function for finding right atom name from weight

    alt_1 = get_alternative(name)
    alt_2 = get_alternative(name)

    alt_dict = [alt_1, alt_2, name]
    random.shuffle(alt_dict, inplace=True)
    attempts = 3

    print("Guess the atom name of", weight)
    while attempts > 0:
        for alt, index in alt_dict:
            print(index + ":" + alt)

        answer = input("Guess: ")
        if answer == name:
            break
        attempts -= 1
        if attempts > 0:
            print("You guessed incorrectly.", attempts, " attempts left")
    if attempts > 0:
        print("Good job you guessed it in", 3 - attempts, " attempts!")
    else:
        print("You didn't manage to guess it correctly, the answer was", name)


def get_alternative(name):
    guess = name
    while guess == name:
        guess = random.choice(list(atoms.keys()))
    return guess


def meny_print():
    print("zap")


def meny_practice_weights():
    print("zap")


def meny_practice_names():
    print("zap")


def meny_exit():
    print("Exiting...")
    sys.exit()


def meny():
    items = {
        "1": meny_print,
        "2": meny_practice_weights,
        "3": meny_practice_names,
        "4": meny_exit,
    }
    ans = ""
    print("-------------- MENY ---------------")
    print("1. Visa alla atomer")
    print("2. Träna på atomnummer")
    print("3. Träa på atombeteckningar")
    print("4. Sluta")
    print("-----------------------------------")
    while True:
        ans = input("Vad vill du göra? ")
        if ans in items.keys():
            break
    items[ans]()


def main():
    # meny()
    global atoms
    atoms = fr.read_file("avikt.txt")
    ran_atom = random.choice(list(atoms.values()))
    get_question_name(ran_atom)


main()
