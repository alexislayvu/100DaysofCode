import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Check the user's guess with the answer."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    """Determines how many attempts the user gets to guess the number."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def play_game():
    """Play the Number Guessing Game!"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)
    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print(f"You've run out of guesses, you lose. The answer was {answer}.")
            break
        elif guess != answer:
            print("Guess again.")


play_game()
