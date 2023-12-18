import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Select a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize variables
guessed_letters = []
attempts = 6  # Number of allowed incorrect attempts


# Function to display the current state of the word with guessed letters
def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    return display


# Main game loop
while True:
    # Display the current state of the word
    print("\nCurrent word:", display_word(chosen_word, guessed_letters))

    # Ask the player for a letter guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter and not already guessed
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please guess a single letter.")
        continue

    # Check if the letter has been guessed before
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add the letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in chosen_word:
        print("Good guess!")
    else:
        print("Incorrect guess.")
        attempts -= 1

    # Check for win or loss conditions
    if display_word(chosen_word, guessed_letters) == chosen_word:
        print("\nCongratulations! You've won. The word was:", chosen_word)
        break
    elif attempts == 0:
        print("\nGame over! You've run out of attempts. The word was:", chosen_word)
        break

# End of the game
