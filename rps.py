
from os import urandom
import random


greeting = 'Please choose your selection'.title()
print('')
print(greeting.center(50, '='))
print('')

value = print('you have 3 options. 1 - Paper, 2 - Scissor, 3 -  Rock \n')
val = int((input()))

opt = {1: 'Paper', 2: 'Scissor', 3: 'Rock'}

random = random.choice(list(opt.values()))
print('Computer Choose ' + random)

no_winner = 'no winner'.upper()
lost = 'you lost'.upper()
win = 'you win'.upper()


def ask(val):
    if val:
        print('Please make a new selection between 1-3 or for stop press 0 \n')
        val = int((input()))


for x in opt.values():
    if val == 1:
        print('You have choose Paper')
        if random == 'Scissor':
            print(win.center(50, '*'))
            ask(val)
        elif random == 'Rock':
            print(lost.center(50, '*'))
            ask(val)
        else:
            print(no_winner.center(50, '*'))
            ask(val)

    elif val == 2:
        print('You have choose Scissor')
        if random == 'Paper':
            print(win.center(50, '*'))
            ask(val)
        elif random == 'Rock':
            print(lost.center(50, '*'))
            ask(val)
        else:
            print(no_winner.center(50, '*'))
            ask(val)

    elif val == 3:
        print('You have choose Rock')
        if random == 'Paper':
            print(lost.center(50, '*'))
            ask(val)
        elif random == 'Scissor':
            print(win.center(50, '*'))
            ask(val)
        else:
            print(no_winner.center(50, '*'))
            ask(val)

    else:
        ask(val)