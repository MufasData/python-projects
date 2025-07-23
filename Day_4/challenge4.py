from random import randint
print()
user_name = input("Hello, what is your name? ")
print()

print(f"Nice to meet you {user_name}. We are going to play a game where you will guess a number from 1 to 100. You get a total of 8 tries. Let's go!")
print()

correct_number = randint(1,100)
tries = 8

while tries > 0:
    guess = int(input(f"Guess the number... Try {9 - tries}..."))
    if guess > 100 or guess < 1:
        print("The number you provided is outside the bounds. Try again\n")
    elif guess == correct_number:
        print(f"The correct answer is indeed {correct_number}...\nYou got the correct answer in {9 - tries} tries. Congrats!\n")
        break
    elif guess > correct_number:
        print("The correct number is less than your guess. Try again\n")
    elif guess < correct_number:
        print("The correct number is greater than your guess. Try again\n")
    
    tries -= 1

if guess != correct_number:
    print("Sorry, you have used up all 8 attempts :(")
    print()


print("""Thanks for playing my game.
See you next time!

""")
