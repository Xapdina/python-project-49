import prompt
from brain_games.const import MAX_ROUND


def run_game(get_question_and_answer, game_instruction):
    player_name = prompt.string('Welcome to the Brain Games!\n'
                                'May I have your name? ')
    print(f'Hello, {player_name}!\n'
          f'{game_instruction}')

    for _ in range(MAX_ROUND):
        question, correct_answer = get_question_and_answer()
        player_answer = prompt.string(f'Question: {question}\n'
                                      f'Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {player_name}!")
            return

    return print(f'Congratulations, {player_name}!')
