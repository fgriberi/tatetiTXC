"""
TXC-Tateti project
"""

import unittest
from model.board import Board

BOARD_WIDTH = 3
BOARD_HEIGHT = 3


class BoardTest(unittest.TestCase):
    """
    This class is responsible to test the model Board class methods
    """

    board = None

    def setUp(self):
        self.board = Board()

    def tearDown(self):
        self.board = None

    def test_init_board(self):
        """
        Check the board initial state
        """
        self.assertTrue(self.board.is_empty())

    def test_board_width(self):
        """
        Check the board width
        """
        self.assertEqual(self.board.width, BOARD_WIDTH)

    def test_board_height(self):
        """
        Check the board height
        """
        self.assertEqual(self.board.height, BOARD_HEIGHT)
