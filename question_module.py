import random


def get_question_number(a_list, a_dict):
    weight = random.choice(a_list)
    index = a_list.index(weight)
    name = a_dict[weight]

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


def get_question_name(a_list, a_dict):
    weight = random.choice(a_list)
    index = a_list.index(weight)
    name = a_dict[weight]

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


def get_alternatives(weight, a_list, index):
    guess_list = [weight]
    a_list_temp = []
    for element in a_list:
        a_list_temp.append(element)
    for i in range(index):
        if guess_list[i] in a_list_temp:
            a_list_temp.pop(a_list_temp.index(guess_list[i]))
        random_element = random.choice(a_list_temp)
        guess_list.append(random_element)
    return guess_list


def get_question_weight(a_list, a_dict):
    weight = random.choice(a_list)

    name = a_dict[weight]
    guess_list = get_alternatives(weight, a_list, 2)
    random.shuffle(guess_list)  # TODO fortsätt göra en liten gisnsingsmeny här
    attempts = 2

    print("Guess the atom weight of", name)
    for index, element in enumerate(guess_list):
        print(str(index + 1) + ":" + element)
    while attempts > 0:
        answer = input("Guess: ")
        if answer == str(guess_list.index(weight) + 1):
            break
        attempts -= 1
        if attempts > 0:
            print("You guessed incorrectly.", attempts, " attempts left")
    if attempts > 0:
        print("Good job you guessed it!")
    else:
        print("You didn't manage to guess it correctly, the answer was", index)


"""
import file_reader as fr

a_dict, a_list = fr.get_atoms("avikt.txt")
get_question_weight(a_list, a_dict)"""
