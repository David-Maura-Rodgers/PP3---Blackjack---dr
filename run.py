# Write your code to expect a terminal of 80 characters wide and 24 rows high
# TO RUN CODE: python3 run.py
# The Jack/Queen/King all count as 10
# The Ace can count as 11 or 1
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


import random

# GLOBAL VARIABLES
user_cards = []
com_cards = []
game_over = False


def random_card():
    '''
    FUNCTION: Will loop through available cards
    and assign a random card to player
    '''
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(all_cards)
    return chosen_card


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


# pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has
# a blackjack (0), then the user loses. If the user has a blackjack (0),
# then the user wins. If the user_score is over 21, then the user
# (and vice versa). If none of the above, then the player with the 
# highest score wins
def compare_hands(user_hand, com_hand):
    '''
    FUNCTION: Compare values of user_hand and com_hand and determine the winner
    '''
    if user_hand == com_hand:
        return "This round is a draw . . ."
    elif com_hand == 0:
        return "You lose - dealer has Blackjack!!"
    elif user_hand == 0:
        return "Win with a Blackjack 😎"
    elif user_hand > 21:
        return "You went over. You lose 😭"
    elif com_hand > 21:
        return "Opponent went over. You win 😁"
    elif user_hand > com_hand:
        return "You win 😃"
    else:
        return "You lose 😤"


# This for loop will run twice with 'range(2)'
# use append to have random_card function to output as a list
for i in range(2):
    user_cards.append(random_card())
    com_cards.append(random_card())


# The score will need to be rechecked with every new card drawn
# and the checks in 'calculate_card_sum' need to be repeated 
# until the game ends.
while not game_over:
    # Call 'calculate_score'. If the computer or the user has a blackjack (0)
    # or if the user's score is over 21, then the game ends.
    user_hand = calculate_card_sum(user_cards)
    com_hand = calculate_card_sum(com_cards)
    print(f"Your hand: {user_cards} current score: {user_hand}")
    print(f"Dealers first card is: {com_cards[0]}")

    if user_hand == 0 or com_hand == 0 or user_hand > 21:
        game_over = True
    else:
        user_deal_again = input("Type 'y' to deal \
again or 'n' to pass: ").lower()
        if user_deal_again == "y":
            user_cards.append(random_card())
        else:
            game_over = True


# Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has
# a score less than 17.
while com_hand != 0 and com_hand < 17:
    com_cards.append(random_card())
    com_score = calculate_card_sum(com_cards)

# --- BUGS ---- \\
# user_cards += new_card did not work, so had to use append to put random_card 
# function to output as a list
    # new_card = random_card()
    # user_cards.append(new_card)
    # FIX: user_cards.append = [random_card()]
