#!/usr/bin/env python3

from random import randint, choice
from operator import add, sub, mul

TASK = 'What is the result of the expression?'


def question_and_answer():
    first_random_num = randint(1, 10)
    second_random_num = randint(1, 10)
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*')
    ])
    correct_answer = operation(first_random_num, second_random_num)
    question = f'{first_random_num} {operator} {second_random_num}'
    return question, str(correct_answer)
