#!/usr/bin/env python3

import math
from brain_games.utils import get_rand_num
from brain_games.engine import get_question_and_answer
from brain_games.const import GAME_INSTRUCTIONS


def get_nums_pair_and_gcd():
    num1, num2 = (get_rand_num(), get_rand_num())
    gcd = math.gcd(num1, num2)
    nums_pair = f'{num1} {num2}'
    return nums_pair, str(gcd)


def launch_gcd():
    get_question_and_answer(get_nums_pair_and_gcd, GAME_INSTRUCTIONS['gcd'])
