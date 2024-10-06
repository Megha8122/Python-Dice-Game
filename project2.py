# Ask user to enter a number between 1 and 100
# Loop
# If
#   the entered number is lower than the number set by computer
# print Too Low!
# Else If
#   the entered number is ligher than the number set by computer
# print Too High!
# Else If entered number is True
# print COngratulations! You guessed the number

import random

number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
    
        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print("Congratulations! You guessed the number")
            break
    except ValueError:
        print("Please enter a valid number")
