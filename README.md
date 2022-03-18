# Blackjack Python Game

My Blackjack game runs through an Heroku Terminal. The game will take in user input and deal cards to both the player and the dealer. 

The rules and conditions for the game are outlined as below:
Cards are drawn from a list data model - [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
There are no jokers in the deck
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1

If the computer has a blackjack (0), then the player loses and vice versa
If the player_hand is over 21, then the player loses and vice versa
If none of the above, then the player with the highest hand wins

![home-page](https://user-images.githubusercontent.com/91907661/153290742-48f5e3aa-489c-417a-9db4-06869f676cc4.png)


## How to play
The game begins by asking you if you would like to play a game of Blackjack, if yes, the game begins.

Both the player and the dealer start the game with a pot of €1000 each
The madatory bet is €30 and you can bet on top of this if you wish.

Random cards are drawn and and the total value of your cards and the dealer's first card is displayed.

The aim of the game is to get to as close to 21 as possible, closer than the dealer, and without going over the value of 21.

You can chose to draw more cards or stay with the hand you have currently. The dealer then continues to draw cards for themselves providing the total value of their hand is not more that 17.

Game concepts and behaviours are explained in more detail in the features section below.


### Each Feature Explained

- __Game Start__

  - You must enter 'y' on keyboard to begin game or 'n' to close application

![question-display](https://user-images.githubusercontent.com/91907661/153291336-e0cd84b7-e701-4b47-8d9b-89fe8de6a1b7.png)


- __Place a bet__
  - All players have a stating pot of €1000
  - The mandatory bet is €30
  - You can either chose to stay at €30 or increase this amount by either
  €20, €40, €80.
  - The dealer will always match the bet that you make
  - Both the player bet and dealer bet are then added to the round pot
  - The value of the round pot is either added to or deducted from 
  value of the player and dealer pots, depending on who wins that round

![radio-buttons](https://user-images.githubusercontent.com/91907661/153291667-c2943dac-587a-4988-b819-f9f7ee53a9f1.png)


- __Feedback: Hit or Stick__
  - After a bet has been placed, the dealer deals the cards to both player and the dealer
  - The player's first 2 cards are revealed and the the dealers first card is revealed
  - The player can either chose to draw another random card or stick with
  the hand(value) they currently have
  - The dealer then continues to draw cards for themselves providing the total value of their hand is not more that 17.
  - Once the dealers hand is above 17, the total values of each hand are revealed


- __Display Winner and remaining Player and Dealer Pots__
  - After Each round has concluded, the WINNER is displayed to the player
  - The total pot for player and dealer is then displayed and their
  values either increment or decrement or stay the same depending on 
  the result of the wound

![icons](https://user-images.githubusercontent.com/91907661/153291941-cf3e1321-7764-451b-b716-f9096a6b6485.png)


- __Play Another Round__
  - The player can then choose to play another round via the input prompt
  - if they wish to do so the deck is cleared and new cards are drawn
  to repeat the process
  - The values of the player pot and dealer pots are kept on from the previous round

![next-alert](https://user-images.githubusercontent.com/91907661/153292940-ff36ffe3-18ee-448b-b380-085ada9853ac.png)


- __End Game__
  - The end game is triggered once either the player pot or dealer pot reaches 0 or a minus value

![next-hide](https://user-images.githubusercontent.com/91907661/153293260-7de11d90-c73f-4de2-be46-7683e6255505.png)


- __Future Features__
  - The end game is triggered once either the player pot or dealer pot reaches 0 or a minus value


### Data Model and Methods Used
I decided to use lists that generated random values for the card values in the game. This was done using random and append methods.

I used quite a few functions to execute the game at each step, several while and for loops were used to output data and check if certain processed were complete in order to move ahead to the next step of the game.

Several if statments were throught the program to verify inputted data and store this data correctly in addition to esnureing the correct information is disaplyed to the end user.


### Testing and Unfixed Bugs


## Deployment
- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://david-maura-rodgers.github.io/JavaScript_Project_2/ 


### Credits for all Content 
- __HTML Code__
  - For Start Button on index page: https://stackoverflow.com/questions/2906582/how-to-create-an-html-button-that-acts-like-a-link
  - Icons come from: https://fontawesome.com/
  - Favicon comes from : https://favicon.io/

- __CSS Code__
  - None

- __JavaScript Code__
  - I looked online at W3 Schools and MDN to get a better understanding of JavaScript concepts when writing the script.
  - I had a look at Stack Overflow on numerous occasions, and though I did try several snippets of code in my project, I never ended up using any of it as it never worked as I needed it to for what I was doing
  - I did however, receive a lot of help in the mentor sessions and guidance on similar projects to get started, along with quite a few online tutor sessions to help me through the logic of what I was trying to achieve with my script. My mentor decided that I should look at https://github.com/Jonathanrange/Rock-Metal-Quiz. The ideas in this project helped me get started in building my own project.

