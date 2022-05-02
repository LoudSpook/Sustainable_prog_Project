"""Handle things related to the computer opponent."""


class Bot():
    """Handle the bot object."""

    name = "BOT"
    score = 0
    rolls = 0
    max_rolls = 4

    def __init___(self):
        """Instantiate object."""

    def select_difficulty(self):
        """Select the difficulty of the bot."""
        keep_going = True
        print("Difficulties: 1 - Easy, 2 - Medium, 3 - Hard")
        self.difficulty = input("Select difficulty: ")
        while keep_going:
            if self.difficulty == '1':
                print("Difficulty set to easy")
                keep_going = False
            elif self.difficulty == '2':
                print("Difficulty set to medium")
                self.score = 20
                keep_going = False
            elif self.difficulty == '3':
                print("Difficulty set to hard")
                self.score = 40
                keep_going = False
            else:
                print("Only 1-3 please!")

        return self.difficulty

    def add_score(self, score_to_add, rolls_to_add):
        """Add a bot's score from that round to its total"""
        self.score += score_to_add
        self.rolls += rolls_to_add

    def clean_score(self, difficulty):
        """Reset the bots score and rolls to default."""
        if difficulty == '1':
            self.score = 0
        elif difficulty == '2':
            self.score = 20
        else:
            self.score = 40

        self.rolls = 0

        return self.score, self.rolls
