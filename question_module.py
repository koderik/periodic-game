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


def get_alternatives(weight, a_list):
    alt_list = range(1, len(a_list))
    alt_list.popitem(weight)
    ran_index = random.choice(alt_list)
    guess_1 = a_list[ran_index]
    alt_list.popitem(weight)
    ran_index = random.choice(alt_list)
    guess_2 = a_list[ran_index]
    return [guess_1, guess_2, weight]


def get_question_weight(a_list, a_dict):
    weight = random.choice(a_list)
    index = a_list.index(weight)
    name = a_dict[weight]
    guess_list = get_alternatives(weight, a_list)
    random.shuffle(guess_list) # TODO fortsätt göra en liten gisnsingsmeny här
    attempts = 3

    print("Guess the atom weight of", name)
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
