import prompt
from random import randint
from brain_games.game_logic import check_even_number
from time import sleep


def start_even_odd_game(user_name):
    num_of_questions = 3
    while num_of_questions:
        number = randint(0, 999999)
        answer = prompt.string(f'Question: {number}  ').lower()
        print(f'Your answer: {answer} ')
        is_correct, message = check_even_number(number, answer)
        if not is_correct:
            print(message)
            print(f"Let's try again, {user_name}")
            break
        else:
            print('correct!')
            num_of_questions -= 1
            sleep(0.5)

    if not num_of_questions:
        print(f'Congratulations, {user_name}!')
