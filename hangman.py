import random
from words import words
from hangman_visual import lives_visual_dict
import string

##Takes a list of words as a parameter
def get_valid_word(words):
    ##Selects a random word from the list
    word = random.choice(words)
    #Continue choosing words until
    ## a valid word without a dash or space is obtained
    while '-' in word or ' ' in word:
        word = random.choice(words)
    ##Returns the word in all uppercase
    return word.upper()

def hangman():
    ##Calls the above function to obtain a valid word
    word = get_valid_word(words)
    ##Initializes sets for the letters in the word, the alphabet and used letters.
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    ##Sets the initial number of lives to 7.
    lives = 7

    ##While loop that continues as long as there are letters to guess.
    ##And the lives remaining.
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        ##Words list where the guessed letters are displayed
        ##and unguessed letters are represented as '-'.
        word_list = [letter if letter in used_letters else '-' for letter in word]
        ##Prints the hangman visual graphic and the current state of the word
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        ##Asks the user to enter a letter
        user_letter = input('Guess a letter: ').upper()
        ##Checks if the letter is already used.
        if user_letter in alphabet - used_letters:
            ##Adds the guessed letter to the set of used letters.
            used_letters.add(user_letter)
            ##Checks if the guessed letter is in the word.
            if user_letter in word_letters:
                ##Removes the letter from the set of word letters.
                word_letters.remove(user_letter)
                print('')
            ##If not, it decrements the number of lives
            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')

        ##Checks for invalid input
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    ##Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()