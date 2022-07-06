# Written 7/5/2022
# Day 11 Project of 100 Days of Code

# Program that emulates the game Blackjack. The purpose of this game is to get as close to 21 through your card count without going over.

import blackjack_art
import random           # need to randomly select card
import os               # need clear function, refer to either day 9 or 10 for code

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = {"Ace": 11, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
# user_hand_val = cards.get(user_hand[0]) + cards.get(user_hand[1])




def check_user_hand(user_hand_val, user_hand):
    '''
    Function that checks the user hand's value.
    '''
    for card in range(len(user_hand)):
        user_hand_val += cards.get(user_hand[card])
    return user_hand_val

def check_comp_hand(comp_hand_val, comp_hand):
    for card in range(len(comp_hand)):
        comp_hand_val += cards.get(comp_hand[card])
    return comp_hand_val

# def check_comp_hand():
#     '''
#     Function that checks the computer hand's value.
#     '''
#     # print(comp_hand)
#     # print(cards.get(comp_hand[0]) + cards.get(comp_hand[1]))
#     user_hand_val = cards.get(comp_hand[0]) + cards.get(comp_hand[1])
#     return user_hand_val
#     # if cards.get(comp_hand[0]) + cards.get(comp_hand[1]) == 21:
#     #     return True
#     # elif cards.get(comp_hand[0]) + cards.get(comp_hand[1]) < 21:
#     #     return cards.get(comp_hand[0]) + cards.get(comp_hand[1])
#     # else:
#     #     return False

def ace_check(user_hand, comp_hand):
    comp_hand_val = 0
    comp_hand_val = check_comp_hand(comp_hand_val, comp_hand)
    user_hand_val = 0
    user_hand_val = check_comp_hand(user_hand_val, user_hand)
    if 'Ace' in user_hand and user_hand_val > 21:
        user_hand_val = user_hand_val - 10
    if 'Ace' in comp_hand and check_comp_hand() > 21:
        comp_hand_val = comp_hand_val - 10

def hit_me():
    '''
    Function that adds a card to user list if wanted. Also adds card to computer's hand
    if certain conditions are met. 
    '''
    hit = input("Type \'y\' to get another card, type \'n\' to pass: ")

# def win_check(comp_hand_val, user_hand_val):
#     if comp_hand_val == 21:
#         print("User loses!")
#     elif user_hand_val == 21:
#         print("You win!")
#     elif comp_hand_val == user_hand_val:
#         print("You draw.")
#     elif comp_hand_val > user_hand_val:
#         print("User loses.")
#     elif comp_hand_val < user_hand_val:
#         print("You win!")

def win_check(comp_hand, user_hand):
    comp_hand_val = 0
    comp_hand_val = check_comp_hand(comp_hand_val, comp_hand)
    user_hand_val = 0
    user_hand_val = check_comp_hand(user_hand_val, user_hand)

    if comp_hand_val == 21:
        print("User loses!")
    elif user_hand_val == 21:
        print("You win!")
    elif comp_hand_val == user_hand_val:
        print("You draw.")
    elif comp_hand_val > user_hand_val:
        print("User loses.")
    elif comp_hand_val < user_hand_val:
        print("You win!")


def blackjack_game():
    user_hand = [random.choice(list(cards)), random.choice(list(cards))]
    comp_hand = [random.choice(list(cards)), random.choice(list(cards))]
    user_hand_val = 0
    comp_hand_val = 0

    ace_check(user_hand, comp_hand)
    print(blackjack_art.logo)
    print("Computer hand:")
    print(comp_hand)
    print(check_comp_hand(comp_hand_val, comp_hand))
    # print(cards.get(comp_hand[0]) + cards.get(comp_hand[1]))

    print(f"Your cards: {user_hand[0]} and {user_hand[1]}, current score is: {check_user_hand(user_hand_val, user_hand)}")
    print(f"Computer's first card: {comp_hand[0]}")
    #print(check_user_hand())
    # print(cards.get(user_hand[0]) + cards.get(user_hand[1]))

    # hit_me()
    #user_hand_val = check_user_hand(user_hand_val, user_hand)
    win_check(comp_hand, user_hand)


blackjack_game()