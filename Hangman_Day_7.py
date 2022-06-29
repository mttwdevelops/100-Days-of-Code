# Written 6/29/2022
# Day 7 Project of 100 Days of Code

# Program that emulates the hangman game. 

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
chosen_word_list = []
lives = 6
for i in chosen_word:
    chosen_word_list.append("_")

print(hangman_art.logo)

while ("".join(chosen_word_list) != chosen_word):
    guess = input("Please guess a letter that may be in the word: ").lower()
    if guess in chosen_word_list:
        print(f"You already guessed {guess}...")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            chosen_word_list[position] = guess
    print(chosen_word_list)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    if lives == 0:
        break
    print(lives)
    print(f'{hangman_art.stages[lives]}')

if lives == 0:
    print(f"You lose, the correct word was {chosen_word}\n\n.")
else:
    print("You guessed the word correctly! Hooray!\n\n")