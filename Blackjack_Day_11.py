# Written 7/5/2022
# Day 11 Project of 100 Days of Code

# Program that emulates the game Blackjack. The purpose of this game is to get as close to 21 through your card count without going over.

import blackjack_art
import random           # need to randomly select card
import os               # need clear function, refer to either day 9 or 10 for code

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = {"Ace": 11, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

user_hand = [random.choice(list(cards)), random.choice(list(cards))]
comp_hand = [random.choice(list(cards)), random.choice(list(cards))]

def check_user_hand():
    '''
    Function that checks the user hand's value.
    '''
    # print(user_hand)
    # print(cards.get(user_hand[0]) + cards.get(user_hand[1]))
    return (cards.get(user_hand[0]) + cards.get(user_hand[1]))
    # if cards.get(user_hand[0]) + cards.get(user_hand[1]) == 21:
    #     return True
    # elif cards.get(user_hand[0]) + cards.get(user_hand[1]) < 21:
    #     return cards.get(user_hand[0]) + cards.get(user_hand[1])
    # else:
    #     return False

def check_comp_hand():
    '''
    Function that checks the computer hand's value.
    '''
    # print(comp_hand)
    # print(cards.get(comp_hand[0]) + cards.get(comp_hand[1]))
    return (cards.get(comp_hand[0]) + cards.get(comp_hand[1]))
    # if cards.get(comp_hand[0]) + cards.get(comp_hand[1]) == 21:
    #     return True
    # elif cards.get(comp_hand[0]) + cards.get(comp_hand[1]) < 21:
    #     return cards.get(comp_hand[0]) + cards.get(comp_hand[1])
    # else:
    #     return False

def blackjack_game():
    print("Computer hand:")
    print(comp_hand)
    print(check_comp_hand())
    # print(cards.get(comp_hand[0]) + cards.get(comp_hand[1]))

    print("User hand:")
    print(user_hand)
    print(check_user_hand())
    # print(cards.get(user_hand[0]) + cards.get(user_hand[1]))

    if check_comp_hand() == 21:
        print("User loses!")
    elif check_user_hand() == 21:
        print("You win!")
    elif check_comp_hand() == check_user_hand():
        print("You draw.")
    elif check_comp_hand() > check_user_hand():
        print("User loses.")
    elif check_comp_hand() < check_user_hand():
        print("You win!")

blackjack_game()