# Written 7/4/2022
# Day 8 Project of 100 Days of Code

# Program that encrypts and decrypts messages based off of the Caesar Cipher, which shifts the numerical value of letters.
import caesar_art

print(caesar_art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amt):
    cipher_text = ""
    if shift_amt > 26:
        shift_amt %= 26
    for letter in plain_text:
        if letter not in alphabet:
            cipher_text += letter
        elif (alphabet.index(letter) + shift_amt) > 25:
             cipher_text += alphabet[(alphabet.index(letter) + shift_amt) - 26] 
        else:
            cipher_text += alphabet[alphabet.index(letter) + shift_amt]
    print(cipher_text)
    
def decrypt(plain_text, shift_amt):
    cipher_text = ""
    if shift_amt > 26:
        shift_amt %= 26
    for letter in plain_text:
        if letter not in alphabet:
            cipher_text += letter
        elif (alphabet.index(letter) - shift_amt) < 0:
             cipher_text += alphabet[26 + (alphabet.index(letter) - shift_amt)] 
        else:
            cipher_text += alphabet[alphabet.index(letter) - shift_amt]
    print(cipher_text)

def caesar(direction, text, shift):
    if direction == "encode":
        encrypt(plain_text = text,shift_amt = shift)
    elif direction == "decode":
        decrypt(plain_text = text,shift_amt = shift)
    else:
        print("Goodbye")

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     for letter in start_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "decode":
#             shift_amount *= -1
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {end_text}.")

# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
play_again = True
while play_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    w_t_p_a = input("Do you want to play again? Enter \'y\' to play again or \'n\' to exit.\n")
    if w_t_p_a == "n":
        play_again = False

print("Thank you for using the program!")