# Written 7/7/2022
# Day 14 Project of 100 Days of Code

# Game where player guesses which person has more instagram followers

import os
import random
from re import A
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
while alive:
    os.system('cls')
    print(logo)
    a = random.choice(higherlower_data.data)
    b = random.choice(higherlower_data.data)

    # print(a)
    # print(b)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.\n\n")
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.\n\n")
    guess = input("Who has more followers? Type \'A\' or \'B\': ")
    
    if guess == "A":
        if a['followers'] > b['followers']:
            pass
        else:
            print(f"That was incorrect. Person B had {b['followers']}, while Persona A had {a['followers']}.")
            alive = False
    else:
        if a['followers'] > b['followers']:
            pass
        else:
            print(f"That was incorrect. Person A had {A['followers']}, while Persona B had {b['followers']}.")
            alive = False

# TODO: need to figure out how to set a = b
# TODO: need to figure out conditionals
