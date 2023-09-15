#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint


def main():
    name = welcome_user()
    i = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while i < 3:
        i = i + 1
        random_num = randint(1, 100)
        print(f'Question: {random_num}')
        answer = str(input('Your answer: '))
        if (random_num % 2) == 0 and answer == 'yes':
            print('Correct!')
        elif (random_num % 2) != 0 and answer == 'no':
            print('Correct!')
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\
            \nLet's try again, {name} !")
            break
        if i == 3:
            print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
