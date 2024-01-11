import random
from brain_games.engine import run_game
from brain_games.const import QUESTIONS, OPERATOR
from brain_games.utils import get_rand_num


def get_math_expression_and_res():
    num1, num2 = get_rand_num(), get_rand_num()
    get_operator = random.choice(OPERATOR)
    expression = f'{num1} {get_operator} {num2}'
    calculation = eval(expression)
    return expression, str(calculation)


def run_calc():
    run_game(get_math_expression_and_res, QUESTIONS['calc'])
