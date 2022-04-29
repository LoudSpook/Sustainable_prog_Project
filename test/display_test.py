"""Unittesting."""

import unittest
from game import display
from unittest import mock

class testDisplayClass(unittest.TestCase):
    """Test the display class."""

    def setUp(self):
        self.display = display.Display()

    def tearDown(self):
        del self.display

    def test_init_display_object(self):
        """Test if a display object is instantiated properly."""
        self.assertIsInstance(self.display, display.Display)

    @mock.patch("game.display.print")
    def test_print_start_menu(self, mock_print_start_menu):
        self.display.print_start_menu()
        mock_print_start_menu.assert_called_with("-------------------------\n"
        "1. Single player\n2. Multiplayer\n3. Exit\n-------------------------")

    @mock.patch("game.display.print")
    def test_print_rules(self, mock_print_rules):
        self.display.print_rules()
        mock_print_rules.assert_called_with("RULES\n"
        "-------------------------\n"
        "Take turns rolling the die.\n"
        "You can roll until you roll a 1 or decide to hold.\n"
        "If you decide to hold, you add the numbers from every roll and\n"
        "add that to your total score.\n"
        "If you roll a 1, you get no points from that round.\n"
        "After you've rolled a 1 or decided to hold, it's next players turn.\n"
        "First to a score total of 100 wins.\n"
        "Good luck and have fun!")
