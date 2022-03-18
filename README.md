# Blackjack Python Game

My Blackjack game runs through an Heroku Terminal. The game will take in user input and deal cards to both the player and the dealer. 

The rules and conditions for the game are outlined as below:
Cards are drawn from a list data model - [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
There are no jokers in the deck
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1


The first question in the question array will be displayed on this page. The questions will change dynamically when the user has selected a radio button that corresponds with the answer they wish to choose. They will then click on the Next Question button to get the next question in the array. This process repeats until they reach the end of the quiz. They can then click the Restart Button to try the quiz again.

![home-page](https://user-images.githubusercontent.com/91907661/153290742-48f5e3aa-489c-417a-9db4-06869f676cc4.png)

![quiz-page](https://user-images.githubusercontent.com/91907661/153291017-5b302647-6f0c-47a5-bab5-9aa5b179b20e.png)


## Features 

Below is a list of features that I have on this site which I will detail individually. There is a welcome page with a Start Quiz Button that will take the user to the main quiz page. On this quiz page, there is a quiz area which contains a question display area and four radio buttons that the user can select from to register an answer. And below this, but still within the same containing div, the user will receive feedback on their answers. 

There is another div below which contains dynamic icons in response to user input. And finally two buttons: Next Question and Restart Quiz along with a score tracker at the bottom. 

I have also added a favicon for the site.

### Each Feature Explained

- __Question Display__

  - The question display will dynamically display every question in the array as the user progress with the quiz

![question-display](https://user-images.githubusercontent.com/91907661/153291336-e0cd84b7-e701-4b47-8d9b-89fe8de6a1b7.png)


- __Radio Buttons for Answer Selection__

  - There are four radio buttons from which the user can click to register an answer
  - Once they select an answer all other radio buttons are disabled

![radio-buttons](https://user-images.githubusercontent.com/91907661/153291667-c2943dac-587a-4988-b819-f9f7ee53a9f1.png)


- __Feedback: rolling and at quiz end__

  - The feedback display will display "Correct!" or "Incorrect! The correct answer . . ." each time the user chooses an answer. This always corresponds to either the correct or incorrect answer.
  - When the user reaches the last question in the array, the feedback text will turn purple and let them know their final score and that the quiz has ended
- __Icons (Correct and Incorrect)__

  - There are two icons which respond to the user input and responds to the checkAnswer function to supply visual feedback 
  - Both screenshots below show both icon responses

![icons](https://user-images.githubusercontent.com/91907661/153291941-cf3e1321-7764-451b-b716-f9096a6b6485.png)

![feedback-end](https://user-images.githubusercontent.com/91907661/153292342-1a7bd361-41eb-4c54-b0c9-12ac0982bd69.png)


- __Buttons: Next Question & Restart Quiz__
- __Score Tracker__

  - The Next Question and Restart Quiz are displayed as below and will navigate the quiz accordingly
  - When the user hovers over either button, the button responds dynamically as shown below and reverts back when the user 
  moves cursor away from the button
  - If the user clicks on the next button after the last question - they will receive an alert
  - Once the user clicks OK on the alert, the next button will disappear and the user can click the Restart Button
  - (The Restart Button can be activated at any time)
  - The score tracker is below the buttons and displays a running total as evidenced below and in previous screenshots

![next-alert](https://user-images.githubusercontent.com/91907661/153292940-ff36ffe3-18ee-448b-b380-085ada9853ac.png)

![next-hide](https://user-images.githubusercontent.com/91907661/153293260-7de11d90-c73f-4de2-be46-7683e6255505.png)


## Lighthouse Score

Please see below for lighthouse report:

![lighthouse](https://user-images.githubusercontent.com/91907661/153421986-3d3fa1d4-fb44-4cda-a356-4c2fdcc07092.png)

  
### Validator Testing (HTML, CSS, JavaScript)

- HTML (index page)
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fdavid-maura-rodgers.github.io%2FJavaScript_Project_2%2F)
- HTML (quiz page)
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fdavid-maura-rodgers.github.io%2FJavaScript_Project_2%2Fquiz.html%3F)

- CSS (index page)
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdavid-maura-rodgers.github.io%2FJavaScript_Project_2%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- CSS (quiz page)
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdavid-maura-rodgers.github.io%2FJavaScript_Project_2%2Fquiz.html%3F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

- JavaScript
  - No errors were found using JSHint validator [(JShint) validator](https://jshint.com/)
  Screenshot is shown below: 

  ![jshint](https://user-images.githubusercontent.com/91907661/153269134-e6066486-774f-4757-a1bb-2f08d898d7a1.png)


- __Warnings__
  - I received the below from both pages when doing the CSS validator check. They just seem to be toolkit warnings for the icons I am using from Font Awesome (this doesn't affect the user's experience of the site in anyway):
  - moz-osx-font-smoothing is a vendor extension
	- webkit-font-smoothing is a vendor extension
	- ms-filter is a vendor extension
	- ms-filter is a vendor extension
	- ms-filter is a vendor extension
	- ms-filter is a vendor extension
	- ms-filter is a vendor extension
	- The property clip is deprecated
	- The property clip is deprecated


### Unfixed Bugs or Other Quirks

- There doesn't appear to be any bugs with the functionality of the quiz in of itself. I have tested it several times, as can be expected during the time I was developing the script. All seems to work fine and all functions called upon appear to work with no problems.

- Font Awesome:
  - As mentioned previously above, I get warnings about vendor extensions with my use of Font Awesome, but nothing that seems to be critical or impedes the functionality of the site for the user.

- However, I have put a lot of work into responsiveness  for this site and have had quite a few challenges, many of which are resolved now. My comments on this are as below:
  - I have had to take the no repeat attribute off the background img for the 1024 px media query as the image would not cover the entire screen as hoped.
  - The icons within the icon area div are generally well centered within its containing div, however on some screens, it can look a bit off kilter. With enough time in the future, I would hope to have this 100%. 
  - I have added media queries for 5 breakpoints (1440px, 1240px, 992px, 576px, 375px) to ensure as much integrity as possible. Screenshots evidence the below:

  ![1440px](https://user-images.githubusercontent.com/91907661/153282167-9ad76422-ee8f-45af-b5e4-42be52e16138.png)

  ![1024px](https://user-images.githubusercontent.com/91907661/153282524-a803ea18-33d9-4d71-a6d5-43983ab6e003.png)

  ![768px](https://user-images.githubusercontent.com/91907661/153282682-e034dc17-4bb4-4c98-9f70-b59c024e1c08.png)

  ![425px](https://user-images.githubusercontent.com/91907661/153282823-49ac5e73-b45b-454c-86cc-2ecf1f435f6e.png)

  ![320px](https://user-images.githubusercontent.com/91907661/153282999-3b5d889e-ce26-4289-b353-ef37541c3afc.png)


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

### Media
- The background image is from this Open Source site: https://pixabay.com/illustrations/question-mark-pile-questions-symbol-2492009/
