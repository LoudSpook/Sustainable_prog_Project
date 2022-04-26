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

        exp_name = "BOT"
        res_name = self.bot.name
        self.assertEqual(res_name, exp_name)

        exp_score = 0
        self.assertEqual(self.bot.score, exp_score)

        exp_rolls_made = 0
        self.assertEqual(self.bot.rolls_made, exp_rolls_made)
