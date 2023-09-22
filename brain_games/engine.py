#!/usr/bin/env python3

from prompt import string

MAX_ROUND = 3


def engine_games(games):
    print('Welcome to the Brain Games')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(games.TASK)

    count_round = 0

    while count_round < MAX_ROUND:
        question, correct_answer = games.question_and_answer()
        print(f'Question: {question}')
        player_answer = string('Your answer: ')
        print('Correct!')
        count_round += 1
        if correct_answer != player_answer:
            print(f"'{player_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
