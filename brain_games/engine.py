import prompt
from brain_games.const import MAX_ROUND


def get_question_and_answer(game, task):
    player_name = prompt.string('Welcome to the Brain Games!\n'
                                'May I have your name? ')
    print(f'Hello, {player_name}!\n'
          f'{task}')

    for _ in range(MAX_ROUND):
        question, correct_answer = game()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            return print(f"'{player_answer}' is wrong answer ;(.\n"
                         f"Correct answer was '{correct_answer}'.\n"
                         f"Let's try again, {player_name}!")

    return print(f'Congratulations, {player_name}!')
