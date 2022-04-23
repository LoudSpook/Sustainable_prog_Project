"""Unittesting."""

import unittest
from game import player

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

        res1 = self.player.name
        exp1 = ""
        self.assertEqual(res1, exp1)

        res2 = self.player.score
        exp2 = 0
        self.assertEqual(res2, exp2)

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
        """Add a score of 3 to the players total and
        test if it is added correctly."""
        old_score = self.player.score
        self.player.add_score(3)
        self.assertNotEqual(0, self.player.score)
        self.assertNotEqual(old_score, self.player.score)

if __name__ == '__main__':
    unittest.main()
