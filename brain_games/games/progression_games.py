from random import randint


GAME_MESSAGE = 'What number is missing in the progression?'
LEN = 10


def create_prog():
    prog = []
    start = randint(1, 100)
    step = randint(1, 5)
    for i in range(0, LEN):
        prog.append(str(start + i * step))
    return prog


def get_game():
    progression = create_prog()
    rand_index = randint(0, LEN - 1)
    crt = progression[rand_index]
    progression[rand_index] = '..'
    str_progression = ' '.join(progression)
    question = f'Question: {str_progression}'
    return question, crt
