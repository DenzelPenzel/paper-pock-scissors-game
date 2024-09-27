#!/usr/bin/env python

import path_util  # noqa: F401
from game.app.game_app import Game
from game import init_logging

MAX_ROUNDS = 10000


def main():
    init_logging("game_logs.yml")
    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds <= 0 or rounds > MAX_ROUNDS:
                raise ValueError(f"Number of rounds must be a positive integer up to {MAX_ROUNDS}.")
            break
        except ValueError:
            print("Please enter a valid number of rounds")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            exit()

    Game(rounds).play_game()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
