class NumberGuessingGame {
    constructor() {
      this.randomNumber = this.generateRandomNumber();
      this.attempts = 0;
      this.isGuessCorrect = false;
      this.rl = require("readline").createInterface({
        input: process.stdin,
        output: process.stdout,
      });
    }
  
    generateRandomNumber() {
      return Math.floor(Math.random() * 10) + 1;
    }
  
    startGame() {
      console.log("-------------> Welcome to the Number Guessing Game! ------------------------>");
      console.log("Try to guess the random number between 1 and 10.");
  
      this.getUserGuess();
    }
  
    getUserGuess() {
      this.rl.question("Enter your guess: ", (userInput) => {
        const userGuess = parseInt(userInput);
  
        if (isNaN(userGuess) || userGuess < 1 || userGuess > 10) {
          console.log("Please enter a valid number between 1 and 10.");
          this.getUserGuess();
        } else {
          this.attempts++;
  
          if (userGuess === this.randomNumber) {
            this.isGuessCorrect = true;
            console.log(`Congratulations! You guessed the correct number (${this.randomNumber}) in ${this.attempts} attempts.`);
  
            this.askToPlayAgain();
          } else {
            if (userGuess < this.randomNumber) {
              console.log("Try a higher number.");
            } else {
              console.log("Try a lower number.");
            }
            this.getUserGuess();
          }
        }
      });
    }
  
    askToPlayAgain() {
      this.rl.question("Do you want to play again? (yes/no): ", (playAgain) => {
        if (playAgain.toLowerCase() === "yes") {
          this.randomNumber = this.generateRandomNumber();
          this.attempts = 0;
          this.isGuessCorrect = false;
          console.log("Great! Let's play again.");
          this.getUserGuess();
        } else {
          console.log("Thank you for playing!");
          this.rl.close();
        }
      });
    }
  }
  
  // Create an instance of the game and start it
  const game = new NumberGuessingGame();
  game.startGame();
  