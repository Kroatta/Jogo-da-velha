import pytest
from tic_tac_toe import TicTacToe

def test_player_x_wins_row():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(1, 0)  # O
    game.play(0, 1)  # X
    game.play(1, 1)  # O
    result = game.play(0, 2)  # X
    assert result == "Player X wins!"

def test_player_o_wins_column():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(0, 1)  # O
    game.play(1, 0)  # X
    game.play(1, 1)  # O
    game.play(2, 2)  # X
    result = game.play(2, 1)  # O
    assert result == "Player O wins!"

def test_player_wins_diagonal():
    game = TicTacToe()
    game.play(0, 0)  # X
    game.play(0, 1)  # O
    game.play(1, 1)  # X
    game.play(0, 2)  # O
    result = game.play(2, 2)  # X
    assert result == "Player X wins!"

def test_draw():
    game = TicTacToe()
    moves = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2)
    ]
    results = [game.play(r, c) for r, c in moves]
    assert results[-1] == "Draw!"

def test_switch_turns():
    game = TicTacToe()
    assert game.current_player == "X"
    game.play(0, 0)
    assert game.current_player == "O"
    game.play(1, 1)
    assert game.current_player == "X"

def test_block_double_play():
    game = TicTacToe()
    game.play(0, 0)
    result = game.play(0, 0)
    assert result == "Field already taken."

def test_game_over_blocks_play():
    game = TicTacToe()
    game.play(0, 0)
    game.play(1, 0)
    game.play(0, 1)
    game.play(1, 1)
    game.play(0, 2)  # X wins
    result = game.play(2, 2)  # Tentativa depois do fim
    assert "Game over" in result
