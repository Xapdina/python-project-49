#!/usr/bin/env python3

from random import choice
from brain_games.randomizer import generator_random_num
from brain_games.engine import is_engine_games
from brain_games.const import TASK


def is_math_action():
    start_progression = generator_random_num()
    stop_progression = 100
    step_progression = generator_random_num()

    lst = []
    for i in range(start_progression, stop_progression, step_progression):
        if len(lst) != 10:
            lst.append(i)

    secret_index = '..'
    correct_answer = choice(lst)
    index_correct_answer = lst.index(correct_answer)
    lst[index_correct_answer] = secret_index
    question = " ".join(map(str, lst))
    return question, str(correct_answer)


def is_run_progression():
    is_engine_games(is_math_action, TASK['progression'])
