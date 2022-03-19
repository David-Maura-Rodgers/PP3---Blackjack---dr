

# Blackjack Python Game

Here is the live version of my project - https://blackjack-david-r.herokuapp.com/

My Blackjack game runs through a Heroku Terminal. The game will take in user input and deal cards to both the player and the dealer. 

The rules and conditions for the game are outlined as below:
- Cards are drawn from a list data model - [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- There are no jokers in the deck
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1
- If the computer has a blackjack 21 or 0; then the player loses and vice versa
- If the player's hand is over 21, then the player loses and vice versa
- If none of the above, then the player with the highest hand wins

![Home](https://user-images.githubusercontent.com/91907661/159094522-10c92534-568c-4398-9542-15e0346a1be1.png)


## How to play
The game begins by asking you if you would like to play a game of Blackjack, if yes, the game begins.

Both the player and the dealer start the game with a pot of €1000 each

The mandatory bet is €30 and you can bet on top of this if you wish.

Random cards are drawn and the total value of your cards and the dealer's first card is displayed.

The aim of the game is to get to as close to 21 as possible, closer than the dealer, and without going over the value of 21.

You can choose to draw more cards or stay with the hand you have currently. The dealer then continues to draw cards for themselves providing the total value of their hand is not more than 17.

Game concepts and behaviours are explained in more detail in the features section below.


### Each Feature Explained

- __Game Start__

  - You must enter 'y' on keyboard to begin game or 'n' to close application

![Place bet](https://user-images.githubusercontent.com/91907661/159094705-b0995e41-f613-4bb4-b354-601210d196e9.png)


- __Place a bet__
  - All players have a stating pot of €1000.
  - The mandatory bet is €30.
  - You can either choose to stay at €30 or increase this amount by either.
  €20, €40, €80.
  - The dealer will always match the bet that you make.
  - Both the player bet and dealer bet are then added to the round pot.
  - The value of the round pot is either added to or deducted from the value of the player and dealer pots, depending on who wins that round.

![Choose bet amount](https://user-images.githubusercontent.com/91907661/159094900-deee0671-be38-49e2-8549-b6d64ef66aec.png)


- __Feedback: Hit or Stick__
  - After a bet has been placed, the dealer deals the cards to both player and the dealer
  - The player's first 2 cards are revealed and the the dealers first card is revealed
  - The player can either choose to draw another random card or stick with the hand(value) they currently have
  - The dealer then continues to draw cards for themselves providing the total value of their hand is not more than 17.
  - Once the dealer's hand is above 17, the total values of each hand are revealed


- __Display Winner and remaining Player and Dealer Pots__
  - After each round has concluded, the WINNER is displayed to the player
  - The total pot for player and dealer is then displayed and their values either increment or decrement or stay the same depending on 
  the result of the round

![Round Display](https://user-images.githubusercontent.com/91907661/159095160-b84c8283-e455-4342-829e-bfb4b591bbf6.png)

![display round winner](https://user-images.githubusercontent.com/91907661/159095267-0be6a9c6-0dbe-46f7-9736-57b180b1564c.png)


- __Play Another Round__
  - The player can then choose to play another round via the input prompt
  - if they wish to do so the deck is cleared and new cards are drawn to repeat the process
  - The values of the player pot and dealer pots are kept on from the previous round


- __End Game__
  - The end game is triggered once either the player pot or dealer pot reaches 0 or a minus value

![Display game winner](https://user-images.githubusercontent.com/91907661/159095814-5e100df7-d79b-47c5-a694-b7033dfcdaa9.png)


- __Future Features__
  - Have player choose from a range of starting pots
  - Have visuals added with corresponding card images for the cards drawn by the player


### Data Model and Methods Used
I decided to use lists that generated random values for the card values in the game. This was done using random and append methods.

I used quite a few functions to execute the game at each step, several while and for loops were used to output data and check if certain 
processes were complete in order to move ahead to the next step of the game.

Several if statements were used throughout the program to verify inputted data and store this data correctly in addition to ensuring the correct information is displayed to the end user.


### Testing and Unfixed Bugs

- __Testing__
  - Manual testing in local repository
  - Testing output and appearance to end user in Heroku terminal
  - Passed through PEP8 Linter with no issues - http://pep8online.com/checkresult


- __Solved Bugs__
  - Tried adding random cards into list using += which didn't work, so used append function instead
  - Hands were not being cleared after each round and kept being appended to player and dealer hands every time. So I cleared them each time in a while loop as shown below:
while input("Do you want to start a new round of Blackjack? \
Type 'y' or 'n': ").lower() == "y":
    print("\n")
    player_cards = []
    com_cards = []
    place_bet()
    play_game()
- Also had a lot of trouble resetting the round pot value after each round, after a mentor session, we figured out that I had been redefining this variable too many times in the application. Defining these variables once in the global scope of application fixed this issue


- __Remaining Bugs__
  - Dealer's first card is displayed every time a cards is drawn by the player, it does not harm the functionality of the game in any way, 
it would just be tidier if it only displayed once at the beginning of every round
  - Can't get application to tell user to enter either 20, 40 or 80 only if user types any other value


### Deployment
This project was deployed using Code Institute's mock terminal for Heroku
- The steps to deploy are as follows: 
  - Fork or clone this repository 
  - Create a new Heroku app
  - Set the buildpack to Python and NodeJS in that order
  - Link Heroku app to this repository
  - Click on deploy
  - My Heroku link to this application is here: https://dashboard.heroku.com/apps/blackjack-david-r/deploy/github


### Credits for all Content 
- https://www.wikihow.com/Play-Blackjack
- https://stackoverflow.com/questions/73663/how-to-terminate-a-script
- https://stackoverflow.com/questions/2084508/clear-terminal-in-python
- Had several mentor and tutor sessions to work through ideas and bugs in code in search of solutions
