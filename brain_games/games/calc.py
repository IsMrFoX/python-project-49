import prompt
from random import randint, choice
from brain_games.game_logic import check_expression
from time import sleep


def start_calc_game(user_name):
    num_of_questions = 3
    while num_of_questions:
        operators = ['+', '-', '*']
        oper = choice(operators)
        f_num = randint(0, 100)
        s_num = randint(0, 100)
        answer = prompt.string(f'Question: {f_num} {oper} {s_num}  ')
        print(f'Your answer: {answer} ')

        is_correct, message = check_expression(f_num, s_num, oper, answer)
        if not is_correct:
            print(message)
            print(f"Let's try again, {user_name}!")
            break
        else:
            print('Correct!')
            num_of_questions -= 1
            sleep(0.5)

    if not num_of_questions:
        print(f"Congratulations, {user_name}!")
