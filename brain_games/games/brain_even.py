import random

MAX_COUNT = 3
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no". '

def get_question():
    question = random.randint(1, 20)
    return question

def correct_answer(question):
    if question % 2 == 0:
        correct = 'yes'
        return correct
    else:
        correct = 'no'
        return correct
