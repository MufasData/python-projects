from random import choice

name = input("Hello... What's your name?\n")

word_list = ['orange', 'tides', 'association', 'whale', 'watch', 'basketball', 'tennis', 'racket']
word_to_guess = choice(word_list)
word_length = len(word_to_guess)

print(f"\nHello {name}. Welcome to Mufas' Hangman game.")
print(f"You get 6 chances. Good luck!\n")
print('_' * word_length + f" ({word_length} letters)\n")

def letter_guess():
    return input("Guess a letter: ").lower()

def list_of_indices(guess):
    return [i for i, char in enumerate(word_to_guess) if char == guess]

def guess_game():
    hangman_word = ['_'] * word_length
    tries = 6
    guessed_letters = set()

    while tries > 0:
        print("\nCurrent word: " + ' '.join(hangman_word))
        guess = letter_guess()

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        guessed_letters.add(guess)

        indices = list_of_indices(guess)

        if indices:
            for i in indices:
                hangman_word[i] = guess
            if '_' not in hangman_word:
                print("\n" + ' '.join(hangman_word))
                return f"\n🎉 Congratulations {name}, you guessed the word: {word_to_guess}!"
        else:
            tries -= 1
            print(f"Incorrect! You have {tries} tries left.")

    return f"\n💀 Game Over! The word was: {word_to_guess}"

# Run the game
print(guess_game())