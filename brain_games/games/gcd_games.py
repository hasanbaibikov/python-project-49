import prompt
from random import randint
import math


BEGIN = 1
END = 100


def gcd_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        divisor1 = randint(BEGIN, END)
        divisor2 = randint(BEGIN, END)
        print(f'Question: {divisor1} {divisor2}')
        crt = math.gcd(divisor1, divisor2)
        answer = prompt.string('Your answer: ')
        if crt != int(answer):
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{crt}".')
            print(f'''Let's try again, {name}!''')
            break
        else:
            print('Correct!')
            count += 1
    if count == 3:
        print(f'Congratulations, {name}!')
