from random import randint, choice
import operator


GAME_MESSAGE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = ['+', '-', '*']


def calc_expression(num1, num2, random_operator):
    if random_operator == '+':
        crt = operator.add(num1, num2)
        return crt
    elif random_operator == '-':
        crt = operator.sub(num1, num2)
        return crt
    else:
        crt = operator.mul(num1, num2)
        return crt


def get_game():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    random_operator = choice(OPERATORS)
    question = f'Question: {num1} {random_operator} {num2}'
    crt = calc_expression(num1, num2, random_operator)
    return question, str(crt)
