# Written 6/23/2022
# Day 3 Project of 100 Days of Code

# Short game that runs based off of simple choices made by player. Tests conditionals.

from turtle import left


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 

cross_choice = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\".\n\n")
if cross_choice == "left":
    print("Good choice!\n\n")
else:
    print("Fell into a hole. Game over!\n\n")
    quit()

lake_choice = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n\n")
if lake_choice == "wait":
    print("Good choice!\n\n")
else:
    print("Attacked by trout. Game Over!\n\n")
    quit()

house_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n\n")
if house_choice == "yellow":
    print("You win! Game completed. +100 respect.\n\n")
    quit()
elif house_choice == "red":
    print("Burned by fire. Game Over!\n\n")
    quit()
elif house_choice == "blue":
    print("Eaten by beasts. Game Over!\n\n")
    quit()
else:
    print("Game Over.\n\n")
    quit()