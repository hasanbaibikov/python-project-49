#!/usr/bin/python3


import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_MESSAGE)
    count = 0
    while count < 3:
        question, crt = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != crt:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{crt}".'
                  f'''Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')
