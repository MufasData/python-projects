# Programming The Hangman Game

from random import choice
print()
name = input("Hello... What's your name?\n")

word_list = ['association','watch','basketball','racket']

word_to_guess = choice(word_list)
print()
print(f"Hello {name}. Welcome to Mufas' Hangman game. Below is a word that you are going to have to guess. You get 6 lives. Good luck!\n")

word_length = len(word_to_guess)

incomplete_word = word_length * '_'

print(incomplete_word + f' ({word_length} letters)')
print()

def letter_guess():
    guess = input(f"Guess a letter... {tries} lives\n").lower()
    return guess

def letter_in_word_check(letter):
    if letter in word_to_guess:
        return True
    else:
        return False
    
def get_index_list(letter):
    count = 0
    index_list = []
    for i in word_to_guess:
        if i == letter:
            index_list.append(count)
            count += 1
        else:
            count += 1
    
    return index_list

def replace_letters(letter,index_list,word):
    incomplete_list = list(word)
    for i in index_list:
        incomplete_list[i] = letter
    
    word = ''.join(incomplete_list)
    return word

def check_if_won(word):
    if '_' in word:
        return False
    else:
        return True
    
#Start game

tries = 6

while tries > 0:

    guess = letter_guess()
    if guess.isalpha() == True and len(guess) == 1:
        if letter_in_word_check(guess) == True:
            index_list = get_index_list(guess)
            incomplete_word = replace_letters(guess,index_list,incomplete_word)
            print(incomplete_word)
        else:
            print(incomplete_word)
            tries -= 1
    else:
        print(f"You entered an inappropriate value: {guess}... you can only input a letter. Try again...")
        print(incomplete_word)
        continue

    if check_if_won(incomplete_word) == True:
        print()
        print(f"Congratulations!!! You have won the game.")
        break

if check_if_won(incomplete_word) == False:
    print()
    print(f"Unfortunately, you were not lucky this time... The correct word was {word_to_guess.upper()}.\nDon't worry, you will get it next time.")

print()
print("Thanks for playing!")
print()