import os
from random import randint
from number_guessing_game_art import logo

EASY = 10
HARD = 5

def check_answer(guess, answer, turns):
    """
    Check answer after guess. Return the number of turns remaining.
    """
    if guess == answer:
        print(f"The number is {answer}, you guess a correct number!")
    elif guess > answer:
        print("Too hgh.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1

def difficulty():
    """
    Return the number of turns depends on what level player choose.
    """
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("The number is between 1 and 100.")
    level = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if level == "easy":
        os.system("clear")
        print(logo)
        print("Your have 10 turns to attempt.")
        return EASY
    elif level == "hard":
        os.system("clear")
        print(logo)
        print("Your have 5 turns to attempt.")
        return HARD

def number_guessing_game():
    answer = randint(1, 100)
    turns = difficulty()
    guess = 0

    while guess != answer:
        guess = int(input("Make a guess: "))
        if turns == 1:
            os.system("clear")
            print(logo)
            print(f"You have used all your attempts, the correct number is {answer}.")
            play_again = input("Do you want to play again? Type 'yes' or 'no': ")
            if play_again == "yes":
                os.system("clear")
                number_guessing_game()
            return
        elif guess != answer:
            os.system("clear")
            print(logo)
            turns = check_answer(guess, answer, turns)
            print(f"You have {turns} attempts remaining to guess the number.")
            print("Guess again.")

number_guessing_game()