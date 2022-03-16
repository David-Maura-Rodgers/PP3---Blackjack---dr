# TO RUN CODE: python3 test.py

START_BET = 30
BET_20 = 20
BET_40 = 40
BET_80 = 80
player_bet = 0
dealer_bet = None
betting_over = False
bets_placed = 0
game_over = False


def place_bet():
    '''
    FUNCTION:
    '''
    global betting_over
    global bets_placed
    global player_bet
    global dealer_bet
    print("Betting always starts at €30")
    
    while not betting_over:
        should_bet = input("Would you like to place bet? 'y' for yes,\
'n' for no: ").lower()
        if should_bet == "n":
            betting_over = True
        else:
            player_bet = int(input("Please enter bet: 20, 40 or 80: "))
        if player_bet == 20:
            player_bet = BET_20 + START_BET
            dealer_bet = player_bet
            print(f" Player bet this hand: €{player_bet}")
            print(f" Dealer bet this hand: €{dealer_bet}")
        if player_bet == 40:
            player_bet = BET_40 + START_BET
            dealer_bet = player_bet
            print(f" Player bet this hand: €{player_bet}")
            print(f" Dealer bet this hand: €{dealer_bet}")
        if player_bet == 80:
            player_bet = BET_80 + START_BET
            dealer_bet = player_bet
            print(f" Player bet this hand: €{player_bet}")
            print(f" Dealer bet this hand: €{dealer_bet}")

        return player_bet
        return dealer_bet


# def display_bet():
#     '''
#     FUNCTION:
#     '''
#     # global MAX_BET
#     # global player_bet
#     player_bet = int(input("Please enter bet: 20, 40 or 80: "))

#     if player_bet == 20:
#         player_bet = BET_20 + START_BET
#         dealer_bet = player_bet
#         print(f" Player bet this hand: €{player_bet}")
#         print(f" Dealer bet this hand: €{dealer_bet}")
#     elif player_bet == 40:
#         player_bet = BET_40 + START_BET
#         dealer_bet = player_bet
#         print(f" Player bet this hand: €{player_bet}")
#         print(f" Dealer bet this hand: €{dealer_bet}")
#     elif player_bet == 80:
#         player_bet = BET_80 + START_BET
#         dealer_bet = player_bet
#         print(f" Player bet this hand: €{player_bet}")
#         print(f" Dealer bet this hand: €{dealer_bet}")


place_bet()
# display_bet()