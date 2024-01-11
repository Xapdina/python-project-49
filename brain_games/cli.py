#!/usr/bin/env python3

import prompt


def welcome_user():
    player_name = prompt.string('Welcome to the Brain Games!\n'
                                'May I have your name? ')
    print(f'Hello, {player_name}!')


def get_user_name():
    welcome_user()
