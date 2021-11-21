import os
import random
from typing import Annotated


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


letters = list("ABCD")
simon_lijst = []
highscore = 0

while True:
    letters_gekozen = random.choice(letters)
    simon_lijst.append(letters_gekozen)
    print("remember these letters: ", *simon_lijst)

    enter = input("press enter to start the game")
    if enter == " ":
        clear()

    antwoord = input("type the right letters: ")
    for index, a in enumerate(simon_lijst):
        if antwoord[index] == a:
            if index == len(simon_lijst) - 1:
                print("correct")

        else:
            clear()
            score = len(simon_lijst)
            print("you're wrong: ", *simon_lijst)
            print("the score is: ", score - 1)

            if score - 1 > highscore:
                highscore = score - 1
                print("new highscore")

            retry = input("wanne play? [y/n] : ")
            if retry == "y":
                simon_lijst.clear()
                clear()
                break
            else:
                exit()
