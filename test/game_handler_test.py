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
        with capture_output() as out:
            self.ghandler.start_game()
            self.assertEqual(out.getvalue(), "Started new game\n")
