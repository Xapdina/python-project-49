#!/usr/bin/env python3

from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():
    random_num = randint(1, 10)
    if random_num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_num}'
    return question, str(correct_answer)
