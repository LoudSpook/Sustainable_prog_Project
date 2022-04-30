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
        self.assertEqual(self.bot.rolls, exp_rolls_made)

        exp_skips = 0
        res_skips = self.bot.skips
        self.assertEqual(exp_skips, res_skips)

        exp_max_rolls = 5
        res_max_rolls = self.bot.max_rolls
        self.assertEqual(exp_max_rolls, res_max_rolls)

    def test_bot_difficulty(self):
        """Test if the difficulty variable is properly returned."""
        difficulty = self.bot.select_difficulty()
        err = None

        self.assertNotEqual(err, self.bot.difficulty)
        self.assertEqual(self.bot.difficulty, difficulty)

    def test_add_score(self):
        """Add a score of 12 and 2 rolls to the bots total and test
        if they're added correctly."""
        old_score = self.bot.score
        old_rolls = self.bot.rolls

        self.bot.add_score(12, 2)

        self.assertNotEqual(0, self.bot.score)
        self.assertNotEqual(old_score, self.bot.score)

        self.assertNotEqual(0, self.bot.rolls)
        self.assertNotEqual(old_rolls, self.bot.rolls)
