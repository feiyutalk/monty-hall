# -*- coding:utf-8 -*-  
__author__ = 'neuclil'
import random
import sys

win = 0
for i in range(int(sys.argv[1])):
    prize = random.randint(1, 3)
    choice = 1
    # case 1   prize == choice
    # In this case, host can random choice a door to open, suppose door 2
    # We switch the choice, and don't get the prize
    if prize == choice:
        open = 2
        choice = 3
    # case 2 prize == 2, then the host should open door 3
    elif prize == 2:
        open = 3
        choice = 3
        win += 1
    # case 3 prize == 3, then the host should open door 2
    else :
        open = 2
        choice = 3
        win += 1

print('Test for monty hall, trials {} times, if switch door, win {} times, {}% of {} trials.'.format(sys.argv[1], win, 100*win/int(sys.argv[1]), sys.argv[1]))


