import prompt
from random import randint
from time import sleep
from brain_games.game_logic import check_progression_number


def start_progression_game(user_name):
    num_of_questions = 3
    count_numbers = 10
    print('What number is missing in the progression?')
    while num_of_questions:
        start = randint(0, 20)
        stop = randint(120, 120)
        step = randint(1, 9)
        sequence = list(range(start, stop, step)[:count_numbers])
        value = sequence[randint(0, 9)]
        sequence[sequence.index(value)] = '..'
        answer = int(prompt.string(f'Question: \
{" ".join(map(str, sequence))}  '))

        is_correct, message = check_progression_number(value, answer)
        if not is_correct:
            print(message)
            print(f"Let's try again, {user_name}!")
        else:
            print(message)
            num_of_questions -= 1
            sleep(0.5)
    if not num_of_questions:
        print(f'Congratulations, {user_name}!')
