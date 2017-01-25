"""
TXC-Tateti project
"""

DEFAULT_BOARD_WIDTH = 3
DEFAULT_BOARD_HEIGHT = 3


class Board(object):
    """
    This class is responsible to keep the state of the board
    """

    def __init__(self):
        self._width = DEFAULT_BOARD_WIDTH
        self._height = DEFAULT_BOARD_HEIGHT

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def is_empty(self):
        return True
