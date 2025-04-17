# HANGMAN
# Arrayscape Gaming 2025
# Developed by Josephine Lee
# Inspiration: https://realpython.com/python-hangman/
###################################################################################################

# INITIALIZING ###################################################################################################
import random # a built-in module for random choice

MAX_INCORRECT_GUESSES = 6 # create a global variable containing the max number of incorrect guesses

# FUNCTIONS ###################################################################################################

# Function to select a random word from the file
# Assume every line in the file is a unique choice and is in all lowercase
# @return: string - representing a random word selected from the file
def selectWord() -> str:
    file = open("hangmanWords.txt", "r") # open the file
    fileContent = file.read() # read from the file
    wordsList = fileContent.splitlines() # split the content based on the lines
    file.close()
    return random.choice(wordsList) # return a random word from the list

# Function to get the player input
# @param: guessedLetters - a list containing the characters the user has guessed already
#               this list is passed by reference, meaning any changes we make to it in the function
#               will be recorded outside this function
# @return: string - representing a valid user letter guess 
def getPlayerInput(guessedLetters:list) -> str:
    while True: # keep getting the user input until it is a new, valid guess
        playerInput = input("Guess a letter: ")
        playerInput = playerInput.lower() # make sure to lowercase it
        if len(playerInput) == 1 and playerInput.isalpha() and (playerInput not in guessedLetters): # player has not guessed this letter yet
            guessedLetters.append(playerInput) # add it to the guessedLetters list
            return playerInput

# Function to display how much of the secret word that the user has guessed already
# @param: secretWord - the string containing the secret word to guess
# @param: guessedLetters - a list containing the characters the user has guessed already
# @return: string - representing the word in progress of being guessed
#               underscores represent letters that are still hidden
def buildWordGuess(secretWord:str, guessedLetters:list) -> str:
    currentWord = "" # create an empty string
    for letter in secretWord: # go through every character in the secret word
        if (letter in guessedLetters): # if that letter has been guessed already
            currentWord += str(letter) # add it to the string we want to return
        else: # otherwise
            currentWord += "_" # add an underscore
    return currentWord

# Function to draw the hangman
# @param: wrongGuesses - the number (integer) representing how many guesses the user has gotten wrong
# @return: void
def drawHangman(wrongGuesses:int):
    hangman = [ # storing the drawings of the different phases of hangman
r"""
------
 |   |
 |   
 |  
 |  
 |________
""",
r"""
------
 |   |
 |   O
 |  
 |  
 |________
""",
r"""
------
 |   |
 |   O
 |   |
 |  
 |________
""",
r"""
------
 |   |
 |   O
 |  /|
 |  
 |________
""",
r"""
------
 |   |
 |   O
 |  /|\
 |  
 |________
""",
r"""
------
 |   |
 |   O
 |  /|\
 |  /
 |________
""",
r"""
------
 |   |
 |   O
 |  /|\
 |  / \
 |________
"""]
    print(hangman[wrongGuesses]) # print out the hangmand depending on how many wrong guesses the user has had
    return # return nothing

# Function to check when the game is over and print whether the user won
# @param: wrongGuesses - the number (integer) representing how many guesses the user has gotten wrong
# @param: secretWord - the string containing the secret word to guess
# @param: guessedLetters - a list containing the characters the user has guessed already
# @return: boolean - representing whether the game is over  
#               True = the game is over 
#               False = the game is not over yet 
def gameOver(wrongGuesses:int, secretWord:str, guessedLetters:list) -> bool:
    print("\n")
    if (wrongGuesses >= MAX_INCORRECT_GUESSES): # the player guesses wrong too many times
        print("You lose!")
        return True
    if set(secretWord) <= set(guessedLetters): # all the letters in the secret word have already been guessed
        print("You win!!!")
        return True
    return False


# MAIN ###################################################################################################
print("*" * 30)
print("WELCOME TO HANGMAN")
print("*" * 30)

# initializing variables to use
secretWord = selectWord()
guessedLetters = []
wrongGuesses = 0
isGameOver = False

drawHangman(wrongGuesses); # draw the initial hangman
while not isGameOver: # keep going until the game is over!
    print(buildWordGuess(secretWord, guessedLetters)) # printing the progress of the word being guessed
    userGuess = getPlayerInput(guessedLetters)
    if userGuess not in secretWord:
        wrongGuesses += 1 # increment the number of wrong guesses
    print("Guessed letters: " + str(sorted(guessedLetters))) # print the list of guesses the player has already guessed
    drawHangman(wrongGuesses); # draw the hangman
    isGameOver = gameOver(wrongGuesses, secretWord, guessedLetters) # set the variable to determine if the game is over

# game is over so reveal the secret word!
print("The secret word was " + secretWord)