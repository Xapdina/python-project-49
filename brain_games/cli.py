#!/usr/bin/env python3

import prompt


def get_user_name():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!')
