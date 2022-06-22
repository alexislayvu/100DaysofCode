import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

display = []
for letter in chosen_word:
    display.append("_")

lives = 7
counter = -1
end_of_game = False

while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = user_guess

    if user_guess not in chosen_word:
        lives -= 1
        print(hangman_art.stages[counter])
        counter -= 1
        print(f"You guessed {user_guess}, that's not in the word. You have {lives} lives left.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0 and "_" in display:
        end_of_game = True
        print(f"You lose. The word was '{chosen_word}'")