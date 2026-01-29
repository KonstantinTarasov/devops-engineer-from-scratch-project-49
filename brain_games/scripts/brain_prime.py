from brain_games.engine import game_engine
from brain_games.games.brain_prime import (
    GAME_RULES,
    MAX_COUNT,
    get_question_answer,
)


def main():
    game_engine(game_rules=GAME_RULES,
                max_count=MAX_COUNT,
                func_question=get_question_answer)


if __name__ == "__main__":
    main()
