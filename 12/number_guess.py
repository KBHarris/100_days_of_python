import random

print("Welcome to the Number Guessing Game!")

chosen_number = random.randint(1, 101)

print("I'm thinking of a number between 1 and 100.")

attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
if difficulty == 'hard':
    attempts = 5

print(f"You have {attempts} attempts to guess the number.")

game_over = False

while not game_over:

    guess = int(input("Make a guess: "))

    if guess == chosen_number:
        print(f"You win! The number was {chosen_number}.")
        game_over = True
    elif guess > chosen_number:
        print("Too high")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.")
    elif guess < chosen_number:
        print("Too low")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.")

    if attempts == 0:
        print("You've run out of guesses. You lose.")
        print(f"The number was {chosen_number}")
        game_over = True
