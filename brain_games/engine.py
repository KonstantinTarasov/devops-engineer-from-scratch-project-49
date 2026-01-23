from brain_games.cli import welcome_user
from brain_games.module import greet
from typing import Callable
import prompt

def game_engine(game_rules: str, max_count: int, func_question: Callable):

    greet()
    name = welcome_user() # переменная обязательно присваивается иначе, name не сохранится
    print(f'{game_rules}') # аккуратно с кавычками при интерпаляции
    
    count = 0
    while count < max_count:
#       question = func_question()
        question, correct_answer = func_question()        
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        correct = correct_answer

        if answer == correct:
            print("Correct")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            break
    print(f"Congratulations, {name}!")
