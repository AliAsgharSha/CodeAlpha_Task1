import random

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

guessed_letters = []
attempts = 6

def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    return display

while True:
    print("\nCurrent word:", display_word(chosen_word, guessed_letters))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please guess a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")
    else:
        print("Incorrect guess.")
        attempts -= 1

    if display_word(chosen_word, guessed_letters) == chosen_word:
        print("\nCongratulations! You've won. The word was:", chosen_word)
        break
    elif attempts == 0:
        print("\nGame over! You've run out of attempts. The word was:", chosen_word)
        break


