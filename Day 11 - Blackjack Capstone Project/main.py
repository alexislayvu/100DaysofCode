import os
import random
from art import logo


def calculate_score(card_list):
    """Calculates the sum of the numbers in the provided list."""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare(user_score, computer_score):
    """Compare the user's score and the computer's score and determine the winner."""
    if user_score == computer_score:
        print("Draw!\n")
    elif computer_score == 0:
        print("Opponent has a Blackjack. You lose.\n")
    elif user_score == 0:
        print("Win with a Blackjack!\n")
    elif user_score > 21:
        print("You went over. You lose.\n")
    elif computer_score > 21:
        print("Opponent went over. You win.\n")
    elif user_score > computer_score:
        print("You win!\n")
    else:
        print("You lose.\n")


def deal_card():
    """Selects a random number from the 'cards' list."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)


def play_game():
    """Play the Blackjack game!"""
    print(logo)

    user_cards = []
    computer_cards = []

    is_game_over = False

    # Deal two cards to the user and the computer.
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_deal_again == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("")
    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score {calculate_score(computer_cards)}")
    compare(user_score, computer_score)


# Play Blackjack
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system('cls')
    play_game()
