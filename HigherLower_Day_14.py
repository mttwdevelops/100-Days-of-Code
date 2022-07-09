# Written 7/7/2022
# Day 14 Project of 100 Days of Code

# Game where player guesses which person has more instagram followers

import os
import random
import higherlower_data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

alive = True
a = random.choice(higherlower_data.data)

while alive:
    os.system('cls')
    print(logo)
    b = random.choice(higherlower_data.data)
    if a == b:
        b = random.choice(higherlower_data.data)

    # print(a)
    # print(b)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.\n\n")
    # print(f"A: {a['follower_count']}")
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.\n\n")
    # print(f"B: {b['follower_count']}")
    guess = input("Who has more followers? Type \'A\' or \'B\': ").lower()
    
    if guess == "a":
        if a["follower_count"] >= b["follower_count"]:
            pass
        else:
            print(f"That was incorrect. Person B had {b['follower_count']} million followers, while Persona A had {a['follower_count']} million followers.")
            alive = False

    else:
        if b["follower_count"] >= a["follower_count"]:
            a = b
        else:
            print(f"That was incorrect. Person A had {a['follower_count']} million followers, while Persona B had {b['follower_count']} million followers.")
            alive = False