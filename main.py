from logo import logo
from random import randint
from functions import set_difficulty, check_answer



def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)

    attempts = set_difficulty()

    is_guessed = False
    while attempts > 0 and not is_guessed:
        print(f"You have {attempts} remaining to guess the number.")
        attempts -= 1
        guess = int(input("Make a guess: "))
        if check_answer(guess, number):
            is_guessed = True
    else:
        print("You've run out of guesses. You lose!")


game()