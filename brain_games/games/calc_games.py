import prompt
from random import randint, choice


BEGIN = 1
END = 10


def calc_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        operand1 = randint(BEGIN, END)
        operand2 = randint(BEGIN, END)
        operators = ['+', '-', '*']
        random_operators = choice(operators)
        calc = f'{operand1} {random_operators} {operand2}'
        some_dict = {
        '-': operand1 - operand2,
        '+': operand1 + operand2,
        '*': operand1 * operand2,
   }
        print(f'Question: {calc}')
        answer = prompt.string('Your answer: ')
        coorect = some_dict[random_operators]
        if coorect != int(answer):
          print(f'''"{answer}" is wrong answer ;(. Correct answer was "{coorect}".\n Let's try again, {name}!''')
          break
        else:
          print('Coorect!')
          count += 1
    if count == 3:
      print(f'Congratulations, {name}!')
