import random
import prompt
from brain_games.game_logic import check_gcd_number
from time import sleep


def start_gcd_game(user_name):
    num_of_questions = 3
    print('Find the greatest common divisor of given numbers.')
    while num_of_questions:
        num1, num2 = random.randint(0, 100), random.randint(0, 100)
        answer = prompt.string(f'Question: {num1} {num2}  ')
        print(f'Your answer: {answer}')
        is_correct, message = check_gcd_number(num1, num2, answer)
        if not is_correct:
            print(message)
            print(f"Let's try again, {user_name}!")
        else:
            print(message)
            num_of_questions -= 1
            sleep(0.5)
    if not num_of_questions:
        print(f'Congratulations, {user_name}!')
