#!/usr/bin/env python3

from random import randint
from math import gcd

TASK = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    first_random_num = randint(1, 10)
    second_random_num = randint(1, 10)
    correct_answer = gcd(first_random_num, second_random_num)
    question = f'{first_random_num} {second_random_num}'
    return question, str(correct_answer)
