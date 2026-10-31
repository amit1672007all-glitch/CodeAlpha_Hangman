
import random

words = ["python", "computer", "programming", "developer", "coding"]

max_attempts = 6


def play_game():

    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    
    
    print("WELCOM TO HANGMAN GAME! 🤗")
    print("Guess the 😉 hidden  word! ")
    
    print("You have 6 incorrect guesses.")

    while wrong_guesses < max_attempts:

        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Wrong guesses left:", max_attempts - wrong_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The correct word was:", secret_word)
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print("\nGame Over!")
    print("The correct word was:", secret_word)


while True:

    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if again not in ["yes", "y"]:
        print("\nThanks for playing Hangman!")
        break
