"""Handle things related to the dice."""

import random

class Dice():
    """Handle the dice object."""

    faces = 6

    def __init__(self):
        """Instantiate object."""
        self.rolls_made = 0
        random.seed()

    def roll_dice(self):
        """Roll a dice."""
        roll = random.randint(1, self.faces)
        self.rolls_made += 1

        return roll

    if __name__ == '__main__':
        die = Dice()
