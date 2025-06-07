# HANGMAN
# Arrayscape Gaming 2025
# Developed by Josephine Lee
# Inspiration: https://realpython.com/python-hangman/
###################################################################################################

# INITIALIZING ###################################################################################################
import random # a built-in module for random choice
import pygame

pygame.init() # initialize pygame and
screen = pygame.display.set_mode((800, 600)) # create a new display
screen.fill(0)
pygame.display.set_caption("HANGMAN")

MAX_INCORRECT_GUESSES = 6 # create a global variable containing the max number of incorrect guesses

# FUNCTIONS ###################################################################################################

# Function to select a random word from the file
# Assume every line in the file is a unique choice and is in all lowercase
# @return: string - representing a random word selected from the file
def selectWord() -> str:
    file = open("hangmanWords.txt", "r") # open the file
    fileContent = file.read() # read from the file
    wordsList = fileContent.split() # split into a list
    file.close()
    return random.choice(wordsList) # return a random word from the list

# Function to get the player input and check validity
# @param: guessedLetters - a list containing the characters the user has guessed already
#               this list is passed by reference, meaning any changes we make to it in the function
#               will be recorded outside this function
# @param: playerInput - a character containing the user input received from pygame; 
#                this parameter will be added in week 4
# @return: string - representing a valid user letter guess 
def getPlayerInput(guessedLetters:list, playerInput:chr) -> str:
    while True: # keep getting the user input until it is a new, valid guess
        # playerInput = input("Guess a letter: ") # this was implemented in week 3 but we get rid of it because of pygame!
        if len(playerInput) == 1 and playerInput.isalpha() and (playerInput not in guessedLetters): # player has not guessed this letter yet
            playerInput = playerInput.lower() # make sure to lowercase it
            guessedLetters.append(playerInput) # add it to the guessedLetters list
            return playerInput
        # else - invalid guess
        return "" # so just return a blank character

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
            currentWord += "-" # add a dash
    return currentWord

# Function to draw the hangman
# @param: wrongGuesses - the number (integer) representing how many guesses the user has gotten wrong
# @return: void
def drawHangman(wrongGuesses:int):
    # empty the drawing by covering it with a rectangle
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 800, 300)) 
    hangman = [ # storing the drawings of the different phases of hangman
r"""
______
 |   |
 |   
 |  
 |  
 |________
""",
r"""
______
 |   |
 |   O
 |  
 |  
 |________
""",
r"""
______
 |   |
 |   O
 |   |
 |  
 |________
""",
r"""
______
 |   |
 |   O
 |  /|
 |  
 |________
""",
r"""
______
 |   |
 |   O
 |  /|\
 |  
 |________
""",
r"""
______
 |   |
 |   O
 |  /|\
 |  /
 |________
""",
r"""
______
 |   |
 |   O
 |  /|\
 |  / \
 |________
"""]
    # print out the hangman depending on how many wrong guesses the user has had
    # break it up per line since render only renders one line at a time
    lineNum = 0
    for line in hangman[wrongGuesses].split('\n'):
        print(line)
        label = hangmanDrawing.render(line, 1, (255,255,255))
        screen.blit(label, (300, 100+(35*lineNum))) # draw at these coords x,y
        lineNum += 1
    pygame.display.flip() # update the display
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
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 350, 800, 300)) # empty the screen
    gameStatus = pygame.font.Font(None, 75)
    if (wrongGuesses >= MAX_INCORRECT_GUESSES): # the player guesses wrong too many times
        print("You lose!")
        gameStatusLabel = gameStatus.render("You lose!", 1, (255,0,0), (0,0,0))
        screen.blit(gameStatusLabel, (300, 450))
        return True
    if set(secretWord) <= set(guessedLetters): # all the letters in the secret word have already been guessed
        print("You win!!!")
        gameStatusLabel = gameStatus.render("You win!!!", 1, (0,255,0), (0,0,0))
        screen.blit(gameStatusLabel, (300, 450))
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
userGuess = ""


# NEW STUFF WITH PYGAME
hangmanDrawing = pygame.font.Font(None, 50)
wordDrawing = pygame.font.Font(None, 50)
guessesDrawing = pygame.font.Font(None, 35)

# draw the initial hangman and text
drawHangman(wrongGuesses); 
secretWordText = buildWordGuess(secretWord, guessedLetters)
print(secretWordText)
wordLabel = wordDrawing.render(secretWordText, 1, (255,255,255), (0,0,0))
screen.blit(wordLabel, (300, 50))
pygame.display.flip() # update the display

while True: # loop for pygame
    # event handling -- nothing too major
    for event in pygame.event.get():
        # keep going until the game is over!
        # or if we manually exit the game
        if isGameOver or event.type == pygame.QUIT:
            # game is over so reveal the secret word!
            drawHangman(wrongGuesses) # draw hangman one last time
            
            # let the user know what the secret word is
            print("The secret word was " + secretWord)
            wordLabel = wordDrawing.render(secretWord, 1, (255,255,255), (0,0,0))
            screen.blit(wordLabel, (300, 50))

            pygame.display.flip() # update the display

            pygame.time.wait(1000) # wait 1 second before closing the game
            pygame.quit() # quit pygame

        # detect user guess
        if event.type == pygame.KEYDOWN:
            userGuess = event.unicode # get the key pressed

            userGuess = getPlayerInput(guessedLetters, userGuess) # validate user guess
            if userGuess != "": # if user guess valid
                if userGuess not in secretWord: 
                    wrongGuesses += 1 # increment the number of wrong guesses
            # else: # user guess invalid so do nothing
            
            drawHangman(wrongGuesses); # draw the hangman

            # printing the progress of the word being guessed
            secretWordText = buildWordGuess(secretWord, guessedLetters)
            print(secretWordText)
            wordLabel = wordDrawing.render(secretWordText, 1, (255,255,255), (0,0,0))
            screen.blit(wordLabel, (300, 50))

            # print the list of guesses the player has already guessed
            print("Guessed letters: " + str(sorted(guessedLetters))) 
            guessesLabel = guessesDrawing.render(str(sorted(guessedLetters)), 1, (255,255,255), (0,0,0))
            screen.blit(guessesLabel, (200, 450))

            pygame.display.flip() # update the display

            # set the variable to determine if the game is over
            isGameOver = gameOver(wrongGuesses, secretWord, guessedLetters) 