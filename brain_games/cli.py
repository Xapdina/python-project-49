#!/usr/bin/env python3

import prompt


def get_user_name():
    player_name = prompt.string('Welcome to the Brain Games!\n'
                                'May I have your name? ')
    print(f'Hello, {player_name}!')


def launch_game():
    get_user_name()
