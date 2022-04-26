"""Unittesting."""

import unittest
from game import bot

class testBotClass(unittest.TestCase):
    """Test the computer opponent class."""

    def setUp(self):
        self.bot = bot.Bot()

    def tearDown(self):
        del self.bot

    def test_init_bot_object(self):
        """Test an instantiated bot object's default values."""
        self.assertIsInstance(self.bot, bot.Bot)
