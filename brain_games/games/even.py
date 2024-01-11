from brain_games.utils import get_rand_num
from brain_games.engine import run_game
from brain_games.const import QUESTIONS


def get_num_and_even_ans():
    num = get_rand_num()
    even_ans = 'yes' if num % 2 == 0 else 'no'
    return num, even_ans


def run_even_odd():
    run_game(get_num_and_even_ans, QUESTIONS['even_odd'])
