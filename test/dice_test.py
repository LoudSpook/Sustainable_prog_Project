"""Unittesting."""

import unittest
from game import dice

class TestDiceClass(unittest.TestCase):
    """Test the dice class."""

    def setUp(self):
        self.dice = dice.Dice()

    def tearDown(self):
        del self.dice

    def test_init_dice_object(self):
        """Test an instantiated dice object's default values."""
        self.assertIsInstance(self.dice, dice.Dice)

        res = self.dice.faces
        exp = 6
        self.assertEqual(res, exp)

    def test_roll_dice(self):
        """Roll a dice and test the roll."""
        roll = self.dice.roll_dice()
        expected = 1 <= roll <= self.dice.faces
        self.assertTrue(expected)

    def test_get_score(self):
        """Roll dice, get the amount of rolls made and test to see
        if it's correct."""
        default_amount = 0
        self.dice.roll_dice()
        roll_amount = self.dice.get_score()
        self.assertNotEqual(default_amount, roll_amount)

    def test_clean_score(self):
        """Roll a dice a few times then reset the number of rolls made
        back to 0 and test if rolls_made was reset."""
        for x in range(3):
            self.dice.roll_dice()

        self.dice.clean_score()
        exp = 0, 0
        self.assertEqual(exp, self.dice.get_score())

if __name__ == '__main__':
    unittest.main()
