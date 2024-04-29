import random
from art import logo
print(logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\n")
difficulty = input("Choose a difficulty: type 'easy' or 'hard': ")
if difficulty == 'easy':
    number_of_lives = 10
else:
    number_of_lives = 5

final_number = random.choice(range(1,101))

game = True
while game:

    if number_of_lives != 0:
        print(f"You have {number_of_lives} attempts remaining to guess the number.")
    else:
        print(f"Oops. You ran out of attempts. The correct answer was {final_number}")
        game = False
        break

    user_guess = int(input("Make a guess: "))
    if user_guess > final_number:
        number_of_lives -= 1
        print("Too high.\n")
    elif user_guess < final_number:
        print("Too low.\n")
        number_of_lives -= 1
    elif user_guess == final_number:
        print(f"You win! The correct answer was {final_number}")
        game = False
    else:
        number_of_lives -= 1
        print("You made an invalid input.")

    