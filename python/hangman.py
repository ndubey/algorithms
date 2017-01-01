import random

def printIntro():
    print("H A N G M A N")

def printH(lineNum, h):
    if lineNum == 1:
        if h == 1:
            print("   O  |")
        else:
            print("      |")
    if lineNum == 2:
        if h == 1:
            print("   |  |")
        else:
            print("      |")
    if lineNum == 3:
        if h==1:
            print("   |  |")
        elif h == 2:
            print("  /|  |")
        elif h == 3:
            print("  /|\ |")
        else:
            print("      |")
    if lineNum == 4:
        if h == 1:
            print("  /   |")
        if h == 2:
            print("  /\  |")
        else:
            print("      |")


def drawHangman(state):
    print("  +------+")
    print("   |  |")
    if state == 0:
        printH(1,0)
        printH(2,0)
        printH(3,0)
        printH(4,0)
    elif state == 1:
        printH(1,1)
        printH(2,0)
        printH(3,0)
        printH(4,0)
    elif state == 2:
        printH(1,1)
        printH(2,1)
        printH(3,0)
        printH(4,0)
    elif state == 3:
        printH(1,1)
        printH(2,1)
        printH(3,1)
        printH(4,0)
    elif state == 4:
        printH(1,1)
        printH(2,1)
        printH(3,2)
        printH(4,0)
    elif state == 5:
        printH(1,1)
        printH(2,1)
        printH(3,3)
        printH(4,0)
    elif state == 6:
        printH(1,1)
        printH(2,1)
        printH(3,3)
        printH(4,1)
    elif state == 7:
        printH(1,1)
        printH(2,1)
        printH(3,3)
        printH(4,2)

    print("      |")
    print("==========")


def getRandomTvSeries(tvSeriesList):
    wordIndex = random.randint(0,len(tvSeriesList)-1)
    return tvSeriesList[wordIndex]

def blankName(name):
    blanks = []
    for char in name:
        if char == " ":
            blanks.append(" ")
        else:
            blanks.append("_")
    return blanks

def processInput(letter, name, guessed):
    index = 0
    correct = False
    for char in name:
        if char == letter:
            #correct guess
            guessed[index] = letter
            correct = True
        index += 1
    return correct,guessed

def isFinished(guessed, state):
    if state == 7:
        return True
    elif "_" in guessed:
        return False
    return True

def playHangmanIsLost(name):
    state = 0
    finished = False
    guessed = blankName(name)
    print("Missed letters:")
    print("".join(guessed))
    print("Guess a letter")
    letter = input()
    letter = letter.capitalize()
    letter = letter[0:1]
    missed=[]
    
    while not finished:
        (found,guessed) = processInput(letter, name, guessed)
        if not found:
            state += 1
            missed.append(letter)
        drawHangman(state)
        print("Missed letters:", end=' :  ')
        print(",".join(missed))
        print()
        print("".join(guessed))
        finished = isFinished(guessed, state)
        if not finished:
            print("Guess next letter")
            letter = input()
            letter = letter.upper()
            letter = letter[0:1]

    if state >= 7:
        return True
    else:
        return False


tvSeries=["THE SOPRANOS", "SEINFELD", "CHEERS", "GLEE", "2 BROKE GIRLS", "SEX AND THE CITY","COUGAR TOWN", "ROYAL PAINS", "TWO AND A HALF MEN","SUBURGATORY", "HEROES", "NEW GIRL", "SCANDAL","ARROW",\
           "ELEMENTARY","BONES","FRIENDS", "TRIPLING", "GAME OF THRONES", "VIKINGS", "THE FLASH", "GILMORE GIRLS", "PRISON BREAK","THE CROWN", "THE BIG BANG THEORY", "THE VAMPIRE DIARIES", \
          "BREAKING BAD", "MODERN FAMILY", "PLANET EARTH", "SUITS","HOMELAND", "HOUSE OF CARDS", "THE OFFICE", "HOW I MET YOUR MOTHER","QUANTICO", "FARGO", "THE SIMPSONS", "LOST", "WALKING DEAD", \
         "AMERICAN IDOL"]
animals = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.upper().split()

start = 'yes'
while start == 'yes':
    printIntro()
    drawHangman(0)
    print("Kind of game 1. Animals name 2. tv-series names 1/2:")
    answer = input()
    if answer == '2':
        print("Let us play hangman with English tv-series")
        name = getRandomTvSeries(tvSeries)
    else:
        print("Let us play hangman with English Animal Names")
        name = getRandomTvSeries(animals)

    isLost = playHangmanIsLost(name)
    if isLost:
        print("Ha ha ha ha You Lost! Better next time.")
        print("By the way I was thinking of '"+name+"'")
    else:
        print("Bravo!! You won. ")
        if answer == 1:
            print("You smart fella'")
        else:
            print("You do some serious time waste on series.")


    print("Play another yes/no:")
    start = input()


