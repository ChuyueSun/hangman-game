# Problem Set 2, hangman.py
# Name: Chuyue Sun
# Collaborators: No
# Time spent: 3hr

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if (i not in letters_guessed):
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes the letters in
      secret_word are all lowercase.
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters and asterisks (*) that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result=""
    for i in secret_word:
        if i not in letters_guessed:
            result+="*"
        else:
            result+=i
    return result



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which 
      letters have not yet been guessed. The letters should be returned in
      alphabetical order.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    result=""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            result+=i
    return result
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.
      
    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining=10
    letters_guessed=[]
    print("Welcome to Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    print("------------------")
    while guesses_remaining>0:
        
        if guesses_remaining>1:
            print("You have",guesses_remaining,"guesses left.")
        else:
            print("You have",guesses_remaining,"guess left.")
        print("Available letters:",get_available_letters(letters_guessed))
        letter=input("Please guess a letter: ")
        if letter=="%" and guessed_remaining>=2:
            guesses_remaining-=2
            hangman_with_help(secret_word)
        elif letter=="%" and guessed_remaining<2:
            print("Oops! Not enough guessed left:",get_available_letters(letters_guessed))
        if str.isalpha(letter)==False:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:",get_guessed_word(secret_word,letters_guessed))
        elif str.lower(letter) in letters_guessed:
            print("Oops! You've already guessed that letter:",get_guessed_word(secret_word,letters_guessed))
        else:
            letter=str.lower(letter)
            letters_guessed.append(letter)

            if letter in secret_word:
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
            else:
                if letter in ["a","e","i","o","u"]:
                    guesses_remaining-=2
                else:
                    guesses_remaining-=1

                print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
        print("------------------")
        if is_word_guessed(secret_word,letters_guessed):
                
            def get_unique (secret_word):
                unique=0
                for i in string.ascii_lowercase:
                    if i in secret_word:
                        unique+=1
                return unique

            score=guesses_remaining+2*get_unique(secret_word)*len(secret_word)
            print("Congratulations, you won!")
            print("Your total score for this game is:",score)
            break
        
        if guesses_remaining==0:
            print("Sorry, you ran out of guesses. The word was",secret_word,".")
        
    
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def choose(secret_word,available_letters):
    result=""
    for i in string.ascii_lowercase:
        if i in secret_word and i in available_letters :
            result+=i
    return result
            


def hangman_with_help(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.
      
    * The user should start with 10 guesses.
    
    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make sure that
      the user puts in a letter.
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol %, you should reveal to the user one of the 
      letters missing from the word at the cost of 2 guesses. If the user does 
      not have 2 guesses remaining, print a warning message. Otherwise, add 
      this letter to their guessed word and continue playing normally.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    
    guesses_remaining=10
    letters_guessed=[]
    print("Welcome to Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    print("------------------")
    while guesses_remaining>0:
        
        if guesses_remaining>1:
            print("You have",guesses_remaining,"guesses left.")
        else:
            print("You have",guesses_remaining,"guess left.")
        print("Available letters:",get_available_letters(letters_guessed))
        letter=input("Please guess a letter: ")
        if letter=="%" and guesses_remaining>=2:
            guesses_remaining-=2
            available_letters=get_available_letters(letters_guessed)
            choose_from=choose(secret_word,available_letters)
            new=random.randint(0,len(choose_from)-1)
            exposed_letter=choose_from[new]
            print("Letter revealed:",exposed_letter)
            letters_guessed.append(exposed_letter)
            print(get_guessed_word(secret_word,letters_guessed))
        elif letter=="%" and guesses_remaining<2:
            print("Oops! Not enough guessed left:",get_available_letters(letters_guessed))
        elif str.isalpha(letter)==False:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:",get_guessed_word(secret_word,letters_guessed))
        elif str.lower(letter) in letters_guessed:
            print("Oops! You've already guessed that letter:",get_guessed_word(secret_word,letters_guessed))
        else:
            letter=str.lower(letter)
            letters_guessed.append(letter)

            if letter in secret_word:
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
            else:
                if letter in ["a","e","i","o","u"]:
                    guesses_remaining-=2
                else:
                    guesses_remaining-=1

                print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
        print("------------------")
        if is_word_guessed(secret_word,letters_guessed):
                
            def get_unique (secret_word):
                unique=0
                for i in string.ascii_lowercase:
                    if i in secret_word:
                        unique+=1
                return unique

            score=guesses_remaining+2*get_unique(secret_word)*len(secret_word)
            print("Congratulations, you won!")
            print("Your total score for this game is:",score)
            break
        
        if guesses_remaining==0:
            print("Sorry, you ran out of guesses. The word was",secret_word,".")
        
    
# When you've completed your hangman_with_help function, comment the two similar
# lines below that were used to run the hangman function, and then uncomment
# those two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
#    
#    secret_word = choose_word(wordlist)
#    hangman_with_help(secret_word)
