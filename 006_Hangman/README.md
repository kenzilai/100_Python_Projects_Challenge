# Hangman
## Summary
This game will let the player to guess a word by typeing in the letter. The game started with a chosen word from a word file and shows a length of underscore that allow the player see the length of the word. if the player typed in a correct letter, the underscore with be replace with the correct letter until the player get all the letters or lose all the lives then the game will end.

While loop is being used to achieve the goal to check if the game is ended in order to continue the guessing. Everythime when player make a guess, the amount of lives will be updated and the Ascii art that represented the lives will also be printed.

When the player type in the letter, all inputs will also be changed to the lowercase using lower() method to prevent the unecessary losing lives. 

## Objective  
- Use **not** boolean operator and while loop to check if the condition is met before running the if/else statement
- Import os module and use system() method to clear the console everytime the guess is made
- Modulized the program into main, ascii art and word, then import them into main file in order to get access to the data