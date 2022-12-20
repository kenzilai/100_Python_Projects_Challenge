import os
import random
from hangman_ascii_art import stages, logo
from hangman_word import word_list

print(logo)

chosen_word = random.choice(word_list)
display = []
lives = 6
end_game = False
print(chosen_word)

for letter in chosen_word:
    display += "_"

while not end_game:
    print(stages[lives])
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    os.system("clear")

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    if lives == 0:
        end_game = True
        print(stages[lives])
        print(f"The word is '{chosen_word}'. You have no more lives left. You lose.")

    elif guess in display:
        print(f"You've already guessed '{guess}'.")

    else:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print("You guessed a right letter!")

    if "_" not in display:
        end_game = True
        print(stages[lives])
        print(f"{' '.join(display)}")
        
        print("Good job! You guessed the correct word! You win!")