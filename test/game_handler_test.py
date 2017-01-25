"""
TXC-Tateti project
"""

import unittest
import io
import sys

from controller.game_handler import GameHandler
from contextlib import contextmanager


@contextmanager
def capture_output():
    new_out = io.StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


class TestGameHandler(unittest.TestCase):
    """
    This class is responsible to test controller class
    """
    ghandler = None

    def setUp(self):
        self.ghandler = GameHandler()

    def tearDown(self):
        self.ghandler = None

    def test_new_game(self):
        """
        Check the new game method
        """
        status = self.ghandler.start_game()
        self.assertEqual("Game Started!", status)

    def test_board_started(self):
        self.assertTrue(self.ghandler._board is not None and
                        self.ghandler._board.is_empty())

    def test_get_initial_board(self):
        expected_board = [[Board.EMPTY, Board.EMPTY, Board.EMPTY],
                  [Board.EMPTY, Board.EMPTY, Board.EMPTY],
                  [Board.EMPTY, Board.EMPTY, Board.EMPTY]]
        self.assertEqual(expected_board, self.ghandler.get_board_status())

