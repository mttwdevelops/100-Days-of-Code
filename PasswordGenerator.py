# Written 6/28/2022
# Day 5 Project of 100 Days of Code

# Simple program that takes input of how many letters, symbols, and numbers, which then returns a password including the criteria.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_len = nr_letters + nr_symbols + nr_numbers
pass_list = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for i in range(0, nr_letters):
#     pass_list.append(random.choice(letters))
# for i in range(0, nr_symbols):
#     pass_list.append(random.choice(symbols))
# for i in range(0, nr_numbers):
#     pass_list.append(random.choice(numbers))
# final_pass = ''.join(pass_list)
# print(final_pass)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# total number of letters, numbers, symbols
# rand function then randomly picks number and then takes number, then another random
# picks its respective item
# append to list
# then sandwich list into a string

nr_letters_check = 0; nr_numbers_check = 0; nr_symbols_check = 0
pass_list = []
for i in range(0, pass_len):
    x = random.randint(0,2)
    if x == 0:
        if nr_letters_check < nr_letters:
            pass_list.append(random.choice(letters))
            nr_letters_check += 1
        elif nr_numbers_check < nr_numbers:
            pass_list.append(random.choice(numbers))
            nr_numbers_check += 1
        elif nr_symbols_check < nr_symbols:
            pass_list.append(random.choice(symbols))
            nr_symbols_check += 1
        else:
            continue
    if x == 1:
        if nr_numbers_check < nr_numbers:
            pass_list.append(random.choice(numbers))
            nr_numbers_check += 1
        elif nr_letters_check < nr_letters:
            pass_list.append(random.choice(letters))
            nr_letters_check += 1
        elif nr_symbols_check < nr_symbols:
            pass_list.append(random.choice(symbols))
            nr_symbols_check += 1
        else:
            continue
    else:
        if nr_symbols_check < nr_symbols:
            pass_list.append(random.choice(symbols))
            nr_symbols_check += 1
        elif nr_numbers_check < nr_numbers:
            pass_list.append(random.choice(numbers))
            nr_numbers_check += 1
        elif nr_letters_check < nr_letters:
            pass_list.append(random.choice(letters))
            nr_letters_check += 1
        else:
            continue
    
final_pass = ''.join(pass_list)
print(final_pass)
print(len(pass_list))
print(pass_len)
print(nr_letters_check)
print(nr_numbers_check)
print(nr_symbols_check)