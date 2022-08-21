# Functional Testing
 
## **Authentication tests**

<br>

**Description:**
 
Ensure that user can start the game by pressing 'y' or keyboard
 
Steps:
 
1. Navigate to [Blackjack Python Game](https://david-r-blackjack.herokuapp.com/)
2. Hit 'y' on keyboard when prompted by input to start the game
 
Expected:
 
Game starts and user is asked to raise the default bet of €30 with 'y' or 'n' input prompt
 
Actual:
 
Game starts and user is asked to raise the default bet of €30 with 'y' or 'n' input prompt
 
<hr>
<br>

**Description:**
### **Start Game**
Ensure that user can choose to **not start** the game by pressing 'n' or keyboard
 
Steps:
 
1. Navigate to [Blackjack Python Game](https://david-r-blackjack.herokuapp.com/)
2. Hit 'n' on keyboard when prompted by input to start the game
 
Expected:
 
Game does not start and user is given feedback message to say **Goodbye. Hopefully see you soon!**
 
Actual:
 
Game does not start and user is given feedback message to say **Goodbye. Hopefully see you soon!**

<hr>
<br>

**Description:**
### **Start (Error Handling)**
Ensure start game input can handle invalid input: Any input that is not either 'y' or 'n' (both inputs are taken as lower case so caps lock on won't cause any errors)
 
Steps:
 
1. Navigate to [Blackjack Python Game](https://david-r-blackjack.herokuapp.com/)
2. Hit 'a' (other string) on keyboard when prompted by the input to start the game
3. Hit 1 (integer) on keyboard when prompted by the input to start the game
4. Hit Enter (null value) on keyboard when prompted by the input to start the game
5. Hit '#' (character) on keyboard when prompted by the input to start the game
 
Expected:
 
Game does not start and user is given feedback message to say **Invalid Input: Please enter either Y or N**
 
Actual:
 
Game does not start and user is given feedback message to say **Invalid Input: Please enter either Y or N**

<hr>
<br>

**Description:**
### **Raise Bet**
Ensure raise bet input can handle invalid input: Any input that is not either 'y' or 'n' (both inputs are taken as lower case so caps lock on won't cause any errors)
 
Steps:
 
1. Navigate to [Blackjack Python Game](https://david-r-blackjack.herokuapp.com/)
2. Hit 'a' (other string) on keyboard when prompted by the input to raise the default bet
3. Hit 1 (integer) on keyboard when prompted by the input to raise the default bet
4. Hit Enter (null value) on keyboard when prompted by the input to raise the default bet
5. Hit '#' (character) on keyboard when prompted by the input to raise the default bet
 
Expected:
 
Game does not continue and user is given feedback message to say **Invalid Input: Please enter either Y or N**
 
Actual:
 
Game does not continue and user is given feedback message to say **Invalid Input: Please enter either Y or N**

<hr>
<br>

**Description:**
### **Place Bet**
Ensure place bet input can handle invalid input: Any input that is not either 20, 40 or 80 (only these integers are acceptable)
 
Steps:
 
1. Navigate to [Blackjack Python Game](https://david-r-blackjack.herokuapp.com/)
2. Hit 'a' (string) on keyboard when prompted by the input to select bet value (20, 40, 80)
3. Hit 1 (integer) on keyboard when prompted by the input to select bet value (20, 40, 80)
4. Hit Enter (null value) on keyboard when prompted by the input to select bet value (20, 40, 80)
5. Hit '#' (character) on keyboard when prompted by the input to select bet value (20, 40, 80)
 
Expected:
 
Game does not continue and user is given feedback message to say **Invalid Input: Please enter a number** 

Or **Incorrect amount: please select 20, 40 or 80** if they enter any integer that does not match either 20, 40 or 80
 
Actual:
 
Game does not continue and user is given feedback message to say **Invalid Input: Please enter a number** 

Or **Incorrect amount: please select 20, 40 or 80** if they enter any integer that does not match either 20, 40 or 80

<hr>
<br>

**Description:**
### **Deal another card**
Ensure deal another card can handle invalid input: Any input that is not either 'y' or 'n' (both inputs are taken as lower case so caps lock on won't cause any errors)

Steps:
 
1. Navigate to [Blackjack Python Game](https://david-r-blackjack.herokuapp.com/)
2. Hit 'a' (other string) on keyboard when prompted by the input to deal yourself another card
3. Hit 1 (integer) on keyboard when prompted by the input to deal yourself another card
4. Hit Enter (null value) on keyboard when prompted by the input to deal yourself another card
5. Hit '#' (character) on keyboard when prompted by the input deal yourself another card
 
Expected:
 
Game does not continue and user is given feedback message to say **Invalid Input: Please enter either Y or N**
 
Actual:
 
Game does not continue and user is given feedback message to say **Invalid Input: Please enter either Y or N**