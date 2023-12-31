#!/usr/bin/env python3

from random import choice
from operator import add, sub, mul
from brain_games.engine import is_engine_games
from brain_games.const import TASK
from brain_games.randomizer import generator_random_num


def choice_operator():
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*')
    ])
    return operation, operator


def is_math_action():
    first_random_num, second_random_num = (generator_random_num(),
                                           generator_random_num())
    operation, operator = choice_operator()
    correct_answer = operation(first_random_num, second_random_num)
    question = f'{first_random_num} {operator} {second_random_num}'
    return question, str(correct_answer)


def is_run_calculater():
    is_engine_games(is_math_action, TASK['calculater'])
