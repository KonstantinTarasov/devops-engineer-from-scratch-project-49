from brain_games.cli import welcome_user
from brain_games.module import greet
import prompt
import random


def main():
    greet()
    name = welcome_user() # переменная обязательно присваивается иначе, name не сохранится
    print('Answer "yes" if the number is even, otherwise answer "no". ')
    
    count = 0
    while count < 3:
        number = random.randint(1, 20)        
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            even = 'yes'
        else:
            even = 'no'

        if answer == even:
            print("Correct")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{even}'.")
            print(f"Let's try again, {name}!")
            break

    print(f"Congratulations, {name}!")

if __name__ == "__main__":  # Обязательно нужно проверять, иначе будет задвоение
    main()
