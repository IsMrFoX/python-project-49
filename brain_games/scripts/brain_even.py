from brain_games.cli import welcome_user
from brain_games.games.even_or_odd import start_even_odd_game


def main():
    user_name = welcome_user()
    start_even_odd_game(user_name)


if __name__ == "__main__":
    main()
