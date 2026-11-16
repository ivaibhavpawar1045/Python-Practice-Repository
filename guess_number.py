"""
Problem:  Guess the random number

Platform: SelfStudy

Difficulty: mid 

"""

import random

secret_number = random.randint(1, 100)
attempts = 7

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it.\n")

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100.\n")
    elif guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
        break
else:
    print(f"Game over! The correct number was {secret_number}.")