from brain_games.cli import welcome_user
# from brain_games.cli import greet


def main():
    # greet()
    # переесли greet из cli и вынесли из функции приветствие
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == "__main__":  # Обязательно нужно проверять, иначе будет задвоение
    main()
