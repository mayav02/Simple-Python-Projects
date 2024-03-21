import random
from words import words
from hangman_visual import lives_visual_dict
import string

##Takes a list of words as a parameter
    ##Selects a random word from the list
    #Continue choosing words until
    ## a valid word without a dash or space is obtained
    ##Returns the word in all uppercase
def choose_word(words):
    chosen_word = random.choice(words)
    print(chosen_word)
    while '-' in chosen_word or ' ' in chosen_word:
        print("while loop called, new word coming")
        chosen_word = random.choice(words)
        print(chosen_word)
    return chosen_word.upper()

##Calls the above function to obtain a valid word. YES
    ##Initializes sets for the letters in the word, the alphabet and used letters. Y
    ##Sets the initial number of lives to 7. Y
    ##While loop that continues as long as there are letters to guess. Y
    ##And the lives remaining. Y
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

def play():
    print("Let's Play Hangman!")
    chosen_word = choose_word(words)
    chosen_word_letters = set()
    string.ascii_uppercase
    uppercase_alphabet = list(string.ascii_uppercase)
    dashes = len(chosen_word) * '-'
    lives = 7
    while len(chosen_word) or lives >= 7:
        print("Current word:", dashes)
        new_used_list = [user if user in chosen_word_letters else '-' for user in chosen_word]
        print(f'You have {lives} lives left and you have used these letters:', new_used_list)
        player = input("Guess a letter: ")
        uppercase_player = player.upper()
        print(uppercase_player)
        if uppercase_player not in uppercase_alphabet:
            print("That is not a valid letter.")
        elif uppercase_player not in chosen_word:
            print("Your letter", uppercase_player, "is not in the word")
        else:
            chosen_word_letters.add(uppercase_player)
        print(chosen_word_letters)
        lives -= 1


play()
