"""Unittesting."""

import unittest
from game import display

class testDisplayClass(unittest.TestCase):
    """Test the display class."""

    def setUp(self):
        self.display = display.Display()

    def tearDown(self):
        del self.display

    def test_init_display_object(self):
        """Test if a display object is instantiated properly."""
        self.assertIsInstance(self.display, display.Display)
