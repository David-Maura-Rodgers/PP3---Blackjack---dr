# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# TO RUN CODE: python3 run.py

# The Jack/Queen/King all count as 10
# The Ace can count as 11 or 1
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random


def random_card():
    '''
    FUNCTION: Will loop through available cards and assign a card to player
    '''
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(all_cards)
    return chosen_card


# Deal the user and computer 2 cards each
user_cards = []

# This for loop will run twice 'range(2)'
# Assign new card = to out put of random
for _ in range(2):
    new_card = random_card()
    user_cards += new_card


# --- BUGS ----