import random

MAX_COUNT = 3
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no". '


def get_question_answer():
    question = random.randint(1, 20)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
