# Written 7/7/2022
# Day 12 Project of 100 Days of Code

# Game where player guesses a number between 1 to 100 within a certain number of attempts

import random
import sys

logo = '''


  ,ad8888ba,                                                              88                          888b      88                                   88                                   
 d8"'    `"8b                                                      ,d     88                          8888b     88                                   88                                   
d8'                                                                88     88                          88 `8b    88                                   88                                   
88             88       88   ,adPPYba,  ,adPPYba,  ,adPPYba,     MM88MMM  88,dPPYba,    ,adPPYba,     88  `8b   88  88       88  88,dPYba,,adPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,  
88      88888  88       88  a8P_____88  I8[    ""  I8[    ""       88     88P'    "8a  a8P_____88     88   `8b  88  88       88  88P'   "88"    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
Y8,        88  88       88  8PP"""""""   `"Y8ba,    `"Y8ba,        88     88       88  8PP"""""""     88    `8b 88  88       88  88      88      88  88       d8  8PP"""""""  88          
 Y8a.    .a88  "8a,   ,a88  "8b,   ,aa  aa    ]8I  aa    ]8I       88,    88       88  "8b,   ,aa     88     `8888  "8a,   ,a88  88      88      88  88b,   ,a8"  "8b,   ,aa  88          
  `"Y88888P"    `"YbbdP'Y8   `"Ybbd8"'  `"YbbdP"'  `"YbbdP"'       "Y888  88       88   `"Ybbd8"'     88      `888   `"YbbdP'Y8  88      88      88  8Y"Ybbd8"'    `"Ybbd8"'  88          
                                                                                                                                                                                          
                                                                                                                                                                                          
'''

def easy_mode(numb):
    lives = 10
    while lives >= 1:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > numb:
            lives -= 1
            print(f"Too high. You now have {lives} lives left.")
        elif guess < numb:
            lives -= 1
            print(f"Too low. You now have {lives} lives left.")
        else:
            print("You got it!")
            sys.exit()
    print("You lose!")    

def hard_mode(numb):
    lives = 5
    while lives >= 1:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > numb:
            lives -= 1
            print(f"Too high. You now have {lives} lives left.")
        elif guess < numb:
            lives -= 1
            print(f"Too low. You now have {lives} lives left.")
        else:
            print("You got it!")
            sys.exit()
    print("You lose!")

# introduce the game and prompt the user for difficulty
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()
# include the random number for testing purposes
numb = random.randint(1, 100)
# print(f"psst, the number is {numb} for testing purposes.")
# if easy, they have ten attempts to guess
# if hard, they have 5 attempts

if difficulty == "easy":
    easy_mode(numb)
elif difficulty == "hard":
    hard_mode(numb)
else:
    print("Goodbye")