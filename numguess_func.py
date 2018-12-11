import random


# This file is to practice git contribution(fork and pull request) with numguess with function.
# trial: 5
# hint: Low, High
# Provide restart feature by press y or Y if user wants to restart this game.
# When the one game is finished, ask to want to do more game.
def numguess():
    # TODO: do_more() to restart numguess logic
    # TODO: answer_match() with iteration
    answer = set_answer()
    user = user_choice()
    return print("It works!") # to check this file works.

def set_answer():
    # TODO: set answer with random.randint() (range: 1 to 100)
    # return integer

    return random.randint(1,101)


def user_choice():
    # TODO: get integer from user with input()
    # return integer
    pass

def answer_match():
    # TODO: find out user is equal to answer.
    # return True or False
    pass

def do_more():
    # TODO: want some more game?
    # return True or False
    pass

numguess()
