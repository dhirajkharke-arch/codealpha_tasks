import random

# Key Concept: lists - predefined word list
WORDS = ["python", "hangman", "developer", "keyboard", "internet"]

MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly select a word from the list. (Key Concept: random)"""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Show the word with unguessed letters as underscores. (Key Concept: strings)"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("=" * 40)

    # Key Concept: while loop
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: none")

        guess = input("Guess a letter: ").lower().strip()

        # Key Concept: if-else validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"Congratulations! You guessed the word: {word}")
            print("=" * 40)
            return

    # Loop ended without winning -> player lost
    print("\n" + "=" * 40)
    print("You've run out of guesses! Game over.")
    print(f"The word was: {word}")
    print("=" * 40)


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
