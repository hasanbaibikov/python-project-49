from random import randint


GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True


def get_game():
    num = randint(1, 100)
    question = f'Question: {num}'
    if is_even(num):
        crt = 'yes'
    else:
        crt = 'no'
    return question, crt
