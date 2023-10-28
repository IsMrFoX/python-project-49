import prompt
from random import randint
from time import sleep


def start_game_even_odd(user_name):
    count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count:
        number = randint(0, 999999)
        answer = prompt.string(f'Question: {number}  ').lower()
        print(f'Your answer: {answer} ')
        if number % 2 and answer == 'yes':
            print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {user_name}")
            break
        elif number % 2 == 0 and answer == 'no':
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {user_name}")
            break
        else:
            print('correct!')
            count -= 1
            sleep(1)

    if not count:
        print(f'Congratulations, {user_name}!')
