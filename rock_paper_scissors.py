import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_name = ["rock", "paper", "scissors"]
game_images = [rock, paper, scissors]

computer_choice = random.randint(0, 2)
print(computer_choice)

user_choice = int(input("What do you choose?\n"))

if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print(game_images[user_choice])

print(f"Computer chose {choice_name[computer_choice]}.")
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0:
    if computer_choice == 1:
        print("Paper beats rock.  Computer wins.")
    elif computer_choice == 2:
        print("Rock beats scissors.  You won!")
    else:
        print("something went wrong")
elif user_choice == 1:
    if computer_choice == 0:
        print("Paper beats rock.  You win!.")
    elif computer_choice == 2:
        print("Scissors beats paper. Computer wins.")
    else:
        print("something went wrong")
elif user_choice == 2:
    #scissors
    #rock beats scissors
    if computer_choice == 0:
        print("Rock beats scissors. Computer wins.")
    #scissors beats paper
    elif computer_choice == 1:
        print("Scissors beats paper. You win!")
else:
    print(f"{user_choice} not a valid choice. You lose.")
    # user_choice = input("Please choose a whole number from 0 - 2")