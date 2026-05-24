import random

MAX_COUNT = 3
GAME_RULES = 'What number is missing in the progression? '


# создаем последовательность
def get_sequence():
# УПРОЩЕН КОД С ПОМОЩЬЮ ФУНКЦИИ RANGE
#    number_1 = random.randint(1, 10)
    number_1 = 0
    step = random.randint(1, 4)
    count = 37
    sequence = []
#    i = 0
#    count = 10
#    while i < count:
#        current_element = number_1 + i * step
#        sequence.append(current_element)
#        i += 1
#    return sequence
    numbers = range(number_1, count, step)
    for number in numbers:
        sequence.append(number)
        if len(sequence) >= 10:
            break
    return sequence
    

# находим случайный элемент и заменяем его
def get_question_answer():
    sequence = get_sequence()
    random_element = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[random_element]
    for i in range(10):
        if sequence[i] == correct_answer:
            sequence[i] = '..'

    question = ''
    for number in sequence:
        question += str(number) + ' '
    return question, str(correct_answer)
