#!/usr/bin/env python3
import random
from brain_games.utils import get_rand_num
from brain_games.engine import get_question_and_answer
from brain_games.const import GAME_INSTRUCTIONS, PROGRESSION_LENGTH


def get_pg_and_missed_num():
    start, step = get_rand_num(), get_rand_num()
    nums_list = []
    for i in range(start, PROGRESSION_LENGTH, step):
        if len(nums_list) != 10:
            nums_list.append(i)

    missed_num = random.choice(nums_list)
    nums_list[nums_list.index(missed_num)] = '..'
    pg = " ".join(map(str, nums_list))
    return pg, str(missed_num)


def launch_pg():
    get_question_and_answer(get_pg_and_missed_num, GAME_INSTRUCTIONS['pg'])
