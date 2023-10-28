import prompt
from random import randint
from brain_games.game_logic import check_even_number
from time import sleep

# 'Answer "yes" if the number is even, otherwise answer "no".'

def start_game(user_name, game_greeting, check_func):
    num_of_questions = 3
    print(game_greeting)
    while num_of_questions:
        number = randint(0, 1000)
        answer = prompt.string(f'Question: {number}  ').lower()
        print(f'Your answer: {answer} ')
        is_correct, message = check_func(number, answer)
        if not is_correct:
            print(message)
            print(f"Let's try again, {user_name}")
            break
        else:
            print(message)
            num_of_questions -= 1
            sleep(0.5)

    if not num_of_questions:
        print(f'Congratulations, {user_name}!')
