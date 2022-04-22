"""Handle things related to the dice."""

import random

class Dice():
    """Handle the dice object."""

    def __init__(self):
        """Instantiate object."""
        self.rolls_made = 0
        random.seed()
