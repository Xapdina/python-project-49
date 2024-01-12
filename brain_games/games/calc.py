import random
from brain_games.engine import run_game
from brain_games.const import GAME_INSTRUCTIONS, OPERATORS
from brain_games.utils import get_rand_num


def get_math_expression_and_res():
    num1, num2 = get_rand_num(), get_rand_num()
    get_operator = random.choice(OPERATORS)
    expression = f'{num1} {get_operator} {num2}'
    calculation = eval(expression)
    return expression, str(calculation)


def run_calc_game():
    run_game(get_math_expression_and_res, GAME_INSTRUCTIONS['calc'])
