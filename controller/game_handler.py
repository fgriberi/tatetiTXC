"""
TXC-Tateti project
"""

from model.board import Board


class GameHandler(object):
    """
    This class is responsible to capture the game events produced
    in the view module
    """
    PLAYER_ONE = "player1"
    def __init__(self):
        self._board = Board()

    def start_game(self):
        """
        Starts a new game
        """
        return "Game Started!"

    def mark(self, player, x, y):
        """
        Mark value
        """
        mark = Board.CIRCLE if self.PLAYER_ONE else Board.CROSS
        self._board.do_mark(mark, x, y)

    def get_board_status(self):
        """
        Returns board status
        """
        return self._board.board
