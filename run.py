# Write your code to expect a terminal of 80 characters wide and 24 rows high

# TO RUN CODE: python3 run.py

# The Jack/Queen/King all count as 10
# The Ace can count as 11 or 1
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random


# FUNCTION takes a List of cards as input and returns the score. 
def calculate_card_sum(all_cards):
    '''
    FUNCTION: check for a Blackjack:
    a hand with only 2 cards: ace + 10, and return 0
    FUNCTION: Take list of both hands (user and com)
    and return the sum of those cards
    '''
    # CODE: if sum(cards) == 21 and len(cards) == 2:
    if 11 in all_cards and 10 in all_cards and len(all_cards) == 2:
        return 0
   
    # Check for an 11 (ace). If the score is already over 21:
    # remove the 11 and replace it with a 1
    if 11 in all_cards and sum(all_cards) > 21:
        all_cards.remove(11)
        all_cards.append(1)
    
    return sum(all_cards)


def random_card():
    '''
    FUNCTION: Will loop through available cards
    and assign a random card to player
    '''
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(all_cards)
    return chosen_card


# GLOBAL VARIABLES
user_cards = []
com_cards = []
game_over = False

# This for loop will run twice with 'range(2)'
# use append to have random_card function to output as a list
for i in range(2):
    user_cards.append(random_card())
    com_cards.append(random_card())


# Call 'calculate_score'. If the computer or the user has a blackjack (0)
# or if the user's score is over 21, then the game ends.
user_hand = calculate_card_sum(user_cards)
com_hand = calculate_card_sum(com_cards)
print(f"Your hand: {user_cards} current score: {user_hand}")
print(f"Dealers first card is: {com_cards[0]}")

if user_hand == 0 or com_hand == 0 or user_hand > 21:
    game_hand = True


# --- BUGS ---- \\
# user_cards += new_card did not work, so had to use append to put random_card 
# function to output as a list
    # new_card = random_card()
    # user_cards.append(new_card)
    # FIX: user_cards.append = [random_card()]
