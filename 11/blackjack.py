from hashlib import scrypt
from warnings import catch_warnings
from art import logo
import random

play = input("Would you like to play a game of BlackJack? Y or N: ")

if play.lower() == 'n':
    pass
else:

    print(logo)

    def calculate_score(card_list):
        score = sum(card_list)
        if score == 21 and len(card_list) == 2:
            return 0
        if 11 in card_list and score > 21:
            card_list.remove(11)
            card_list.append(1)
        return score
    

    player_cards = []

    dealer_cards = []

    game_over = False

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    while not game_over:
            
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards} Your score: {player_score}")
        print(f"Dealer's first card {dealer_cards[0]}")

        if (player_score == 0 or dealer_score == 0) or player_score > 21:
            game_over = True
        else:
            draw_card = input("Would you like to draw another card? Y or N: ")
            if draw_card.lower() == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

def compare(player_score, dealer_score):
    if dealer_score == 0:
        dealer_score = 21
    elif player_score == 0:
        player_score == 21
    if player_score == dealer_score:
        print("It's a draw!")
    elif dealer_score == 21 or player_score > 21:
        print("You lose")
    elif player_score == 21 or dealer_score > 21:
        print("You win!")
    elif player_score > dealer_score:
        print("You win!")
    elif dealer_score > player_score:
        print("You lose")
    

print(f"Your score was {player_score}, the dealer's score was {dealer_score}.")
compare(player_score, dealer_score)

