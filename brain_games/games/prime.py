#!/usr/bin/env python3

from brain_games.randomizer import generator_random_num
from brain_games.engine import is_engine_games
from brain_games.const import TASK


def prime(random_num):
    if random_num <= 1:
        return 'no'
    for i in range(2, (random_num // 2 + 1)):
        if random_num % i == 0:
            return 'no'
    else:
        return 'yes'


def is_math_action():
    random_num = generator_random_num()
    correct_answer = prime(random_num)
    question = f'{random_num}'
    return question, str(correct_answer)


def is_run_prime():
    is_engine_games(is_math_action, TASK['prime'])
