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
def select_word() -> str:
    file = open("hangman_words.txt", "r") # open the file
    file_content = file.read() # read from the file
    words_list = file_content.split() # split into a list
    file.close()
    return random.choice(words_list) # return a random word from the list

# Function to get the player input and check validity
# @param: guessed_letters - a list containing the characters the user has guessed already
#               this list is passed by reference, meaning any changes we make to it in the function
#               will be recorded outside this function
# @param: player_input - a character containing the user input received from pygame; 
#                this parameter will be added in week 4
# @return: string - representing a valid user letter guess 
def get_player_input(guessed_letters:list, player_input:chr) -> str:
    while True: # keep getting the user input until it is a new, valid guess
        # player_input = input("Guess a letter: ") # this was implemented in week 3 but we get rid of it because of pygame!
        if len(player_input) == 1 and player_input.isalpha() and (player_input not in guessed_letters): # player has not guessed this letter yet
            player_input = player_input.lower() # make sure to lowercase it
            guessed_letters.append(player_input) # add it to the guessed_letters list
            return player_input
        # else - invalid guess
        return "" # so just return a blank character

# Function to display how much of the secret word that the user has guessed already
# @param: secret_word - the string containing the secret word to guess
# @param: guessed_letters - a list containing the characters the user has guessed already
# @return: string - representing the word in progress of being guessed
#               underscores represent letters that are still hidden
def build_word_guess(secret_word:str, guessed_letters:list) -> str:
    current_word = "" # create an empty string
    for letter in secret_word: # go through every character in the secret word
        if (letter in guessed_letters): # if that letter has been guessed already
            current_word += str(letter) # add it to the string we want to return
        else: # otherwise
            current_word += "-" # add a dash
    return current_word

# Function to draw the hangman
# @param: wrong_guesses - the number (integer) representing how many guesses the user has gotten wrong
# @return: void
def draw_hangman(wrong_guesses:int):
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
    line_num = 0
    for line in hangman[wrong_guesses].split('\n'):
        print(line)
        label = hangman_drawing.render(line, 1, (255,255,255))
        screen.blit(label, (300, 100+(35*line_num))) # draw at these coords x,y
        line_num += 1
    pygame.display.flip() # update the display
    return # return nothing

# Function to check when the game is over and print whether the user won
# @param: wrong_guesses - the number (integer) representing how many guesses the user has gotten wrong
# @param: secret_word - the string containing the secret word to guess
# @param: guessed_letters - a list containing the characters the user has guessed already
# @return: boolean - representing whether the game is over  
#               True = the game is over 
#               False = the game is not over yet 
def game_over(wrong_guesses:int, secret_word:str, guessed_letters:list) -> bool:
    print("\n")
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 350, 800, 300)) # empty the screen
    game_status = pygame.font.Font(None, 75)
    if (wrong_guesses >= MAX_INCORRECT_GUESSES): # the player guesses wrong too many times
        print("You lose!")
        game_status_label = game_status.render("You lose!", 1, (255,0,0), (0,0,0))
        screen.blit(game_status_label, (300, 450))
        return True
    if set(secret_word) <= set(guessed_letters): # all the letters in the secret word have already been guessed
        print("You win!!!")
        game_status_label = game_status.render("You win!!!", 1, (0,255,0), (0,0,0))
        screen.blit(game_status_label, (300, 450))
        return True
    return False


# MAIN ###################################################################################################
print("*" * 30)
print("WELCOME TO HANGMAN")
print("*" * 30)

# initializing variables to use
secret_word = select_word()
guessed_letters = []
wrong_guesses = 0
is_game_over = False
user_guess = ""


# NEW STUFF WITH PYGAME
hangman_drawing = pygame.font.Font(None, 50)
word_drawing = pygame.font.Font(None, 50)
guesses_drawing = pygame.font.Font(None, 35)

# draw the initial hangman and text
draw_hangman(wrong_guesses); 
secret_word_text = build_word_guess(secret_word, guessed_letters)
print(secret_word_text)
word_label = word_drawing.render(secret_word_text, 1, (255,255,255), (0,0,0))
screen.blit(word_label, (300, 50))
pygame.display.flip() # update the display

while True: # loop for pygame
    # event handling -- nothing too major
    for event in pygame.event.get():
        # keep going until the game is over!
        # or if we manually exit the game
        if is_game_over or event.type == pygame.QUIT:
            # game is over so reveal the secret word!
            draw_hangman(wrong_guesses) # draw hangman one last time
            
            # let the user know what the secret word is
            print("The secret word was " + secret_word)
            word_label = word_drawing.render(secret_word, 1, (255,255,255), (0,0,0))
            screen.blit(word_label, (300, 50))

            pygame.display.flip() # update the display

            pygame.time.wait(1000) # wait 1 second before closing the game
            pygame.quit() # quit pygame

        # detect user guess
        if event.type == pygame.KEYDOWN:
            user_guess = event.unicode # get the key pressed

            user_guess = get_player_input(guessed_letters, user_guess) # validate user guess
            if user_guess != "": # if user guess valid
                if user_guess not in secret_word: 
                    wrong_guesses += 1 # increment the number of wrong guesses
            # else: # user guess invalid so do nothing
            
            draw_hangman(wrong_guesses); # draw the hangman

            # printing the progress of the word being guessed
            secret_word_text = build_word_guess(secret_word, guessed_letters)
            print(secret_word_text)
            word_label = word_drawing.render(secret_word_text, 1, (255,255,255), (0,0,0))
            screen.blit(word_label, (300, 50))

            # print the list of guesses the player has already guessed
            print("Guessed letters: " + str(sorted(guessed_letters))) 
            guesses_label = guesses_drawing.render(str(sorted(guessed_letters)), 1, (255,255,255), (0,0,0))
            screen.blit(guesses_label, (200, 450))

            pygame.display.flip() # update the display

            # set the variable to determine if the game is over
            is_game_over = game_over(wrong_guesses, secret_word, guessed_letters) 