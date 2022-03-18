def return_winner(player_hand, com_hand):
    '''
    FUNCTION: Compare values of player_hand and com_hand and determine 
    the winner
    '''
    winner = ""
    if player_hand == com_hand:
        return "This round is a draw . . ."
    elif com_hand == 0:
        winner = "com_hand"
        return "You lose - dealer has Blackjack 😱!!"
    elif player_hand == 0:
        winner = "player_hand"
        return "You Win - with a Blackjack 😎"
    elif player_hand > 21:
        winner = "com_hand"
        return "You went over. You lose 😭"
    elif player_hand > 21:
        winner = "player_hand"
        return "Opponent went over. You win 😁"
    elif player_hand > com_hand:
        winner = "player_hand"
        return "You win 😃"
    else:
        winner = "com_hand"
        return "You lose 😤"
    
    return winner
