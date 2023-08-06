from random import choice

def ChooseRandomWord(listOfWords) -> str:
    """
    Chooses a random word from a specified list of words and returns the word. If the list of words is empty, it will return an error
    """
    try:
        return choice(listOfWords)
    except Exception as e:
        print("Some error has occurred: ", e)

def PrintShowcase(listOfRightLetters, word) -> str:
    """
    Creates and returns a string that serves as a place holder for the letters based on the word. It will check the letters already gotten right and place them.
    """
    Showcase = ""
    for x in word:
        if listOfRightLetters.__contains__(x):
            Showcase += x + " "
        else:
            Showcase += "_ "
            
    return Showcase

def VerifyWin(Showcase):
    """
    Verifies if the player has won or not based on the Showcase variable.
    """
    return not Showcase.__contains__("_")

def VerifyIfEnoughAttempts(attempts):
    """
    Verifies if the player has enough attempts
    """
    return attempts == 0


def VerifyIfLetterInWord(word, letter, listOfRightLetters, attempts, listOfUsedLetters = False):
    """
    Verifies if the guessed letter is in the word. It will also update the list with the already guesses letters as well as the remaining attempts and, if the program needs it, the list with the wrong guesses letters. If it does contain the letter, it will return True
    """
    if word.__contains__(letter):
            for x in range(len(word)):
                if word[x] == letter:
                        listOfRightLetters.append(letter)
                        return True
    else:
        attempts = attempts - 1 
        if listOfUsedLetters != False:
            if not listOfUsedLetters.__contains__(letter):
                    listOfUsedLetters.append(letter)
        return False
