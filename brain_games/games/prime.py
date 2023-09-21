#!/usr/bin/env python3

from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(random_num):
    for i in range(2, (random_num // 2 + 1)):
        if random_num % i == 0 or random_num <= 1:
            correct_answer = 'no'
            return correct_answer
    else:
        correct_answer = 'yes'
        return correct_answer


def question_and_answer():
    random_num = randint(0, 20)
    correct_answer = prime(random_num)
    question = f'{random_num}'
    return question, str(correct_answer)
