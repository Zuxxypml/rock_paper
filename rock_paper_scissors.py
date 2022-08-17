# Constants
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
# Welcome Message
print("Welcome to Rock paper scissors")

# Choice Algorithm
def choice_checker(choice_args, whose_choice):
    if choice_args == 0:
        print(f"{whose_choice} Choice")
        print(f"{rock}")
    elif choice_args == 1:
        print(f"{whose_choice} Choice")
        print(f"{paper}")
    elif choice_args == 2:
        print(f"{whose_choice} Choice")
        print(f"{scissors}")
    else:
        print("Invalid Input try again ")
# User Logic
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for scissors"))
choice_checker(user_choice, "Your")
# Computer Logic
computer_choice = round((random.random() * 2))
choice_checker(computer_choice, "Computer's")

# Winner Algorithm
def winner(user, comp):
    if user == 0 and comp == 1 or user == 1 and comp == 2 or user == 2 and comp == 0:
        print("You lose :(")
    elif user == 1 and comp == 0 or user == 2 and comp == 1 or user == 0 and comp == 2:
        print("You win ✔")
    else:
        print("Draw :)")

# Decalres Winner
winner(user_choice, computer_choice)