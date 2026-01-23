from brain_games.games.brain_calc import MAX_COUNT, GAME_RULES, get_question_answer
from brain_games.engine import game_engine


def main():
    game_engine(game_rules=GAME_RULES,
                max_count=MAX_COUNT,
                func_question=get_question_answer)


if __name__ == "__main__":
    main()
