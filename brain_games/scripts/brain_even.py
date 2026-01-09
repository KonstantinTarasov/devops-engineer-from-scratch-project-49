from brain_games.games.brain_even import MAX_COUNT, GAME_RULES, get_question, correct_answer
from brain_games.engine import game_engine


def main():
    game_engine(game_rules=GAME_RULES,
                max_count=MAX_COUNT,
                func_question=get_question,
                correct_answer=correct_answer)


if __name__ == "__main__":  # Обязательно нужно проверять, иначе будет задвоение
    main()
