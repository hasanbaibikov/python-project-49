#!/usr/bin/python3


import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_MESSAGE)
    tries = 3
    while tries:
        question, crt = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != crt:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{crt}".'
                  f'''Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            tries -= 1
    print(f'Congratulations, {name}!')
