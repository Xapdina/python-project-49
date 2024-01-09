#!/usr/bin/env python3

from brain_games.utils import get_rand_num
from brain_games.engine import get_question_and_answer
from brain_games.const import GAME_INSTRUCTIONS


def is_prime(num):
    if num <= 1:
        return 'no'
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            return 'no'
    else:
        return 'yes'


def get_num_and_prime():
    num = get_rand_num()
    prime = is_prime(num)
    return num, str(prime)


def launch_prime():
    get_question_and_answer(get_num_and_prime, GAME_INSTRUCTIONS['prime'])
