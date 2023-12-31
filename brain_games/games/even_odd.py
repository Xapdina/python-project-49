#!/usr/bin/env python3

from brain_games.randomizer import generator_random_num
from brain_games.engine import is_engine_games
from brain_games.const import TASK


def is_math_action():
    random_num = generator_random_num()
    correct_answer = 'yes' if random_num % 2 == 0 else 'no'
    question = random_num
    return question, str(correct_answer)


def is_run_even_odd():
    is_engine_games(is_math_action, TASK['even_odd'])
