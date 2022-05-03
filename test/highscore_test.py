"""Unittesting."""

import unittest
from game import highscore

class testHighscoreClass(unittest.TestCase):
    """Test the display class."""

    def setUp(self):
        self.highscore = highscore.Highscore()

    def tearDown(self):
        del self.highscore

    def test_init_highscore_object(self):
        """Test if a highscore object is instantiated properly."""
        self.assertIsInstance(self.highscore, highscore.Highscore)
