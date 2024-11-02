EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5




def check_answer(user_guess: int, actual_answer: int) -> None or int:
    """Takes two integer and compares them. Prints the result or returns 1 if guessed"""
    if user_guess > actual_answer:
        print("Too high!")
    elif user_guess < actual_answer:
        print("Too low!")
    else:
        print(f"You got it! The answer was {actual_answer}")
        return 1


def set_difficulty() -> int:
    """Asks the difficulty and returns total attempts as a result"""
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        return EASY_LEVEL_TURNS
    return HARD_LEVEL_TURNS