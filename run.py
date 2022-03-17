# Write your code to expect a terminal of 80 characters wide and 24 rows high
# TO RUN CODE: python3 run.py

'''
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The the Ace can count as 11 or 1.
Use the following list as the deck of cards:
[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
'''

import random

# GLOBAL VARIABLES
user_cards = []
com_cards = []
user_hand = 0
com_hand = 0
game_over = False
START_BET = 30
BET_20 = 20
BET_40 = 40
BET_80 = 80
player_bet = 0
dealer_bet = 0
betting_over = False
is_game_over = False
round_pot = 0
player_pot = 1000
dealer_pot = 1000


def random_card():
    '''
    FUNCTION: Will loop through available cards
    and then return a randomly selected one from the list
    '''
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(all_cards)
    return chosen_card


def place_bet():
    '''
    FUNCTION: Ask player to place bet from 3 options: 20, 40, 80
    Dealer will match this bet and both bets are added to the pot,
    for that round
    '''
    betting_over = False
    player_bet = 0
    dealer_bet = 0
    round_pot = 0
    print("Betting always starts at €30")
    while not betting_over:
        should_bet = input("Would you like to place bet? 'y' for yes,\
'n' for no: ").lower()
        if should_bet == "n":
            player_bet = START_BET
            dealer_bet = START_BET
            round_pot = player_bet + dealer_bet
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}")
            print("\n")
            betting_over = True
        else:
            player_bet = int(input("Please enter bet: 20, 40 or 80: "))
        if player_bet == 20:
            player_bet = BET_20 + START_BET
            dealer_bet = player_bet
            round_pot = player_bet + dealer_bet
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}")
            print("\n")
        if player_bet == 40:
            player_bet = BET_40 + START_BET
            dealer_bet = player_bet
            round_pot = player_bet + dealer_bet
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}")
            print("\n")
        if player_bet == 80:
            player_bet = BET_80 + START_BET
            dealer_bet = player_bet
            round_pot = player_bet + dealer_bet
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}")
            print("\n")


def calculate_card_sum(all_cards):
    '''
    FUNCTION: check for a Blackjack:
    a hand with only 2 cards: ace + 10, and return 0
    FUNCTION: Take list of both hands (user and com)
    and return the sum of those cards
    '''
    if sum(all_cards) == 21 and len(all_cards) == 2:
        return 0
    # Check for an 11 (ace). If the score is already over 21:
    # remove the 11 and replace it with a 1
    if 11 in all_cards and sum(all_cards) > 21:
        all_cards.remove(11)
        all_cards.append(1)
    return sum(all_cards)


# pass in the user_hand and com_hand. If the computer and user
# both have the same score, then it's a draw.
# If the computer has a blackjack (0), then the user loses. (vice versa)
# If the user_hand is over 21, then the user loses (vice versa)
# If none of the above, then the player with the highest hand wins
def compare_hands(user_hand, com_hand):
    '''
    FUNCTION: Compare values of user_hand and com_hand and determine the winner
    '''
    if user_hand == com_hand:
        return "This round is a draw . . ."
    elif com_hand == 0:
        print(f"Player Pot is now: €{player_pot}")
        print(f"Dealer Pot is now: €{dealer_pot}")
        print("\n")
        return "You lose - dealer has Blackjack!!"
    elif user_hand == 0:
        print(f"Player Pot is now: €{player_pot}")
        print(f"Dealer Pot is now: €{dealer_pot}")
        print("\n")
        return "You Win - with a Blackjack 😎"
    elif user_hand > 21:
        print(f"Player Pot is now: €{player_pot}")
        print(f"Dealer Pot is now: €{dealer_pot}")
        print("\n")
        return "You went over. You lose 😭"
    elif com_hand > 21:
        print(f"Player Pot is now: €{player_pot}")
        print(f"Dealer Pot is now: €{dealer_pot}")
        print("\n")
        return "Opponent went over. You win 😁"
    elif user_hand > com_hand:
        print(f"Player Pot is now: €{player_pot}")
        print(f"Dealer Pot is now: €{dealer_pot}")
        print("\n")
        return "You win 😃"
    else:
        print(f"Player Pot is now: €{player_pot}")
        print(f"Dealer Pot is now: €{dealer_pot}")
        print("\n")
        return "You lose 😤"
    

def play_game():
    '''
    FUNCTION: Will start the game:
    Deal random cards into player's and dealer's hands
    Check for end game condition and ask if user wants to play again
    '''
    user_cards = []
    com_cards = []
    user_hand = 0
    com_hand = 0
    game_over = False
    # This for loop will run twice with 'range(2)'
    # use append to have 'random_card' FUNCTION to output as a list
    for card in range(2):
        user_cards.append(random_card())
        # print(card_art[user_hand])
        com_cards.append(random_card())
        # print(card_art[com_hand])

    # The score will need to be rechecked with every new card drawn
    # and the checks in 'calculate_card_sum' need to be repeated
    # until the game ends.
    while not game_over:
        # Call 'calculate_card_sum'. If the computer or the user has a
        # blackjack (0) or if the user's score is over 21, then the game ends.
        user_hand = calculate_card_sum(user_cards)
        com_hand = calculate_card_sum(com_cards)
        print(f"Your hand: {user_cards} current score: {user_hand}")
        print(f"Dealers first card is: {com_cards[0]}")
        print("\n")

        player_pot = 1000
        dealer_pot = 1000
        round_pot = 0

        if com_hand == 0:
            player_pot = player_pot - round_pot
            dealer_pot = dealer_pot + round_pot
        elif user_hand == 0:
            player_pot = player_pot + round_pot
            dealer_pot = dealer_pot - round_pot
        elif user_hand > 21:
            player_pot = player_pot - round_pot
            dealer_pot = dealer_pot + round_pot
        elif com_hand > 21:
            player_pot = player_pot + round_pot
            dealer_pot = dealer_pot - round_pot
        elif user_hand > com_hand:
            player_pot = player_pot + round_pot
            dealer_pot = dealer_pot - round_pot
        else:
            player_pot = player_pot - round_pot
            dealer_pot = dealer_pot + round_pot

        if user_hand == 0 or com_hand == 0 or user_hand > 21:
            game_over = True
        else:
            user_deal_again = input("Type 'y' to deal \
again or 'n' to pass: ").lower()
            if user_deal_again == "y":
                user_cards.append(random_card())
                print(f"Dealer's hand: {com_cards} current score: {com_hand}")
            else:
                game_over = True


# Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has
# a score less than 17.
    while com_hand != 0 and com_hand < 17:
        com_cards.append(random_card())
        com_hand = calculate_card_sum(com_cards)

    print(f"Your final hand: {user_cards}, final score: {user_hand}")
    print(f"Computer's final hand: {com_cards}, final score: {com_hand}")
    print(compare_hands(user_hand, com_hand))


# Ask the user if they want to restart the game.
while input("Do you want to start a new round of Blackjack? \
Type 'y' or 'n': \n").lower() == "y":
    print("\n")
    user_cards = []
    com_cards = []
    place_bet()
    play_game()
    

# --- BUGS ---- \\
# user_cards += new_card did not work, so had to use append to put random_card
# function to output as a list
    # new_card = random_card()
    # user_cards.append(new_card)
    # FIX: user_cards.append = [random_card()]
# Hand were not being cleared after each round and kept being appended to
# player and dealer hands

