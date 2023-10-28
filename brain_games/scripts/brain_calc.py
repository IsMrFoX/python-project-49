import prompt
from random import randint, sample
from time import sleep
from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    operators = sample(['+', '-', '*'], 3)
    print('What is the result of the expression?')
    while operators:
        oper = operators.pop(0)
        f_num = randint(0, 100)
        s_num = randint(0, 100)
        expression = str(eval(f'{f_num} {oper} {s_num}'))
        answer = prompt.string(f'Question: {f_num} {oper} {s_num}  ')
        print(f'Your answer: {answer} ')
        if answer != expression:
            print(f"""'{answer}' is wrong answer \
;(. Correct answer was '{expression}'.""")
            print(f"Let's try again, {user_name}!")
            break
        else:
            print('Correct!')
            sleep(0.5)

    if not operators:
        print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
