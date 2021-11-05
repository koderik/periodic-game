import sys
import file_reader as fr
import question_module as que
import game_window as g_w
import atom_list_window as a_w
import question_window as q_w
from atom import *



def meny_print():
    a_win = a_w.Atom_list_window(a_list)


def meny_practice_numbers():
    q_win = q_w.Question_frame(a_list, "number")


def meny_practice_names():
    q_win = q_w.Question_frame(a_list, "name")


def meny_practice_weights():
    for i in range(3):
        que.get_question_weight(a_list, a_dict)


def meny_start_game():
    Game = g_w.Game_window(a_list)


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


a_list = Atom_list()
a_list.get_atoms("avikt.txt", "period_coord.txt")
meny()
