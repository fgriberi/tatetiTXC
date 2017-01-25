"""
TXC-Tateti project
"""


class Board(object):
    """
    This class is responsible to keep the state of the board
    """
    DEFAULT_BOARD_WIDTH = 3
    DEFAULT_BOARD_HEIGHT = 3

    EMPTY = 0
    CIRCLE = 1
    CROSS = 2

    def __init__(self):
        self._width = self.DEFAULT_BOARD_WIDTH
        self._height = self.DEFAULT_BOARD_HEIGHT
        self._board = self._initialize_board()

    def _initialize_board(self):
        new_board = list()
        for row in range(0, self.DEFAULT_BOARD_WIDTH):
            row_list = list()
            for col in range(0, self.DEFAULT_BOARD_HEIGHT):
                row_list.append(self.EMPTY)
            new_board.append(row_list)

        return new_board

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def board(self):
        return self._board

    def is_empty(self):
        return True
