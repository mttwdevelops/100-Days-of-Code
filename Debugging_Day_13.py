# Written 7/6/2022
# Day 13 Project of 100 Days of Code

# Debugging practice done while undertaking blackjack game

############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21): # range was originally from 1 to 20
    if i == 20:
      print("You got it")
my_function()

# The issue with this program is that the range was from 1 to 20, meaning it stopped at 19 and thus did not get to 20, so the print statement never happened. We can also set the if statement to 19 instead of 20 to run.

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# The issue with this program is that the numbers for the randint function are in the wrong range, they should instead be from 0 to 5. This is since the list index starts from 0.

# Play Computer
year = int(input("What's your year of birth?"))
if (year > 1980 and year < 1994):
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

# The issue with this program is if someone was born in 1994. The original elif statement was just > and not >=.

# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# The issues with this program is the lack of an indent before the print statement, a needed integer conversion for the age input, and an indicator for the f-string (putting f in front of the quotation marks). 

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# The issue with this program is a check statement for words_per_page instead of just =.

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)
mutate([1,2,3,5,8,13])

# The issue with this program is that the b_list.append function was not indented properly.
