from brain_games.cli import welcome_user
from brain_games.games.single_number_game import start_game
from brain_games.game_logic import check_prime


def main():
    user_name = welcome_user()
    game_greeting = '"yes" if given number is prime. Otherwise answer "no".'
    start_game(user_name, game_greeting, check_prime)


if __name__ == "__main__":
    main()
