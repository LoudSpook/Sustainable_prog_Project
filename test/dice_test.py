"""Unittesting."""

import unittest
from game import dice

class TestDiceClass(unittest.TestCase):
    """Test the dice class."""

    def test_init_dice_object(self):
        """Instantiate a dice object and test its values."""
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice)

        res = die.faces
        exp = 6
        self.assertEqual(res, exp)

    def test_roll_dice(self):
        """Roll a dice and test the roll."""
        die = dice.Dice()
        roll = die.roll_dice()
        expected = 1 <= roll <= die.faces
        self.assertTrue(expected)

    def test_get_rolls_made(self):
        """Roll dice, get the amount of rolls made and test to see
        if it's correct."""
        die = dice.Dice()
        default_amount = 0
        die.roll_dice()
        roll_amount = die.get_rolls_made()
        self.assertNotEqual(default_amount, roll_amount)

    def test_clean_rolls_made(self):
        """Roll a dice a few times then reset the number of rolls made
        back to 0 and test if rolls_made was reset."""
        die = dice.Dice()
        for x in range(3):
            die.roll_dice()

        die.clean_rolls_made()
        exp = 0
        self.assertEqual(exp, die.get_rolls_made())

if __name__ == '__main__':
    unittest.main()
