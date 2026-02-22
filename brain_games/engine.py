import prompt

from brain_games.cli import welcome_user
from brain_games.cli import greet


def game_engine(game):

    greet()
    name = welcome_user()  # переменная обязательно присваивается 
    print(f'{game.GAME_RULES}')  # аккуратно с кавычками при интерпаляции
    
    count = 0
    while count < game.MAX_COUNT:
        question, correct_answer = game.get_question_answer()        
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        correct = correct_answer

        if answer == correct:
            print("Correct")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            exit()
    print(f"Congratulations, {name}!")
