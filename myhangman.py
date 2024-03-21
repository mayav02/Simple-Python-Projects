import random
from words import words
from hangman_visual import lives_visual_dict
import string

print("hey bestie!")

def choose_word(words):
    chosen_word = random.choice(words)
    print(chosen_word, '\n')
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
        ##Words list where the guessed letters are displayed. Y
        ##and unguessed letters are represented as '-'. Y
        ##Prints the hangman visual graphic and the current state of the word. 
        ##Asks the user to enter a letter. Y
        ##Checks if the letter is already used. Y
            ##Adds the guessed letter to the set of used letters. y
            ##Checks if the guessed letter is in the word. y
                ##Removes the letter from the set of word letters. 
            ##If not, it decrements the number of lives. Y
        ##Checks for invalid input. Y 
    ##Gets here when len(word_letters) == 0 OR when lives == 0
        ##Prints the hangman graphic and the word if lives run out
        ##Otherwise, congratulates the user for guessing the word.

def play():
    print('Lets Play Hangman! \n')
    chosen_word = choose_word(words)
    chosen_word_letters = set()
    string.ascii_uppercase
    uppercase_alphabet = list(string.ascii_uppercase)
    dashes = len(chosen_word) * ' - '
    ##lives = 7
    ##for len(chosen_word) in chosen_word: ##and lives <= 7:
        print(len(chosen_word))
        ##print(lives)
        new_used_list = [user if user in chosen_word_letters else '-' for user in chosen_word]
        print(f'You have used these letters:', (' '.join(chosen_word_letters)), '\n')
        print("Current word:", (' '.join(new_used_list)))
        player = input('Guess a letter: ')
        uppercase_player = player.upper()
        if uppercase_player not in uppercase_alphabet:
            print('That is not a valid letter.' , '\n')
        elif uppercase_player not in chosen_word:
            print(f'Your letter, {uppercase_player}, is not in the word.','\n' )
            chosen_word_letters.add(uppercase_player)
        else:
            print('Yes! That is right!', '\n')
            chosen_word_letters.add(uppercase_player)
        """
            lives -= 1
        if lives == 0 :
            print('Sorry, you have no lives left.')
            print(f'The word was {chosen_word}.')
            print('Play Again!')
            break
        """
        if chosen_word_letters == chosen_word: ##and lives == len(chosen_word):
            print(f"Congratulations! You guessed {chosen_word} correctly!")
            print("Play Again!")
            break
play()
