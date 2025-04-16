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
userAction = input("Enter a choice (rock, paper, scissors): ")

# 2. Generate a random choice for the computer player
possibleActions = ["rock", "paper", "scissors"]
computerAction = random.choice(possibleActions)

# 3. Compare the choices
print("\nYou chose " + userAction + " and the computer chose " + computerAction + "\n")

# 4. And print the winner
if userAction == computerAction: # Tie
    print("Both players selected " + userAction + ". It's a tie!") 
elif userAction == "rock": # Player choices rock
    if computerAction == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif userAction == "paper": # Player choices paper
    if computerAction == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif userAction == "scissors": # Player choices scissors
    if computerAction == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

# BONUS: What if the user inputs a choice that is not valid?
else:
    print("Invalid choice")