from brain_games.utils import get_rand_num
from brain_games.engine import run_game
from brain_games.const import QUESTIONS


def is_prime(num):
    return 'no' if num <= 1 or any(num % i == 0 for i in range(2, (num // 2 + 1))) else 'yes'


def get_num_and_prime_ans():
    num = get_rand_num()
    prime = is_prime(num)
    return num, prime


def run_prime():
    run_game(get_num_and_prime_ans, QUESTIONS['prime'])
