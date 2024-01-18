import random
from brain_games.utils import get_rand_num
from brain_games.engine import run_game
from brain_games.const import GAME_INSTRUCTIONS, PROGRESSION_LENGTH


def get_pg_and_missed_num():
    start, step = get_rand_num(), get_rand_num()
    progression = []
    for i in range(PROGRESSION_LENGTH):
        progression.append(start + step * i)

    missed_index = random.randint(0, PROGRESSION_LENGTH - 1)
    missed_num = progression[missed_index]
    progression[missed_index] = '..'
    pg = ' '.join(map(str, progression))
    return pg, str(missed_num)


def run_progression_game():
    run_game(get_pg_and_missed_num, GAME_INSTRUCTIONS['progression'])
