import random

your_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))

comp_choice = random.randint(0, 2)

if your_choice == 0:
    print("\nYou chose Rock")
elif your_choice == 1:
    print("\nYou chose Paper")
elif your_choice == 2:
    print("\nYou chose Scissors")

if comp_choice == 0:
    print("\nComputer chose Rock")
elif comp_choice == 1:
    print("\nComputer chose Paper")
elif comp_choice == 2:
    print("\nComputer chose Scissors")

if your_choice == 0 and comp_choice == 2:
    print("You Win!")
if comp_choice == 0 and your_choice == 2:
    print("You Lose!")
elif comp_choice > your_choice:
    print("You Lose!")
elif comp_choice == your_choice:
    print("It's a draw!")
else:
    print("You typed an invalid number. You lose!")


    
    



