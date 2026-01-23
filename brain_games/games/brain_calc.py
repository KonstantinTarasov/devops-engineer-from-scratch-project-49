import random

MAX_COUNT = 3
GAME_RULES = 'What is the result of the expression? '

def get_question_answer():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"{number_1} {operation} {number_2}"

    if operation == '+':
        correct_answer  = (int(number_1) + int(number_2))
    elif operation == '-':
        correct_answer = (int(number_1) - int(number_2))
    elif operation == '*':
        correct_answer = (int(number_1) * int(number_2))
    return question, str(correct_answer)    
