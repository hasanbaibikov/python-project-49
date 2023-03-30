from random import randint, choice
import operator


GAME_MESSAGE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul}


def calc_expression(random_operator):
    return OPERATORS.get(random_operator)


def get_game():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    random_operator = choice(list(OPERATORS.keys()))
    question = f'Question: {num1} {random_operator} {num2}'
    operator_func = calc_expression(random_operator)
    crt = operator_func(num1, num2)
    return question, str(crt)
