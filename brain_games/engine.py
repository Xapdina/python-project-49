import prompt
from brain_games.const import MAX_ROUND


def is_engine_games(games, task):
    name = prompt.string(
        'Welcome to the Brain Games!\n'
        'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{task}')

    for count_round in range(MAX_ROUND):
        question, correct_answer = games()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')
        print('Correct!')
        if correct_answer != player_answer:
            print(f"'{player_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
