from art import logo
from os import system, name
import random

def calculate_score(card_list):
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 21
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return score

def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
    
def compare(player_score, dealer_score):
        if player_score == dealer_score:
            return("It's a draw!")
        elif dealer_score == 21:
            return "Dealer has a BlackJack"
        elif player_score == 21:
            return "You win with a BlackJack!"
        elif player_score > 21:
            return "You lose, you went over."
        elif dealer_score > 21:
            return "Dealer went over, you win!"
        elif player_score > dealer_score:
            return "You win!"
        elif dealer_score > player_score:
            return "You lose"

def clear():
  if name == "nt":
    _ = system('cls')
  else:
    _ = system('clear')

def play_game():

    print(logo)

    player_cards = []

    dealer_cards = []

    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
            
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"\nYour cards: {player_cards} Your score: {player_score}")
        print(f"Dealer's first card {dealer_cards[0]}")

        if (player_score == 0 or dealer_score == 0) or player_score > 21:
            game_over = True
        else:
            draw_card = input("\nWould you like to draw another card? Y or N: ")
            if draw_card.lower() == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nYour deck: {player_cards}, Your score was {player_score}")
    print(f"Dealer's hand {dealer_cards}, Dealer's score was {dealer_score}\n")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of BlackJack? Y or N: ") == 'y':
    clear()
    play_game()