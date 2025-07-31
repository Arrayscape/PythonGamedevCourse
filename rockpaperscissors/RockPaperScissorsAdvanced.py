# ROCK PAPER SCISSORS - Advanced Solution using dictionaries and funtions
# Arrayscape Gaming 2025
# Developed by Josephine Lee
###################################################################################################

# INITIALIZING ###################################################################################################
import random # a built-in module to generate random numbers

# a dictionary containing the first letter
#   key: a letter representing the choice of rock, paper, or scissors
#   value: the word associated with the letter
choice_dict = {'r': "rock", 'p': "paper", 's': "scissors"}

# a dictionary containing pairs of possible combinations of choices
#   key: the winner
#   value: the loser
winner_dict = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# a string containing the prompt to prompt the user for an input
prompt = "Type the letters for your choice: \n\t \'r\' for rock \n\t \'p\' for paper \n\t \'s\' for scissors \n\t 'q' for quit\n"

# FUNCTIONS ###################################################################################################
# Function for the bot to randomly choose a choice
# @return: String - representing the choice of the bot 
def bot_chooses():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices) # choose a random choice

# MAIN GAME ###################################################################################################
print("*" * 30)
print("WELCOME TO ROCK PAPER SCISSORS")
print("*" * 30)

user_input = input(prompt) # get the input from the user
user_input = user_input.lower()
while user_input != 'q' and user_input != "quit": # the program quits if the user inputs 'q' or 'quit'
    if user_input not in choice_dict:
        print("\nPlease input a valid choice")
        user_input = input(prompt)
        continue # skip over to the next while loop

    user_input = choice_dict[user_input] # get the word of the user's choice
    bot_choice = bot_chooses() # save the bot choice

    # checking who won
    if user_input == bot_choice:
        print("TIE")
    elif bot_choice == winner_dict[user_input]: # the bot's choice matches the loser of the pair
        print("YOU WIN")
    else:
        print("YOU LOSE")

    print("\tYou chose " + user_input + ".\t Bot chose " + bot_choice + ".\n") # output what each player chose
    user_input = input(prompt) # reprompt the user

# quit while loop and end game
print("THANK YOU FOR PLAYING ROCK PAPER SCISSORS\n")