# Written 7/5/2022
# Day 11 Project of 100 Days of Code

# Program that emulates the game Blackjack. The purpose of this game is to get as close to 21 through your card count without going over.

import blackjack_art
import random           
import os               

cards = {"Ace": 11, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

keep_playing = True 
_run = True
while keep_playing:
    play_game = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")
    if play_game == "y":
        os.system("cls")
        user_hand = [random.choice(list(cards)), random.choice(list(cards))]
        user_hand_total = cards.get(user_hand[0]) + cards.get(user_hand[1])
        comp_hand = [random.choice(list(cards)), random.choice(list(cards))]
        comp_hand_total = cards.get(comp_hand[0]) + cards.get(comp_hand[1])

        print(blackjack_art.logo)
        print(f"Your cards: {user_hand}, current score: {user_hand_total}")
        print(f"Computer's first card: {comp_hand[0]}")

        # Kept in for testing purposes
        # print(f"Computer hand is: {comp_hand}")
        # print(f"Computer hand total is: {comp_hand_total}")

        # Checks for immediate blackjack
        if comp_hand_total == 21:
            print("You lose!")
        elif user_hand_total == 21:
            print("You win!")
        elif user_hand_total > 21 and "Ace" in user_hand:
            if user_hand_total - 10 > 21:
                print("You lose. You went over")
                break
            else:
                user_hand_total -= 10

        keep_hitting = True
        if user_hand_total > 21:
            keep_hitting = False
        while keep_hitting:
            hit_condition = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
            if hit_condition == "y":
                user_hand.append(random.choice(list(cards)))
                user_hand_total += cards.get(user_hand[-1])
                print(f"Your new card is: {user_hand[-1]}")
                print(f"Your total is now: {user_hand_total}")
                # code here needs to be revised...
                if user_hand_total > 21:
                    if "Ace" in user_hand:
                        if user_hand_total - 10 > 21:
                            print("You lose, still over 21... (even after ace is 1)")
                            break
                        else:
                            user_hand_total -= 10
                    else:
                        print("You lose, over 21 and no aces can be brought down to 1..")
                else:
                    continue
            else:
                break        

        if comp_hand_total < 16:
            while comp_hand_total < 16:
                comp_hand.append(random.choice(list(cards)))
                comp_hand_total += cards.get(comp_hand[-1])

        print(f"User hand total is: {user_hand_total}")
        print(f"Comp hand total is: {comp_hand_total}")

        # determine if the player wins or loses
        if comp_hand_total > 21:
            print("You win, computer hand is over 21.")
        if (user_hand_total <= 21) and user_hand_total > comp_hand_total:
            print("You win, you are closer to 21!")
        elif user_hand_total < comp_hand_total and (comp_hand_total <= 21):
            print("You lose, computer is closer to 21.")
        elif user_hand_total == comp_hand_total:
            print("Draw.")
    else:
        break