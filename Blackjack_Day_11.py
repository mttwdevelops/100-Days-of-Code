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
    if cards.get(user_hand[0]) + cards.get(user_hand[1]) == 21:
        print("blackjack")
    else:
        print("not blackjack")

    print(user_hand)
    print(cards.get(user_hand[0]) + cards.get(user_hand[1]))

def check_comp_hand():
    '''
    Function that checks the computer hand's value.
    '''
    if cards.get(comp_hand[0]) + cards.get(comp_hand[1]) == 21:
        print("blackjack")
    else:
        print("not blackjack")

    print(comp_hand)
    print(cards.get(comp_hand[0]) + cards.get(comp_hand[1]))

