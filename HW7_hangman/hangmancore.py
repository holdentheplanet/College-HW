# Name: Holden Moore
# hangmancore.py
#
# Problem: Creates the internal logic necessary for a hangman game. Not intended for execution. See the other files.
# Certification of Authenticity:
# I certify that this lab is entirely my own work. 

from graphics import *
import random as r
import os
from time import sleep
# Hangman logic

def readWords(file="wordlist.txt"):
    wordFile = open(file, "r")
    wordList = []
    line = wordFile.readline()
    while(line != ""):
        words = line.split()
        i = 0
        while(i < len(words)):
            wordList.append(str(words[i]))
            i += 1
        line = wordFile.readline()
    return wordList

def randomWord(words):
    selection = r.randint(0, len(words))
    return words[selection]

def getGuess(guessedLetters): 
    guess = ""
    while ((guess in guessedLetters) or (len(guess) != 1)):
        guess = input("Enter letter: ")
    guess = guess.lower()
    if ((guess not in guessedLetters) and len(guess) == 1):
        guessedLetters.append(guess)

def blanks(word, guessedLetters):
    # go through each character of word, see if it matches each character of guessedLetters
    blank = ""
    for i in range(len(word)):
        if word[i] in guessedLetters:
            blank += word[i] + " "
        else:
            blank += "_ "
    return blank

def isWon(blank):
    return blank.find("_") == -1 # The absence of underscores implies that every letter has been uncovered

