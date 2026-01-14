import random

MAX_COUNT = 3
GAME_RULES = 'What is the result of the expression? '

def get_question():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"{number_1} {operation} {number_2}"
    return question

def correct_answer(question):
    number_1, operation, number_2 = question.split(" ")
    if operation == '+':
        result = (int(number_1) + int(number_2))
        return str(result)
    elif operation == '-':
        result = (int(number_1) - int(number_2))
        return str(result)
    elif operation == '*':
        result = (int(number_1) * int(number_2))
        return str(result)
