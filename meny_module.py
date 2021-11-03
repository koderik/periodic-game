import sys
import file_reader as fr
import question_module as que
import game_window as game


a_dict = {}
a_list = []


def meny_print():
    print("Number, Name, Weight:")
    for index, element in enumerate(a_list):
        print(index + 1, a_dict[element], element)


def meny_practice_numbers():
    for i in range(3):
        que.get_question_number(a_list, a_dict)


def meny_practice_names():
    for i in range(3):
        que.get_question_name(a_list, a_dict)


def meny_practice_weights():
    for i in range(3):
        que.get_question_weight(a_list, a_dict)


def meny_start_game():
    Game = game.Game_window()


def meny_exit():
    print("Exiting...")
    sys.exit()


def print_meny():
    print("-------------- MENY ---------------")
    print("1. Visa alla atomer")
    print("2. Träna på atomnummer")
    print("3. Träna på atombeteckningar")
    print("4. Träna på atomvikter")
    print("5. Starta spelet")
    print("6. Sluta")
    print("-----------------------------------")


def meny():
    global a_dict, a_list
    a_dict, a_list = fr.get_atoms("avikt.txt")
    items = {
        "1": meny_print,
        "2": meny_practice_numbers,
        "3": meny_practice_names,
        "6": meny_exit,
        "5": meny_start_game,
        "4": meny_practice_weights,
    }
    ans = ""
    print_meny()
    while True:
        ans = input("Vad vill du göra? ")
        if ans in items.keys():
            items[ans]()
            print_meny()
        else:
            print("Välj alternativ ur menyn")
