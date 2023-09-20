#!/usr/bin/env python3

from random import randint
from math

TASK = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    random_num = randint(1, 10)
    if random_num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_num}'
    return question, str(correct_answer)

question_and_answer()