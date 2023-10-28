#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import start_game_even_odd


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    start_game_even_odd(user_name)


if __name__ == "__main__":
    main()
