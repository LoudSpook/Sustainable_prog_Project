"""Unittesting."""

import unittest
from game import dice_graphics
from unittest import mock

class TestDiceGraphics(unittest.TestCase):
    """Testing the class."""

    def setUp(self):
        self.dice_graphics = dice_graphics.DiceGraphics()

    def tearDown(self):
        del self.dice_graphics

    @mock.patch("game.dice_graphics.print")
    def test_dice_one(self, mock_dice_one):
        self.dice_graphics.dice_one()
        mock_dice_one.assert_called_with(
        " -----------\n"
        "|           |\n"
        "|     o     |\n"
        "|           |\n"
        " -----------"
        )

    @mock.patch("game.dice_graphics.print")
    def test_dice_two(self, mock_dice_two):
        self.dice_graphics.dice_two()
        mock_dice_two.assert_called_with(
        " -----------\n"
        "|  o        |\n"
        "|           |\n"
        "|        o  |\n"
        " -----------"
        )

    @mock.patch("game.dice_graphics.print")
    def test_dice_three(self, mock_dice_three):
        self.dice_graphics.dice_three()
        mock_dice_three.assert_called_with(
        " -----------\n"
        "|  o        |\n"
        "|     o     |\n"
        "|        o  |\n"
        " -----------"
        )

    @mock.patch("game.dice_graphics.print")
    def test_dice_four(self, mock_dice_four):
        self.dice_graphics.dice_four()
        mock_dice_four.assert_called_with(
        " -----------\n"
        "|  o     o  |\n"
        "|           |\n"
        "|  o     o  |\n"
        " -----------"
        )

    @mock.patch("game.dice_graphics.print")
    def test_dice_five(self, mock_dice_five):
        self.dice_graphics.dice_five()
        mock_dice_five.assert_called_with(
        " -----------\n"
        "|  o     o  |\n"
        "|     o     |\n"
        "|  o     o  |\n"
        " -----------"
        )

    @mock.patch("game.dice_graphics.print")
    def test_dice_six(self, mock_dice_six):
        self.dice_graphics.dice_six()
        mock_dice_six.assert_called_with(
        " -----------\n"
        "|  o  o  o  |\n"
        "|           |\n"
        "|  o  o  o  |\n"
        " -----------"
        )
