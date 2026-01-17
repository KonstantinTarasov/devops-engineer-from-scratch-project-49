import random

MAX_COUNT = 3
GAME_RULES = 'Find the greatest common divisor of given numbers.'

def get_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f"{number_1} {number_2}"
    return question
    

def correct_answer(question):
    number_1, number_2 = question.split(" ")
    number_1 = int(number_1)
    number_2 = int(number_2)
    variable = 0
    while number_2 != 0:
        variable = number_2
        number_2 = number_1 % number_2
        number_1 = variable
    return str(number_1)
