from brain_games.cli import welcome_user
from brain_games.module import greet
import prompt
import random

def main():
    greet()
    name = welcome_user() # переменная обязательно присваивается иначе, name не сохранится
    print('What is the result of the expression? ')

    mathem_elements = ['+', '-', '*']
    count = 0
    result = 0
    while count < 3:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        operation = random.choice(mathem_elements)
        print(f"Question: {number_1} {operation} {number_2}")
        answer = prompt.string('Your answer: ')
        if operation == '+':
            result = number_1 + number_2
        elif operation == '-':
            result = number_1 - number_2
        elif operation == '*':
            result = number_1 * number_2

        if int(answer) == result:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
    
    print(f"Congratulations, {name}!")

if __name__ == "__main__":  # Обязательно нужно проверять, иначе будет задвоение
    main()
