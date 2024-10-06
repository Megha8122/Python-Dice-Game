# Ask user to choose between Rock-Paper-Scissors.
# If choice is not valid
# print error
# Generate R P S for computer.
# Compare between Computer and User choice.
# Determine the winner
# Ask user if they want to continue
# If not, Terminate the game

import random

emoji = {"r": "🪨", "s": "✂️", "p": "🗒️"}
choices = ("r", "p", "s")

while True:
    user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()
    
    if user_choice not in choices:
        print("Invalid Choice")
    
    computer_choice = random.choice(choices)
    
    print(f"You chose {emoji[user_choice]}")
    print(f"Computer chose {emoji[computer_choice]}")
    
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "s" and computer_choice == "p")
        or (user_choice == "p" and computer_choice == "r")
    ):
        print("You win!")
    else:
        print("You Lose!")

    wanna_continue = input("Continue? (y/n): ").lower()
    if wanna_continue == 'n':
        break