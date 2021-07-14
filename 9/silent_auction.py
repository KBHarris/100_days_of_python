from os import system, name
from art import logo

print(logo)

winner = ''
largest_bid = 0

bids = {}

def add_to_bids(name, bid):
    bids[name] = bid

def clear():
  if name == "nt":
    _ = system('cls')
  else:
    _ = system('clear')

go_again = False

while not go_again:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    add_to_bids(name, bid)
    clear()

    run = input("Are there any other bids? Y or N? ")
    if run.lower() == 'n':
        go_again = True
        
        for key in bids:
            value = bids[key]
            if value > largest_bid:
                largest_bid = value
                winner = key
clear()
print(f"{winner} is the winner with a bid of ${largest_bid}.")


