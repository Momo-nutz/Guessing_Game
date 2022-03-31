#A quick little game where the user tries to guess the location of the "O" character in a list sized of 3.
import random

def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist

def player_guess():
    guess = ' '
    while guess not in ['0','1','2']:
        
        guess = input("Pick a number: 0,1, or 2")
        
    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

mylist = [' ', 'O', ' ']
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list,guess)