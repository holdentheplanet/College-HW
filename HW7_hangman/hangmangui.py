from hangmancore import *
from graphics import *
# Name: Holden Moore
# hangmangui.py
#
# Problem: Handles and serves as a execution point for the graphical variation of the game
# Certification of Authenticity:
# I certify that this lab is entirely my own work. 

def drawBlanks(Blank, blank, win):
    Blank.undraw()
    Blank.setText(blank)
    Blank.draw(win)
    return Blank

   
def drawHealth(head,
               torso,armLeft,armRight,
               legLeft, legRight, deadHead,
               win,health):

    head.undraw()
    torso.undraw()
    armLeft.undraw()
    armRight.undraw()
    legLeft.undraw()
    legRight.undraw()

 
    if health < 7:
        head.draw(win)
    if health < 6:
        torso.draw(win)
    if health < 5:
        armLeft.draw(win)
    if health < 4:
        armRight.draw(win)
    if health < 3:
        legLeft.draw(win)
    if health < 2:
        legRight.draw(win)
    if health < 1:
        head.undraw(win)
        deadHead.draw(win)

def getGuessGraphical(win, guessedLetters):
    key = win.getKey()
    if key not in guessedLetters:
        guessedLetters.append(key)

def playGraphical(): # This is a disgusting function and I am frankly embarassed you have to read it
    again = True
    win = GraphWin("Hangman", 400, 400)
    while(again): # Portion between this and the next while loop initializes the game
        guessedLetters = []
        guessed = Text(Point(200, 380), f"{guessedLetters}")
        secret = randomWord(readWords())
        guessed.draw(win)
        health = 7
        Blank = Text(Point(200, 350), '') # Initializing graphics objects and drawing them
        post = Image(Point(300, 160), "gallows.gif")
        noose = Line(Point(20, 20), Point(400, 399))
        head = Image(Point(230,170), 'head.png')
        torso = Line(Point(230,190), Point(230,220))
        torso.setWidth(4)
        armLeft = Line(Point(230, 200), Point(200, 200))
        armLeft.setWidth(2)
        armRight = Line(Point(230, 200), Point(260, 200))
        armRight.setWidth(2)
        legLeft = Line(Point(230, 220), Point(215, 260))

        legRight = Line(Point(230, 220), Point(245, 260))
        deadHead = Image(Point(230, 170), 'deadhead.png')
        splash = Text(Point(230, 20), f"Save Mrs. Stalvey!")
        splash.draw(win)
        post.draw(win)
        blank = blanks(secret, guessedLetters) # lowerbase blank refers to the string, uppercase Blank is the graphics obj
        while ((not isWon(blank)) and health > 0): 
            guessed.undraw()
            guessed.setText(f"Guessed: {guessedLetters}") #Updates list of guessed letters
            guessed.draw(win)
            drawHealth(head, # Recalculates gallows display
                   torso,armLeft,armRight,
                   legLeft, legRight, deadHead,
                   win, health)
            drawBlanks(Blank, blank, win) 
            getGuessGraphical(win, guessedLetters)
            if blank == blanks(secret, guessedLetters):
                health -= 1
            blank = blanks(secret, guessedLetters)
        if isWon(blank):
            blank = secret
            drawBlanks(Blank, blank, win)
            splash.setText("you're winner!")
            post.undraw()
            head.undraw()
            torso.undraw()
            armLeft.undraw()
            armRight.undraw()
            legLeft.undraw()
            legRight.undraw()

            head.draw(win)
            torso.draw(win)
            armLeft.draw(win)
            armRight.draw(win)
            legLeft.draw(win)
            legRight.draw(win)
        else:
            blank = f"The word was {secret}"
            drawBlanks(Blank, blank, win)
            head.undraw()
            deadHead.draw(win)
        guessed.undraw()
        againButton = Rectangle(Point(20,50), Point(170,100))
        againText = Text(Point(100,75), "Play again button!")
        againText.setSize(12)
        notAgainButton = Rectangle(Point(20, 120), Point(170, 170))
        notAgainText = Text(Point(100, 145), "This game sucks!")
        againButton.draw(win)
        againText.draw(win)
        notAgainButton.draw(win)
        notAgainText.draw(win)
        decision = False
        while not decision: # I can't believe this is how buttons actually work
            clickPoint = win.getMouse()
            if ((clickPoint.getX() > 20 and clickPoint.getX() < 170) and clickPoint.getY() > 120 and clickPoint.getY() < 170):
                again = False
                decision = True
            elif ((clickPoint.getX() > 20 and clickPoint.getX() < 170) and clickPoint.getY() > 50 and clickPoint.getY() < 100):
                again = True
                decision = True
            else:
                decision = False
        splash.undraw()
        head.undraw()
        torso.undraw()
        armLeft.undraw()
        armRight.undraw()
        legLeft.undraw()
        legRight.undraw()
        Blank.undraw()
        deadHead.undraw()
        againButton.undraw()
        againText.undraw()
        notAgainButton.undraw()
        notAgainText.undraw()
    

def main():
    playGraphical()

main()
