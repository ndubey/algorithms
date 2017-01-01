#I am thinking of a 3-digit number. Try to guess what it is.
#Here are some clues:
#When I say:    That means:
#Pico         One digit is correct but in the wrong position.
#Fermi        One digit is correct and in the right position.
#Bagels       No digit is correct.
#I have thought up a number. You have 10 guesses to get it.
#Guess #1:
#123
#Fermi
#Guess #2:
#145
#Fermi Fermi

import random

def printIntro():
    print("B A G E L S")

    print("3 digit number guessing game")


#all three digits should be unique
def aRandomNumber():
    li = list(range(1,9))
    firstIndex = random.randint(0,8)
    firstDigit = li[firstIndex]
    li[firstIndex] = 0
    secondIndex = random.randint(0,8)
    secondDigit = li[secondIndex]
    del li[secondIndex]
    thirdIndex = random.randint(0,7)
    thirdDigit = li[thirdIndex]
    return [firstDigit,secondDigit,thirdDigit]

def isFermi(guess, num):
    numFermi = 0
    if guess[0] == str(num[0]):
        numFermi+=1
    if guess[1] == str(num[1]):
        numFermi+=1
    if guess[2] == str(num[2]):
        numFermi+=1
    return numFermi

def isPico(guess, num):
    numPico = 0
    if guess[0] == str(num[1]) or guess[0] == str(num[2]):
        numPico += 1
    if guess[1] == str(num[0]) or guess[1] == str(num[2]):
        numPico += 1
    if guess[2] == str(num[0]) or guess[2] == str(num[1]):
        numPico += 1
    return numPico


def processGuess(guess, num):
    anything = False
    numFermi = isFermi(guess,num)
    if numFermi == 3:
        print("You got it!")
        return True
    if numFermi > 0:
        print("Fermi "*numFermi, end=' ')
        anything = True
    numPico = isPico(guess,num)
    if numPico > 0:
        print("Pico "*numPico, end=' ')
        anything = True
    if not anything:
        print("Bagles", end=' ')
    print()
    return False
    

playAgain = 'yes'


while playAgain == 'yes':
    print("I am thinking of a randome 3 digit number guess it")
    num = aRandomNumber()
    for i in range(0,9):
        guess = input()
        if processGuess(guess,num):
            break
        if i == 9:
            print("You lost! I was thinking of number: " + "".join(num))


    print("You want to play again yes/no:")
    playAgain = input()

