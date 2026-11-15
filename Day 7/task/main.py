import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lives = 6
chosen_word = random.choice(word_list)

# This builds a row of underscores with one underscore per letter.
placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

# stages[6] is the empty hangman drawing, because the player starts with 6 lives.
print(stages[lives])

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # Accept exactly one alphabetic character.
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    # Don't let the same guess cost a life more than once.
    if guess in guessed_letters:
        print(f"You already guessed {guess}.")
        continue
    guessed_letters.append(guess)

    # Rebuild the display using this guess and all earlier correct guesses.
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}; that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"You lose. The word was {chosen_word}.")
    elif "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # The list is ordered so its index matches the remaining lives.
    print(stages[lives])
