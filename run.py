# TO RUN CODE: python3 run.py
import random
import sys
import os

# Hold random cards and the value of each hand
player_cards = []
com_cards = []
player_hand = 0
com_hand = 0

# Value of bets entered
# Betting and round over conditions
START_BET = 30
BET_20 = 20
BET_40 = 40
BET_80 = 80
player_bet = 0
dealer_bet = 0
betting_over = False
round_over = False

# Calculate: add or subtract these variables after each bet to trigger
# end game conditions
round_pot = 0
player_pot = 1000
dealer_pot = 1000

# Check end game condition
is_game_over = False

print("----------------------------")
print("WELCOME TO MY BLACKJACK GAME")
print("----------------------------")


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
    global round_pot
    print("Betting always starts at €30\n")
    while not betting_over:
        should_bet = input("Would you like to place a bet? Type 'y' for yes, \
or type 'n' to stay with your  current bet: ").lower()
        if should_bet == "n":
            player_bet = START_BET
            dealer_bet = START_BET
            round_pot = 60
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}\n")
            print("\n")
            betting_over = True
        else:
            print("\n")
            player_bet = int(input("Please enter bet: 20, 40 or 80: "))
        if player_bet == 20:
            player_bet = BET_20 + START_BET
            dealer_bet = player_bet
            round_pot = 100
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}\n")
            print("\n")
            betting_over = True
        if player_bet == 40:
            player_bet = BET_40 + START_BET
            dealer_bet = player_bet
            round_pot = 140
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}\n")
            print("\n")
            betting_over = True
        if player_bet == 80:
            player_bet = BET_80 + START_BET
            dealer_bet = player_bet
            round_pot = 220
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}\n")
            print("\n")
            betting_over = True


def calculate_card_sum(all_cards):
    '''
    FUNCTION: check for a Blackjack:
    a hand with only 2 cards: ace + 10, and return 0
    Take list of both hands (player and com)
    and return the sum of those cards
    '''
    # Check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score
    # 0 represents a blackjack
    if sum(all_cards) == 21 and len(all_cards) == 2:
        return 0
    # Check for an 11 (ace). If the score is already over 21,
    # remove the 11 and replace it with a 1.
    if 11 in all_cards and sum(all_cards) > 21:
        all_cards.remove(11)
        all_cards.append(1)
    return sum(all_cards)


def return_winner(p_hand, c_hand):
    '''
    FUNCTION: Compare values of player_hand and com_hand and determine
    the winner
    '''
    winner = ""
    if p_hand == c_hand:
        print("This round is a draw . . .\n")
    elif c_hand == 0:
        winner = "Dealer"
        print("You lose - dealer has Blackjack 😱\n")
    elif p_hand == 0:
        winner = "Player"
        print("You Win - with a Blackjack 😎\n")
    elif p_hand > 21:
        winner = "Dealer"
        print("You went over. You lose 😭\n")
    elif c_hand > 21:
        winner = "Player"
        print("Opponent went over. You win 😁\n")
    elif p_hand > c_hand:
        winner = "Player"
        print("You win 😃\n")
    else:
        winner = "Dealer"
        print("You lose 😤\n")
    return winner


def play_game():
    '''
    FUNCTION:
    Will start the game - Deal random cards into player's and dealer's hands
    Check conditions to find the winner of the round
    Check for end game condition determine the winner
    '''
    player_cards = []
    com_cards = []
    player_hand = 0
    com_hand = 0
    the_winner = ""
    round_over = False
    is_game_over = False
    global round_pot
    global player_pot
    global dealer_pot

    for card in range(2):
        player_cards.append(random_card())
        com_cards.append(random_card())

    while not round_over:
        player_hand = calculate_card_sum(player_cards)
        com_hand = calculate_card_sum(com_cards)
        print(f"Dealers first card is: {com_cards[0]}\n")
        print(f"Your hand: {player_cards} current score: {player_hand}\n")
        print("\n")
        if player_hand == 0 or com_hand == 0 or player_hand > 21:
            round_over = True
            os.system('cls||clear')
        else:
            player_deal_again = input("Type 'y' to deal \
or any key to stick with your current hand: ").lower()
            print("\n")
            if player_deal_again == "y":
                player_cards.append(random_card())
                print(f"Dealer's hand: {com_cards} current score: {com_hand}")
            else:
                round_over = True
                os.system('cls||clear')

    while com_hand != 0 and com_hand < 17:
        com_cards.append(random_card())
        com_hand = calculate_card_sum(com_cards)

    print(f"Your final hand: {player_cards}, final score: {player_hand}")
    print(f"Computer's final hand: {com_cards}, final score: {com_hand}\n")

    the_winner = return_winner(player_hand, com_hand)
    print(f"THE WINNER: {the_winner}")

    if the_winner == "Player":
        player_pot = player_pot + round_pot
        dealer_pot = dealer_pot - round_pot
    if the_winner == "Dealer":
        player_pot = player_pot - round_pot
        dealer_pot = dealer_pot + round_pot
    print(f"Player Pot is now: €{player_pot}")
    print(f"Dealer Pot is now: €{dealer_pot}\n")
    print("\n")

    round_pot = 0

    while not is_game_over:
        if player_pot >= 1 and dealer_pot >= 1:
            place_bet()
            play_game()
        elif player_pot <= 0:
            print("Your pot is empty")
            print("GAME OVER: You lose . . . .")
            print("\n")
            is_game_over = True
            sys.exit()
        elif dealer_pot <= 0:
            print("Dealer pot is empty!!!")
            print("GAME OVER: You WIN!!!!!!")
            print("\n")
            is_game_over = True
            sys.exit()


# Ask the player if they want to play another round.
# Will end the round and game no
while True:
    try:
        while input("Do you want to start a new round of Blackjack? \
Please type 'y' to continue: ").lower() == "y":
            print("\n")
            player_cards = []
            com_cards = []
            place_bet()
            play_game()
            print("Good luck!")
    except ValueError:
        print("Please enter either y or n")
