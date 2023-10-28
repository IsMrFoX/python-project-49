import math


def check_even_number(number, answer):
    if number % 2 and answer == 'yes':
        return False, f"'{answer}' is wrong answer ;(. Correct answer was 'no'."
    elif number % 2 == 0 and answer == 'no':
        return False, f"'{answer}' is wrong answer \
;(. Correct answer was 'yes'."
    else:
        return True, 'correct!'


def check_expression(f_num, s_num, oper, answer):
    expression = str(eval(f'{f_num} {oper} {s_num}'))
    if answer != expression:
        return False, f"'{answer}' is wrong answer \
;(. Correct answer was '{expression}'."
    else:
        return True, 'Correct!'


def check_gcd_number(num1, num2, answer):
    gcd_result = math.gcd(num1, num2)
    if gcd_result == int(answer):
        return True, 'correct!'
    return False, f"'{answer}' is wrong answer \
;(. Correct answer was '{gcd_result}'."
