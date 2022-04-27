"""Handle things related to the computer opponent."""


class Bot():
    """Handle the bot object."""

    name = "BOT"
    score = 0
    rolls_made = 0

    def __init___(self):
        """Instantiate object."""

    def select_difficulty(self):
        """Select the difficulty of the bot."""
        print("Difficulties: 1 - Easy, 2 - Medium, 3 - Hard")
        self.difficulty = input("Select difficulty: ")

        if self.difficulty == 1:
            print("Difficulty set to easy")
        elif self.difficulty == 2:
            print("Difficulty set to medium")
        elif self.difficulty == 3:
            print("Difficulty set to hard")

        return self.difficulty
