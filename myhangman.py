import random
from words import words
from hangman_visual import lives_visual_dict
import string

def choose_word(words):
    chosen_word = random.choice(words)
    print(chosen_word, '\n')
    while '-' in chosen_word or ' ' in chosen_word:
        print("while loop called, new word coming")
        chosen_word = random.choice(words)
        ##print(chosen_word)
    return chosen_word.upper()

def play():
    print('Hey Bestie!')
    print('Lets Play Hangman! \n')
    chosen_word = choose_word(words)
    chosen_word_letters = set()
    string.ascii_uppercase
    uppercase_alphabet = list(string.ascii_uppercase)
    dashes = len(chosen_word) * ' - '
    split_set = set(chosen_word)
    ##print('this is the split set:', split_set)

    for i in range(1, 27) or (chosen_word_letters == split_set): 
        ##^which equals 26, length of alphabet
        ##print('chosen word letters: ',chosen_word_letters)
        ##print('this is the split set:',split_set)
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
  
        if len(chosen_word_letters) == 26:
            print("Sorry, you have no more lives left.")
            print(f"The word was {chosen_word}")
            print("Play Again!")

        if new_used_list == split_set:
            print("Chosen word letters: ", chosen_word_letters)
            print(f"Congratulations! You guessed {chosen_word} correctly!")
            print("Play Again!")
            break


play()





"""import random
from words import words
from hangman_visual import lives_visual_dict
import string

def choose_word(words):
    chosen_word = random.choice(words)
    print(chosen_word, '\n')
    while '-' in chosen_word or ' ' in chosen_word:
        print("while loop called, new word coming")
        chosen_word = random.choice(words)
        ##print(chosen_word)
    return chosen_word.upper()

def play():
    print('Hey Bestie!')
    print('Lets Play Hangman! \n')
    chosen_word = choose_word(words)
    chosen_word_letters = []
    ##chosen_word_letters.sort(chosen_word)
    string.ascii_uppercase
    uppercase_alphabet = set(string.ascii_uppercase)
    dashes = len(chosen_word) * ' - '
    new_used_list = []
    ##split_set = set(chosen_word)
    ##print('this is the split set:', split_set)

    for i in range(1, 27) or (chosen_word_letters == new_used_list): 
        ##^which equals 26, length of alphabet
        new_used_list = [user if user in chosen_word_letters else '-' for user in chosen_word]
        print('chosen word letters: ',chosen_word_letters)
        print('this is new used list: ', new_used_list)
        print(f'You have used these letters:', (' '.join(chosen_word_letters)), '\n')
        print("Current word:", (' '.join(new_used_list)))
        player = input('Guess a letter: ')
        uppercase_player = player.upper()
        if uppercase_player not in uppercase_alphabet:
            print('That is not a valid letter.' , '\n')
        elif uppercase_player not in chosen_word:
            print(f'Your letter, {uppercase_player}, is not in the word.','\n' )
            chosen_word_letters.append(uppercase_player)
        else:
            print('Yes! That is right!', '\n')
            chosen_word_letters.append(uppercase_player)
  
        if len(chosen_word_letters) == 26:
            print("Sorry, you have no more lives left.")
            print(f"The word was {chosen_word}")
            print("Play Again!")

        if new_used_list == chosen_word_letters:
            print("Chosen word letters: ", chosen_word_letters)
            print(f"Congratulations! You guessed {chosen_word} correctly!")
            print("Play Again!")
            break


play()
***
