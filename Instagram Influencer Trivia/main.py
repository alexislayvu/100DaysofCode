import art
import os
import random
from game_data import data


def correct_answer(acc_one, acc_two):
    """Returns the account that has more Instagram followers."""
    if acc_one['follower_count'] > acc_two['follower_count']:
        return acc_one

    return acc_two


def format_choice(account):
    """Formats the account into a printable format: name, description, and country."""
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, {description}, from {country}"


def random_choice():
    """Returns a random account from the 'data' list."""
    return random.choice(data)


score = 0
account_one = random_choice()
account_two = random_choice()

is_correct = True
while is_correct:
    print(art.logo)

    answer = correct_answer(account_one, account_two)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {format_choice(account_one)}.")
    print(art.vs)
    print(f"Against B: {format_choice(account_two)}.")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_guess == 'A':
        user_guess = account_one
    else:
        user_guess = account_two

    if user_guess == answer:
        account_one = answer
        account_two = random_choice()
        score += 1
    else:
        is_correct = False

    os.system('cls')

print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
