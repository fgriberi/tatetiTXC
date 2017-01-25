"""
TXC-Tateti project
"""

from model.board import Board


class GameHandler(object):
    """
    This class is responsible to capture the game events produced
    in the view module
    """
    def __init__(self):
        self._board = Board()

    def start_game(self):
        """
        Starts a new game
        """
        return "Game Started!"
