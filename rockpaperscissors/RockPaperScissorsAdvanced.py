# ROCK PAPER SCISSORS - Advanced Solution using dictionaries and funtions
# Arrayscape Gaming 2025
# Developed by Josephine Lee
###################################################################################################

# INITIALIZING ###################################################################################################
import random # a built-in module to generate random numbers

# a dictionary containing the first letter
#   key: a letter representing the choice of rock, paper, or scissors
#   value: the word associated with the letter
choiceDict = {'r': "rock", 'p': "paper", 's': "scissors"}

# a dictionary containing pairs of possible combinations of choices
#   key: the winner
#   value: the loser
winnerDict = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# a string containing the prompt to prompt the user for an input
prompt = "Type the letters for your choice: \n\t \'r\' for rock \n\t \'p\' for paper \n\t \'s\' for scissors \n\t 'q' for quit\n"

# FUNCTIONS ###################################################################################################
# Function for the bot to randomly choose a choice
# @return: String - representing the choice of the bot 
def botChooses():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices) # choose a random choice

# MAIN GAME ###################################################################################################
print("*" * 30)
print("WELCOME TO ROCK PAPER SCISSORS")
print("*" * 30)

userInput = input(prompt) # get the input from the user
userInput = userInput.lower()
while userInput != 'q' and userInput != "quit": # the program quits if the user inputs 'q' or 'quit'
    if userInput not in choiceDict:
        print("\nPlease input a valid choice")
        userInput = input(prompt)
        continue # skip over to the next while loop

    userInput = choiceDict[userInput] # get the word of the user's choice
    botChoice = botChooses() # save the bot choice

    # checking who won
    if userInput == botChoice:
        print("TIE")
    elif botChoice == winnerDict[userInput]: # the bot's choice matches the loser of the pair
        print("YOU WIN")
    else:
        print("YOU LOSE")

    print("\tYou chose " + userInput + ".\t Bot chose " + botChoice + ".\n") # output what each player chose
    userInput = input(prompt) # reprompt the user

# quit while loop and end game
print("THANK YOU FOR PLAYING ROCK PAPER SCISSORS\n")