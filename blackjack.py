import art
import random

#decalare game functions

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(p_score, d_score):
    """Compares the user score p_score against the computer score d_score."""
    if p_score == d_score:
        return "Draw 🙃"
    elif d_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif p_score == 0:
        return "Win with a Blackjack 😎"
    elif p_score > 21:
        return "You went over. You lose 😭"
    elif d_score > 21:
        return "Opponent went over. You win 😁"
    elif p_score > d_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def initialize():
    print(art.blackjack_logo)
    #declare game variables
    dealer_hand = []
    player_hand = []
    dealer_score = -1
    player_score = -1
    game_over = False


    #start gameplay
    for _ in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        def display_score():
            print(f"\nYour Cards: {player_hand}, current score: {player_score}")
            print(f"The dealer's first card is: {dealer_hand[0]}")

        display_score()

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            hit_me = input("Type 'y' to get another card, type 'n' to pass:  ")
            if hit_me == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    compare(player_score, dealer_score)

    print(f"\nYour final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    initialize()