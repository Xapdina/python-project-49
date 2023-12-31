#!/usr/bin/env python3

from math import gcd
from brain_games.randomizer import generator_random_num
from brain_games.engine import is_engine_games
from brain_games.const import TASK


def is_math_action():
    first_random_num, second_random_num = (generator_random_num(),
                                           generator_random_num())
    correct_answer = gcd(first_random_num, second_random_num)
    question = f'{first_random_num} {second_random_num}'
    return question, str(correct_answer)


def is_run_gcd():
    is_engine_games(is_math_action, TASK['gcd'])
