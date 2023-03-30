#!/usr/bin/python3


import prompt


TRIES = 3


def run(game):
    global TRIES
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_MESSAGE)
    while TRIES:
        question, crt = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != crt:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{crt}".')
            print(f'''Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            TRIES -= 1
    print(f'Congratulations, {name}!')
