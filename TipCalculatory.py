# Written 6/21/2022
# Day 2 Project of 100 Days of Code

# Program that takes the total bill, adds tip, and divides by the number of people to determine individual bill totals. Tests type conversion, math operators, and string formatting. 

bill_total = float(input("Welcome to the tip calculator.\nWhat was the total bill? "))
num_people = int(input("How many people to split the bill? "))
perc_tip = (float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100) + 1
final_amt = round((bill_total * perc_tip) / num_people , 2)
print(f"Each person should pay: ${final_amt}")