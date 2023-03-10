import sympy
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
        correct_num = sympy.isprime(num)
        correct_answer = dict[correct_num]
        answer = prompt.string('Your answer: ')
        if correct_answer != answer:
          print(f'''"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".\n Let's try again, {name}!''')
          break
        else:
          print('Correct!')
          count += 1

    if count == 3:
      print(f'Coungratilations, {name}!')
