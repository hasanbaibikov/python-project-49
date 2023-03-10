import prompt
import random


def ar_progression_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What number is missing in the progression?") 
    count = 0
    LEN = 10
    while count < 3:
        start = random.randint(1, 100)
        step = random.randint(1, 5)
        my_list = []
        a = start
        d = step
        for i in range(0, LEN):
            my_list.append(str(a+i*d))
        rand_int = random.randint(0, LEN - 1)
        correct_answer = my_list[rand_int]
        my_list[rand_int] = '..'
        progression = ' '.join(my_list)
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')
        if correct_answer != answer:
          print(f'''"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".\n Let's try again, {name}!''')
          break
        else:
          print('Correct!')
          count += 1
    if count == 3:
      print(f'Congratulations, {name}!')
