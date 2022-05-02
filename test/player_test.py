"""Unittesting."""

import unittest
from game import player
from unittest import mock

class TestPlayerClass(unittest.TestCase):
    """Testing the class."""

    def setUp(self):
        self.player = player.Player()

    def tearDown(self):
        del self.player

    def test_init_player_object(self):
        """Test if a player object was instantiated correctly and
        test its default values."""
        self.assertIsInstance(self.player, player.Player)

        res_name = self.player.name
        exp_name = ""
        self.assertEqual(res_name, exp_name)

        res_score = self.player.score
        exp_score = 0
        self.assertEqual(res_score, exp_score)

        res_rolls = self.player.rolls
        exp_rolls = 0
        self.assertEqual(res_rolls, exp_rolls)



    def test_name(self):
        """Select and change a player's name and test if the name was
        properly changed both times (use two different names)."""
        name = self.player.select_name()
        err = ""

        self.assertNotEqual(err, self.player.name)
        self.assertEqual(self.player.name, name)

        new_name = self.player.change_name()
        self.assertNotEqual(name, new_name)
        self.assertEqual(self.player.name, new_name)

    def test_add_score(self):
        """Add a score of 12 and 2 rolls to the players total and
        test if they're added correctly."""
        old_score = self.player.score
        old_rolls = self.player.rolls

        self.player.add_score(12, 2)

        self.assertNotEqual(0, self.player.score)
        self.assertNotEqual(old_score, self.player.score)

        self.assertNotEqual(0, self.player.rolls)
        self.assertNotEqual(old_rolls, self.player.rolls)

    @mock.patch("game.player.print")
    def test_cheat(self, mock_cheat):
        self.player.cheat()
        mock_cheat.assert_called_with("\nCheater...")
        self.assertEqual(100, self.player.score)
