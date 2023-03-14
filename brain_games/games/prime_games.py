import prompt
import random


dict = {True: 'yes', False: 'no'}


def prime_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        correct_answer = dict[is_prime(num)]
        answer = prompt.string('Your answer: ')
        if correct_answer != answer:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f'''Let's try again, {name}!''')
            break
        else:
            print('Correct!')
            count += 1
    if count == 3:
        print(f'Congratulations, {name}!')


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
