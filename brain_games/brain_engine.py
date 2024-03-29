import prompt


MAX_TRIES = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_MESSAGE)
    tries_left = MAX_TRIES
    while tries_left:
        question, crt = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != crt:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{crt}".')
            print(f'''Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            tries_left -= 1
    print(f'Congratulations, {name}!')
