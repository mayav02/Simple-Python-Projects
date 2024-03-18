import random

#Defines funcion
def play():
    options = ('R','P','S')
    ##Asks for user input
    user = input("Rock, Paper, or Scissors? Enter 'R' for rock, 'P' for paper, and 'S' for scissors: ")
    ##Computer guesses 
    comp = random.choice(options)

    if (user == 'R' and comp == 'S')\
        or (user == 'P' and comp == 'R')\
        or (user == 'S' and comp == 'P'):

        print (f"Yaaaas! You won! The computer chose {comp}.")

play()