import random
from atom import *


def get_question_number(a_list):
    atom = random.choice(a_list)
    index = atom.number
    name = atom.name

    attempts = 3

    print("Guess the atom number of", name)
    while attempts > 0:
        answer = input("Guess: ")
        if answer == str(index + 1):
            break
        attempts -= 1
        if attempts > 0:
            print("You guessed incorrectly.", attempts, " attempts left")
    if attempts > 0:
        print("Good job you guessed it!")
    else:
        print("You didn't manage to guess it correctly, the answer was", index)


def get_question_name(a_list):
    atom = random.choice(a_list)
    index = atom.number
    name = atom.name

    attempts = 3

    print("Guess the atom name of", index + 1)
    while attempts > 0:
        answer = input("Guess: ")
        if answer == name:
            break
        attempts -= 1
        if attempts > 0:
            print("You guessed incorrectly.", attempts, "attempts left")
    if attempts > 0:
        print("Good job you guessed it!")
    else:
        print("You didn't manage to guess it correctly, the answer was", name)


def get_alternatives(atom, a_list, index):
    guess_list = [atom]
    a_list_temp = []
    for element in a_list:
        a_list_temp.append(element)
    for i in range(index):
        if atom in a_list_temp:
            a_list_temp.pop(a_list_temp.index(atom))
        random_element = random.choice(a_list_temp)
        guess_list.append(random_element)
    return guess_list


def get_question_weight(a_list):
    atom = random.choice(a_list)

    name = atom.name
    guess_list = get_alternatives(atom, a_list, 2)
    random.shuffle(guess_list)  # TODO fortsätt göra en liten gisnsingsmeny här
    attempts = 2

    print("Guess the atom weight of", name)
    for index, element in enumerate(guess_list):
        print(str(index + 1) + ":" + element.weight)
    while attempts > 0:
        answer = input("Guess: ")
        if answer == str(guess_list.index(atom) + 1):
            break
        attempts -= 1
        if attempts > 0:
            print("You guessed incorrectly.", attempts, " attempts left")
    if attempts > 0:
        print("Good job you guessed it!")
    else:
        print("You didn't manage to guess it correctly, the answer was", index)


a_list = Atom_list()
a_list.get_atoms("avikt.txt", "period_coord.txt")
get_question_name(a_list)
get_question_weight(a_list)
get_question_number(a_list)
