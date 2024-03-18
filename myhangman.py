import random
from words import words
from hangman_visual import lives_visual_dict
import string

##Comp chooses word from word lis
def choose_word(words):
    for words in words:
        chosen_word = random.choice(words)
        while '-' or ' ' in words:
            chosen_word = random.choice(words)
    return chosen_word.upper()

print("Let's play Hangman!")
def play():
    chosen_word = choose_word(words)
    chosen_word_letters = set(chosen_word)
    current_guesses = set()
    uppercase_alphabet = string.ascii_uppercase
    uppercase_alphabet = set()
    user = input("Guess a letter: ")
    lives = 7
    print("Let's play Hangman!")
          
    while len(chosen_word) or lives >= 7:
        print(f'You have {lives} left and you have used these letters:')
        if ValueError:
            print("That is not a valid letter")
        if user not in chosen_word:
            print("Your letter", user, "is not in the word")
        else:
            user.append(current_guesses)

##chosen_word
if __name__ == '__myhangman__':
    play()


##Takes a list of words as a parameter
    ##Selects a random word from the list
    #Continue choosing words until
    ## a valid word without a dash or space is obtained
    ##Returns the word in all uppercase


    ##Calls the above function to obtain a valid word
    ##Initializes sets for the letters in the word, the alphabet and used letters.
    ##Sets the initial number of lives to 7.
    ##While loop that continues as long as there are letters to guess.
    ##And the lives remaining.
        ##Words list where the guessed letters are displayed
        ##and unguessed letters are represented as '-'.
        ##Prints the hangman visual graphic and the current state of the word
        ##Asks the user to enter a letter
        ##Checks if the letter is already used.
            ##Adds the guessed letter to the set of used letters.
            ##Checks if the guessed letter is in the word.
                ##Removes the letter from the set of word letters.
            ##If not, it decrements the number of lives
        ##Checks for invalid input
    ##Gets here when len(word_letters) == 0 OR when lives == 0
        ##Prints the hangman graphic and the word if lives run out
        ##Otherwise, congratulates the user for guessing the word.
