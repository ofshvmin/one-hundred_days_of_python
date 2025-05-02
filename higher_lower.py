from art import hl_logo as logo, vs
from game_data import hl_data as data
import random


def find_random_insta():
    return random.choice(data)

def find_winner(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'

def evaluate_guess(guess, winner):
    if guess == winner:
        return True
    else:
        return False

print(logo)
account_b = find_random_insta()
user_score = 0
game_should_continue = True

while game_should_continue:

    account_a = account_b
    account_b = find_random_insta()
    if account_a == account_b:
        account_b = find_random_insta()


    print(account_a['follower_count'], account_b['follower_count'])
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)

    winner = find_winner(account_a, account_b)

    is_correct = evaluate_guess(user_guess, winner)

    if is_correct:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
    else:
        print(f"Sorry, that's wrong.  Final score: {user_score}")
        game_should_continue = False
