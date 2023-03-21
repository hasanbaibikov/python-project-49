from random import randint
import math


GAME_MESSAGE = 'Find the greatest common divisor of given numbers.'


def get_game():
    divisior1 = randint(1, 100)
    divisior2 = randint(1, 100)
    question = f'Question: {divisior1} {divisior2}'
    crt = math.gcd(divisior1, divisior2)
    return question, str(crt)
