import prompt
from brain_games.const import MAX_ROUND


def get_question_and_answer(games, task):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{task}')

    for _ in range(MAX_ROUND):
        question, correct_answer = games()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if correct_answer != player_answer:
            return print(f"'{player_answer}' is wrong answer ;(.\n"
                         f"Correct answer was '{correct_answer}'.\n"
                         f"Let's try again, {name}!")
        print('Correct!')
    return print(f'Congratulations, {name}!')
