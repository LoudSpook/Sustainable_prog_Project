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

    def test_get_rolls_made(self):
        """Roll dice, get the amount of rolls made and test to see
        if it's correct."""
        default_amount = 0
        self.dice.roll_dice()
        roll_amount = self.dice.get_rolls_made()
        self.assertNotEqual(default_amount, roll_amount)

    def test_get_turn_total(self):
        """Roll dice, get the turn total score form the rolls and test
        to see if it's correct."""
        default_turn_total = 0
        self.dice.roll_dice()
        turn_total = self.dice.get_turn_total()
        self.assertNotEqual(default_turn_total, turn_total)

    def test_clean_score(self):
        """Test if rolls_made and turn_total are properly reset after rolls
        are made."""
        for x in range(3):
            self.dice.roll_dice()

        self.dice.clean_score()
        exp_rolls_made = 0
        exp_turn_total = 0
        self.assertEqual(exp_rolls_made, self.dice.get_rolls_made())
        self.assertEqual(exp_turn_total, self.dice.get_turn_total())
