import logging
import random
import sys

CHOICES = ['rock', 'paper', 'scissors']

WINNING_COMBINATIONS = {
    'rock': 'scissors',  # rock beats scissors
    'scissors': 'paper',  # scissors beats paper
    'paper': 'rock'  # paper beats rock
}

s_logger = None


class Game:
    def __init__(self, rounds: int) -> None:
        self.rounds = rounds
        self._user_score = 0
        self._computer_score = 0
        self._current_round = 0

    @classmethod
    def logger(cls):
        global s_logger
        if s_logger is None:
            s_logger = logging.getLogger(__name__)
        return s_logger

    @property
    def user_score(self):
        return self._user_score

    @user_score.setter
    def user_score(self, value: int):
        self._user_score = value

    @property
    def computer_score(self):
        return self._computer_score

    @computer_score.setter
    def computer_score(self, value: int):
        self._computer_score = value

    @property
    def current_round(self):
        return self._current_round

    @current_round.setter
    def current_round(self, value: int):
        self._current_round = value

    def get_user_choice(self):
        while True:
            try:
                user_input = input("Enter your choice (rock, paper, scissors): ").lower().strip()
                if user_input in CHOICES:
                    return user_input
                error_message = f"Invalid choice '{user_input}', please try again."
                self.logger().info(error_message)
                print(error_message)
            except KeyboardInterrupt:
                print("\nGame interrupted. Exiting...")
                self.logger().info(f"Score statistics: {self.show_stats()}, Round id: {self.current_round}")
                self.logger().warning("Game interrupted. Exiting...")
                sys.exit()
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                self.logger().error(f"Unexpected error: {e}")

    def get_computer_choice(self) -> str:
        return random.choice(CHOICES)

    def get_winner(self, user_choice: str, computer_choice: str) -> str:
        if user_choice == computer_choice:
            logging.info("The game is a tie")
            return "It's a tie!"
        elif WINNING_COMBINATIONS[user_choice] == computer_choice:
            self.user_score += 1
            logging.info("User wins this round")
            return "You win!"
        else:
            self.computer_score += 1
            logging.info("Computer wins this round")
            return "Computer wins!"

    def play_round(self, round_id: int) -> None:
        logging.info(f"Starting round {round_id}")
        self.current_round = round_id

        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()

        logging.info(f"User choice: {user_choice}, Computer choice: {computer_choice}")
        print(f"You chose: '{user_choice}' and computer chose: '{computer_choice}'")

        print(self.get_winner(user_choice, computer_choice))

    def show_stats(self) -> str:
        return f"Total score after {self.rounds} rounds - User: {self.user_score}, Computer: {self.computer_score}"

    def play_game(self):
        logging.info(f"Game started, total rounds: {self.rounds}")
        for i in range(1, self.rounds + 1):
            self.play_round(i)
            print("==========================================")
        print(self.show_stats())
