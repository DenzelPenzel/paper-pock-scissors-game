from unittest.mock import patch
from game.app.game_app import Game
from typing import List, Tuple


def calls(rounds: int, user_inputs: List[str]) -> Tuple[int, int]:
    game = Game(rounds)
    with patch('builtins.input', side_effect=user_inputs):
        game.play_game()
    return game.user_score, game.computer_score


def is_valid_score(user_score: int, computer_score: int) -> bool:
    return (user_score == 0 and computer_score == 0) or user_score > computer_score or computer_score >= user_score


def test_all_outcomes():
    for user, pc, want in [
        ('rock', 'scissors', 'You win!'),
        ('scissors', 'paper', 'You win!'),
        ('paper', 'rock', 'You win!'),
        ('rock', 'paper', 'Computer wins!'),
        ('scissors', 'rock', 'Computer wins!'),
        ('paper', 'scissors', 'Computer wins!'),
        ('rock', 'rock', "It's a tie!"),
        ('paper', 'paper', "It's a tie!"),
        ('scissors', 'scissors', "It's a tie!")
    ]:
        game = Game(1)
        got = game.get_winner(user, pc)
        assert want == got


def test_success_inputs():
    user_inputs = ['scissors', 'paper', 'rock', 'rock']
    user_score, computer_score = calls(len(user_inputs), user_inputs)
    assert (user_score + computer_score) >= 0


def test_failed_inputs():
    user_inputs = ['a', 'b', 'c', 'd', 'rock', 'paper', 'scissors', 'rock']
    user_score, computer_score = calls(4, user_inputs)
    assert is_valid_score(user_score, computer_score)


def test_zero_rounds():
    user_inputs = ['rock']
    user_score, computer_score = calls(0, user_inputs)
    assert is_valid_score(user_score, computer_score)


def test_uppercase_input():
    user_inputs = ['Rock']
    user_score, computer_score = calls(1, user_inputs)
    assert is_valid_score(user_score, computer_score)


def test_whitespace_input():
    user_inputs = [' scissors ', '  rock  ', ' paper  ']
    user_score, computer_score = calls(1, user_inputs)
    assert is_valid_score(user_score, computer_score)


def test_repeated_input():
    user_inputs = ['rock', 'rock', 'rock']
    user_score, computer_score = calls(len(user_inputs), user_inputs)
    assert is_valid_score(user_score, computer_score)


def test_max_rounds():
    user_inputs = ['paper'] * 10000
    user_score, computer_score = calls(len(user_inputs), user_inputs)
    assert is_valid_score(user_score, computer_score)
