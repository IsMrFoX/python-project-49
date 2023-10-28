from brain_games.cli import welcome_user
from brain_games.games.calc import start_calc_game


def main():
    user_name = welcome_user()
    start_calc_game(user_name)


if __name__ == "__main__":
    main()
