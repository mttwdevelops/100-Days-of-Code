# Written 7/5/2022
# Day 9 Project of 100 Days of Code

# Program that works as a "blind" auction, meaning that the highest bid is only revealed at the end.

import blindauction_art
import os

print(blindauction_art.logo)

prog_status = True
bidders = {}
while prog_status == True:
    name = input("\nWelcome to the secret auction program.\nWhat is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    end_bid = input("Are there any other bidders? Type \'yes\' or \'no\'. ")
    if end_bid == "no":
        os.system('cls')
        break
    os.system('cls')

winner = max(bidders, key = bidders.get)
print(f"The winner of the bid is {winner} with a bid of ${bidders[winner]}.")