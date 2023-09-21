#!/usr/bin/env python3

import random

TASK = 'What number is missing in the progression?'


def question_and_answer():
    start_progression = random.randint(0, 9)
    stop_progression = 100
    step_progression = random.randint(2, 9)

    lst = []
    for i in range(start_progression, stop_progression, step_progression):
        if len(lst) != 10:
            lst.append(i)

    secret_index = '..'
    correct_answer = random.choice(lst)
    index_correct_answer = lst.index(correct_answer)
    lst[index_correct_answer] = secret_index
    question = " ".join(map(str, lst))
    return question, str(correct_answer)
