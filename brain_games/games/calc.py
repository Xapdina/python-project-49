#!/usr/bin/env python3

import random
from brain_games.engine import get_question_and_answer
from brain_games.const import GAME_INSTRUCTIONS
from brain_games.utils import get_rand_num


def get_nums_and_calc():
    num1, num2 = (get_rand_num(), get_rand_num())
    get_operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {get_operator} {num2}'
    calculation = eval(expression)
    return expression, str(calculation)


def launch_calculater():
    get_question_and_answer(get_nums_and_calc, GAME_INSTRUCTIONS['calc'])
