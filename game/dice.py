"""Handle things related to the dice."""

import random


class Dice():
    """Handle the dice object."""

    faces = 6
    rolls_made = 0
    turn_total = 0

    def __init__(self):
        """Instantiate object."""
        random.seed()

    def roll_dice(self):
        """Roll a dice."""
        roll = random.randint(1, self.faces)
        self.rolls_made += 1
        self.turn_total += roll

        return roll

    def get_score(self):
        """Return rolls made and turn total."""
        return self.rolls_made, self.turn_total

    def clean_score(self):
        """Reset rolls made and turn total back to 0."""
        self.rolls_made = 0
        self.turn_total = 0
        return self.rolls_made, self.turn_total
