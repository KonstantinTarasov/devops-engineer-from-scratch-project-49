import random

MAX_COUNT = 3
GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no". '


def get_sequence():
    sequence = list(range(2, 51))
    
    n = 0
    while n < len(sequence):
        div = sequence[n]
        new_sequence = []
 
        for number in sequence:
            if number == div or number % div != 0:
                new_sequence.append(number)
        sequence = new_sequence
        n += 1
    return new_sequence
        

def get_question_answer():
    new_sequence = get_sequence()
    question = random.randint(1, 50)
    if question in new_sequence:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
