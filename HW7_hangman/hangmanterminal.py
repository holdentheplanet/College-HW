# Name: Holden Moore
# hangmanterminal.py
#
# Problem: Execution point for a headless instance of Hangman
# Certification of Authenticity:
# I certify that this lab is entirely my own work. 

from hangmancore import *
from time import sleep
import os

def display(health):
    if health == 7:
        print(f"Save Mrs. Stalvey!!!")
        print(f"-----------")
        print(f"     |     ")
        print(f"     o     ")
        print(f"           ")
        print(f"           ")
    if health == 6:
        print(f"-----------")
        print(f"     |     ")
        print(f"     o     ")
        print(f"           ")
        print(f"    /      ")
    if health == 5:
        print(f"-----------")
        print(f"     |     ")
        print(f"     o     ")
        print(f"           ")
        print(f"    /\\    ")
    if health == 4:
        print(f"-----------")
        print(f"     |     ")
        print(f"     o     ")
        print(f"   --      ")
        print(f"    /\\    ")
    if health == 3:
        print(f"-----------")
        print(f"     |     ")
        print(f"     o     ")
        print(f"   --|     ")
        print(f"    /\\    ")
    if health == 2:
        print(f"-----------")
        print(f"     |     ")
        print(f"     o     ")
        print(f"   --|--   ")
        print(f"    /\\    ")
    if health == 1:
        print(f"-----------")
        print(f"     |     ")
        print(f"     0     ")
        print(f"   --|--   ")
        print(f"    /\\    ")
    if health == 0:
        print(f"-----------")
        print(f"     |     ")
        print(f"   (x-x)   ")
        print(f"   --|--   ")
        print(f"    /\\    ")

def playGame():
    secret = randomWord(readWords())
    guessedLetters = ['']
    blank = blanks(secret, guessedLetters)
    health = 7
    while ((not isWon(blank)) and health > 0):
        display(health)
        print(blanks(secret, guessedLetters))
        print(f"Already Guessed: {guessedLetters[1::]}")
        getGuess(guessedLetters)
        if blank == blanks(secret, guessedLetters):
            health -= 1 #docks health only for incorrect guess
        blank = blanks(secret, guessedLetters)
        os.system('cls')
    if isWon(blank):
        print("CONGLATURATION!")
        print(f"     O  ^     ")
        print(f"   --|--[3    ")
        print(f"    /\\       ")
        return True
    else:
        display(health)
        print(f"The word was {secret}.")
        sleep(2)
        lose1 = "Where were you when Mrs. Stalvey die?"
        lose2 = "I was at house eating dorito when phone ring"
        lose3 = "\"Mrs. Stalvey is kil\""
        lose4 = "\"no\""
        losestrs = [lose1, lose2, lose3, lose4]
        displaystr = ""
        for string in losestrs:
            for char in string:
                displaystr += char
                print(displaystr)
                sleep(1/16)
                os.system('cls')
            displaystr = ""
            sleep(2)
        return False

def main():
    again = True
    score = 0
    while(again):
        if playGame():
            score += 1
        else:
            score = 0
        print(f"Score: {score}")
        again = input("Would you like to play again? yes/no: ")
        if again.lower() == "no" or again.lower() == "n":
            again = False
        os.system('cls')

main()