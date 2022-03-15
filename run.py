# Write your code to expect a terminal of 80 characters wide and 24 rows high

# TO RUN CODE: python3 run.py

# The Jack/Queen/King all count as 10
# The Ace can count as 11 or 1
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random


def random_card():
    '''
    FUNCTION: Will loop through available cards
    and assign a random card to player
    '''
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(all_cards)
    return chosen_card


# Deal the user and computer 2 cards each
user_cards = []
com_cards = []

# This for loop will run twice with 'range(2)'
# use append to have random_card function to output as a list
for i in range(2):
    user_cards.append(random_card())
    com_cards.append(random_card())


# FUNCTION takes a List of cards as input and returns the score. 
def calucate_card_sum():
    






# --- BUGS ---- \\
# user_cards += new_card did not work, so had to use append to put random_card 
# function to output as a list
    # new_card = random_card()
    # user_cards.append(new_card)
    # FIX: user_cards.append = [random_card()]
