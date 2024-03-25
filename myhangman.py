import random
from words import words
import string

def choose_word(words):
    chosen_word = random.choice(words)
    ##print(chosen_word, '\n')
    while '-' in chosen_word or ' ' in chosen_word:
        print("while loop called, new word coming")
        chosen_word = random.choice(words)
        ##print(chosen_word)
    return chosen_word.upper()

def play():
    print('Hey Bestie!')
    print('Lets Play Hangman! \n')
    chosen_word = choose_word(words)
    final_chosen_word = sorted(chosen_word)
    chosen_word_letters = []
    string.ascii_uppercase
    uppercase_alphabet = set(string.ascii_uppercase)

    attempts = 0
    max_attempts = 26

    while True:
        attempts += 1
        
        new_used_list = [user if user in chosen_word_letters else '-' for user in chosen_word]
        final_new_used = sorted(new_used_list)
        final_chosen_word_letters = sorted(chosen_word_letters)

        ##print("sorted final_new_used: " , final_new_used)
        ##print("sorted final_chosen_word_letters: ", final_chosen_word_letters)

        print(f'You have used these letters:', (' '.join(chosen_word_letters)), '\n')
        print("Current word:", (' '.join(new_used_list)))

        player = input('Guess a letter: ')
        print('\n')
        uppercase_player = player.upper()

        if uppercase_player not in uppercase_alphabet:
            print('That is not a valid letter.' , '\n')
        elif uppercase_player not in chosen_word:
            print(f'Your letter, {uppercase_player}, is not in the word.','\n' )
            chosen_word_letters.append(uppercase_player)
        elif uppercase_player in chosen_word_letters:
            print("You have already guessed that letter")
            print("Try again.", '\n')
            chosen_word_letters.append(uppercase_player)
        else:
            print('Yes! That is right!', '\n')
            chosen_word_letters.append(uppercase_player)

        if final_new_used == final_chosen_word:
            print(f"Congratulations! You guessed {chosen_word} correctly!")
            print("Play Again!")
            break
  
        if attempts == max_attempts:
            print("Sorry, you have no more lives left.")
            print(f"The word was {chosen_word}")
            print("Play Again!")
            break


play()

