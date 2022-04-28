"""Handle things related to the computer opponent."""


class Bot():
    """Handle the bot object."""

    name = "BOT"
    score = 0
    rolls = 0
    skips = 0
    max_rolls = 5

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
            self.skips = 1
        elif self.difficulty == 3:
            print("Difficulty set to hard")
            self.skips = 2

        return self.difficulty

    def add_score(self, score_to_add, rolls_to_add):
        """Add a bot's score from that round to its total"""
        self.score += score_to_add
        self.rolls += rolls_to_add

        return self.score, self.rolls
