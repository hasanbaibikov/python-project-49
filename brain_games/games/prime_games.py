#!/usr/bin/env python3


from random import randint


GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def get_game():
    num = randint(1, 100)
    question = f'Question: {num}'
    crt = is_prime(num)
    if crt == False:
        crt = 'no'
    else:
        crt = 'yes'
    return question, str(crt)
