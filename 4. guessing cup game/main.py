#imports
from random import shuffle

#defining funcs
def shuffle_list(list_to_shuffle):
    shuffle(list_to_shuffle)
    return list_to_shuffle

def player_input():
    guess_input = ''

    while guess_input not in ['0', '1', '2']:
        guess_input = input('Pick a number: 0, 1 or 2: ')
    else:
        return int(guess_input)

def check_guess(cup_list, guess):
    if cup_list[guess] == 'O':
        print('Good job! You guessed it right!')
    else:
        print('Sorry :c')
        print(cup_list)

#START
cup_list = [' ', ' ', 'O']

#shuffling list
shuffled_cup_list = shuffle_list(cup_list)

#getting input from player
player_guess = player_input()

#checking if its correct
check_guess(shuffled_cup_list, player_guess)