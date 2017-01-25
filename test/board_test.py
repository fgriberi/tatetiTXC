"""
TXC-Tateti project
"""

import unittest
from model.board import Board


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
        self.assertEqual(self.board.width, Board.DEFAULT_BOARD_WIDTH)

    def test_board_height(self):
        """
        Check the board height
        """
        self.assertEqual(self.board.height, Board.DEFAULT_BOARD_HEIGHT)

    def test_empty_board(self):
        cboard = self.board.board

        expected_board = [[Board.EMPTY, Board.EMPTY, Board.EMPTY],
                          [Board.EMPTY, Board.EMPTY, Board.EMPTY],
                          [Board.EMPTY, Board.EMPTY, Board.EMPTY]]

        self.assertEqual(cboard, expected_board)
