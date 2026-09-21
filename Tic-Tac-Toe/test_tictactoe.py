import importlib.util
import pathlib
import unittest
from unittest.mock import patch


MODULE_PATH = pathlib.Path(__file__).with_name("TicTacToe.py")
spec = importlib.util.spec_from_file_location("tictactoe", MODULE_PATH)
tictactoe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tictactoe)


class TestTicTacToe(unittest.TestCase):
    def test_is_winner_detects_row(self):
        board = tictactoe.create_board()
        board[1], board[2], board[3] = "X", "X", "X"
        self.assertTrue(tictactoe.isWinner(board, "X"))
        self.assertFalse(tictactoe.isWinner(board, "O"))

    def test_is_board_full(self):
        board = [" ", "X", "O", "X", "X", "O", "X", "O", "X", "O"]
        self.assertTrue(tictactoe.isBoardFull(board))
        board[9] = " "
        self.assertFalse(tictactoe.isBoardFull(board))

    def test_comp_move_wins_when_possible(self):
        board = tictactoe.create_board()
        board[1], board[2] = "O", "O"
        self.assertEqual(tictactoe.compMove(board), 3)

    def test_comp_move_blocks_player(self):
        board = tictactoe.create_board()
        board[1], board[2] = "X", "X"
        self.assertEqual(tictactoe.compMove(board), 3)

    def test_comp_move_prefers_center_after_win_block_checks(self):
        board = tictactoe.create_board()
        board[1] = "X"
        board[9] = "O"
        self.assertEqual(tictactoe.compMove(board), 5)

    def test_comp_move_uses_corner_then_edge(self):
        board = tictactoe.create_board()
        board[5] = "X"
        with patch.object(tictactoe.random, "choice", side_effect=lambda moves: moves[0]):
            self.assertIn(tictactoe.compMove(board), [1, 3, 7, 9])

        board = [" ", "X", " ", "X", " ", "X", " ", "X", " ", "X"]
        with patch.object(tictactoe.random, "choice", side_effect=lambda moves: moves[0]):
            self.assertIn(tictactoe.compMove(board), [2, 4, 6, 8])

    def test_comp_move_returns_none_for_full_board(self):
        board = [" ", "X", "O", "X", "X", "O", "X", "O", "X", "O"]
        self.assertIsNone(tictactoe.compMove(board))


if __name__ == "__main__":
    unittest.main()
