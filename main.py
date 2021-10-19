from art import logo
import random

print(logo)


def easy():
    goal = random.randint(1, 100)
    game_easy = True
    attempts = 10

    while game_easy:
        print(f"You have {attempts} attempts")
        user_guess = int(input("Guess a number between 1 & 100: "))
        if 1 > user_guess or user_guess > 100:
            print("Invalid guess, try again")
        elif user_guess == goal:
            print(f"You guessed correctly!! The number was {goal}")
            game_easy = False
        elif user_guess > goal:
            print(f"Your guess was too high. Try again")
        elif user_guess < goal:
            print(f"Your guess was too low. Try again")
        attempts -= 1
        if attempts == 0:
            game_easy = False


def hard():
    goal = random.randint(1, 100)
    game_hard = True
    attempts = 5

    while game_hard:
        print(f"You have {attempts} attempts")
        user_guess = int(input("Guess a number between 1 & 100: "))
        if 1 > user_guess or user_guess > 100:
            print("Invalid guess, try again")
        elif user_guess == goal:
            print(f"You guessed correctly!! The number was {goal}")
            game_hard = False
        elif user_guess > goal:
            print(f"Your guess was too high. Try again")
        elif user_guess < goal:
            print(f"Your guess was too low. Try again")
        attempts -= 1
        if attempts == 0:
            game_hard = False


def game():
    user_choice = input("Welcome to the Number Guessing game!! Please choose your difficulty: 'easy' or 'hard'\n")

    if user_choice == "easy":
        easy()
    elif user_choice == "hard":
        hard()

    try_again = input("Would you like to play again? 'Yes or 'No' ")
    if try_again == "Yes":
        game()
    elif try_again == "No":
        print("Thanks for playing!! Goodbye")


game()



