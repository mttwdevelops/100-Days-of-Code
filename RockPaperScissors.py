# Written 6/28/2022
# Day 4 Project of 100 Days of Code

# Program that takes the user input to simulate the game "rock, paper, and scissors." This tests string graphical output, random functions, and logic.

import random
from secrets import choice

user_Choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
comp_Choice = random.randint(0,2)

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
def rock_paper_scissors(user_Choice, comp_Choice):
    choice_dict = {"0":rock, "1":paper, "2":scissors}
# compare user and computer's choice to determine winner or draw
    if (int(user_Choice) == comp_Choice):
        print(f"{choice_dict[user_Choice]}\n\n{choice_dict[str(comp_Choice)]}\nThere seems to be a draw. Try again!")
        return 
    elif int(user_Choice) == 0:
        if comp_Choice == 1:
            print(f"{choice_dict[user_Choice]}\n\n{choice_dict[str(comp_Choice)]}\nRock is beaten by paper. You lose!")
        else:
            print(f"{choice_dict[user_Choice]}\n\n{choice_dict[str(comp_Choice)]}\nRock beats scissors. You win!")
    elif int(user_Choice) == 1:
        if comp_Choice == 0:
            print(f"{choice_dict[user_Choice]}\n\n{choice_dict[str(comp_Choice)]}\nPaper beats rock. You win!")
        else:
            print(f"{choice_dict[user_Choice]}\n\n{choice_dict[str(comp_Choice)]}\nPaper is beaten by scissors. You lose!")
    elif int(user_Choice) == 2:
        if comp_Choice == 0:
            print(f"{choice_dict[user_Choice]}\n\n{choice_dict[str(comp_Choice)]}\Scissors is beaten by rock. You lose!")
        else:
            print(f"{choice_dict[user_Choice]}\n\n{choice_dict[str(comp_Choice)]}\Scissors beats paper. You win!")

rock_paper_scissors(user_Choice, comp_Choice)