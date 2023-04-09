import os
import random
from blackjack import art

# random card deck
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

# calculate socore from random cards 
def calculate_score(cards):
    """Take a list of cards and return the score calculator from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

# Create a function called compare
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 🥳"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# create play game function
def play_game():
    print(art.logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # call calculate_score and check score and should deal yes or no (for user)
    while not is_game_over:
        # call calculate_score().    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # check score and should deal yes or no 
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #  compare with computre score
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_score}, final score: {user_score}")
    print(f"Computer final hand: {computer_score}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# ask play game
while input("Do you wnat to play a game for Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('clear')
    play_game()