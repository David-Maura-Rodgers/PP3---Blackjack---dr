START_BET = 30
BET_20 = 20
BET_40 = 40
BET_80 = 80
player_bet = 0
dealer_bet = player_bet

print("Betting always starts at €30")
should_continue = input("Would you like to place bet? 'y' for yes,\
'n' for no. \n").lower()
player_bet = int(input("Please enter bet: 20, 40 or 80"))

print("Betting always starts at €30")
# should_continue = input("Would you like to place bet? 'y' for yes, 
# 'n' for no. \n").lower()
player_bet = int(input("Please enter bet: 20, 40 or 80"))
if player_bet == 20:
    player_bet = BET_20 + START_BET
    print(player_bet)
elif player_bet == 40:
    player_bet = BET_40 + START_BET
    print(player_bet)
elif player_bet == 40:
    player_bet = BET_80 + START_BET
    print(player_bet)
