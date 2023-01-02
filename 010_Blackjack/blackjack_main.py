import os
import random
from blackjack_art import logo

def blackjack():
    os.system("clear")
    print(logo)
    def deal_card():
        """
        Returns a random card from the deck.
        """
        cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards_deck)
        return card

    player_cards = []
    computer_cards = []
    game_over = False

    def calculate_score(cards):
        """
        Takes a list of cards as input and returns the score.
        """
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(player_score, computer_score):
        if player_score == computer_score:
            return "It's a draw."
        elif player_score == 0:
            return "You have Blackjack. You win."
        elif computer_score == 0:
            return "Computer has Blackjack. You lose."
        elif player_score > 21:
            return "Your score is over 21. You lose."
        elif computer_score > 21:
            return "Computer score is over 21. You win."
        elif player_score > computer_score:
            if player_score == 21:
                return "You have Blackjack. You win."
            else:
                return "You win."
        elif computer_score > player_score:
            if computer_score == 21:
                return "Computer has Blackjack. You lose."
            else:
                return "You lose."

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        os.system("clear")
        print(logo)
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, curent score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            if computer_score != 0 and computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            player_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_deal == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    os.system("clear")
    print(logo)
    print(f"Your final cards: {player_cards}, final score: {player_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

    if input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'y':
        blackjack()

blackjack()