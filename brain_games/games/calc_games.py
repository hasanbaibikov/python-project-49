from random import randint, choice


GAME_MESSAGE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = ['+', '-', '*']


def calculate(num1, num2, operator):
    if operator == '+':
        crt = num1 + num2
        return  crt
    elif operator == '-':
        crt = num1 - num2
        return crt
    else:
        crt = num1 * num2
        return crt


def get_game():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(OPERATORS)
    question = f'Question: {num1} {operator} {num2}'
    crt = calculate(num1, num2, operator)
    return question, str(crt)
