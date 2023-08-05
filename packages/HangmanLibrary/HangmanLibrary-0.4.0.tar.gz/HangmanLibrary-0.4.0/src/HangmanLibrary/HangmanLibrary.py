from random import choice

def ChooseRandomWord(listOfWords) -> str:
    try:
        return choice(listOfWords)
    except Exception as e:
        print("Some error has occurred: ", e)


def PrintShowcase(listOfRightLetters, word) -> str:
    Showcase = ""
    for x in word:
        if listOfRightLetters.__contains__(x):
            Showcase += x + " "
        else:
            Showcase += "_ "
            
    return Showcase

def VerifyWin(Showcase, word):
    if not Showcase.__contains__("_"):
        return True
    else:
        return False

def VerifyIfEnoughAttempts(attempts):
    if attempts == 0:
        return True
    else:
        return False

def VerifyIfLetterInWord(word, letter, listOfRightLetters, attempts, listOfUsedLetters = False):
    if word.__contains__(letter):
            for x in range(len(word)):
                if word[x] == letter:
                        listOfRightLetters.append(letter)
                        return True
    else:
        attempts -= 1
        if listOfUsedLetters != False:
            if not listOfUsedLetters.__contains__(letter):
                    listOfUsedLetters.append(letter)
        return False
