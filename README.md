
The general behavior we want to implement is described below. 

1. The computer must select a word at random from the list of available words provided in words.txt. Note that words.txt contains words in  all lowercase letters .
2. The user is given a certain number of guesses at the beginning.
3. The game is interactive; the user inputs their guess and the computer either:
a. reveals the letter if it exists in the secret word
b. penalizes the user and updates the number of guesses remaining
4. The game ends when either the user guesses the secret word or the user runs out
of guesses.
5. If you guess the special character % the computer will provide you with one of the missing letters in the secret word at a cost of 2 guesses. If you don’t have two guesses still remaining, the computer will warn you of this and let you try again.
