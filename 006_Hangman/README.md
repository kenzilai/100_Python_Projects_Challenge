# Hangman
## Summary
This game will let the player guess a word by typing in the letter. The game starts with a chosen word from the word file and shows the length of an underscore that will indicate the length of the word. If the player typed in the correct letter, the underscore with get replaced by the correct letter until the player gets all the letters or loses all the lives, then the game will end.

While loop is being used to check if the game is over or continue the guessing. Everytime a player makes a guess, the amount of lives will be updated, and the Ascii art that represents the lives will also be printed.

When the player type in the letter, all inputs will also be changed to lowercase using the lower() method to prevent the unnecessary losing lives.

## Objective  
- Use **not** boolean operator and while loop to check if the condition is met before running the if/else statement
- Import os module and use system() method to clear the console everytime the guess is made
- Modulized the program into main, ascii art and word, then import them into main file in order to get access to the data