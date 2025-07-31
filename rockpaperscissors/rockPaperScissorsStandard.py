# ROCK PAPER SCISSORS
# Arrayscape Gaming 2025
# Developed by Josephine Lee
# Inspiration: https://realpython.com/python-rock-paper-scissors
###################################################################################################

# INITIALIZING ###################################################################################################
import random # a built-in module to generate random numbers

# MAIN GAME ###################################################################################################
print("*" * 30)
print("WELCOME TO ROCK PAPER SCISSORS")
print("*" * 30)

# 1. Ask the user for their choice
user_action = input("Enter a choice (rock, paper, scissors): ")

# 2. Generate a random choice for the computer player
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

# 3. Compare the choices
print("\nYou chose " + user_action + " and the computer chose " + computer_action + "\n")

# 4. And print the winner
if user_action == computer_action: # Tie
    print("Both players selected " + user_action + ". It's a tie!") 
elif user_action == "rock": # Player choices rock
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper": # Player choices paper
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors": # Player choices scissors
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

# What if the user inputs a choice that is not valid?
else:
    print("Invalid choice")