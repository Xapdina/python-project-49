#!/usr/bin/env python3

from brain_games.utils import get_rand_num
from brain_games.engine import get_question_and_answer
from brain_games.const import GAME_INSTRUCTIONS


def get_num_and_even_odd():
    num = get_rand_num()
    even_odd = 'yes' if num % 2 == 0 else 'no'
    return num, str(even_odd)


def launch_even_odd():
    get_question_and_answer(get_num_and_even_odd, GAME_INSTRUCTIONS['even_odd'])
