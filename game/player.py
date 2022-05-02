"""Handle most things related to the player(s)."""


class Player():
    """Handle the player object."""

    name = ""
    score = 0
    rolls = 0

    def __init__(self):
        """Instantiate the object."""

    def select_name(self):
        """Let players select their name."""
        keep_going = True
        forbidden_word = "BOT"

        while keep_going:
            self.name = input("Select your name: ")

            if self.name:
                if forbidden_word not in self.name:
                    keep_going = False
                else:
                    print('Name can not contain "BOT"!')
            else:
                print("Name can not be empty!")

        print("Name set!")
        return self.name

    def change_name(self):
        """Let players change their names."""
        current_name = self.name
        new_name = self.select_name()

        if current_name == new_name:
            print("You already have this name!")
            self.name = current_name
        else:
            print("Name changed!")

        return self.name

    def add_score(self, score_to_add, rolls_to_add):
        """Add a players score from that round to their total."""
        self.score += score_to_add
        self.rolls += rolls_to_add

        return self.score, self.rolls

    def clean_score(self):
        """Reset a players score and rolls to 0."""
        self.score = 0
        self.rolls = 0

    def cheat(self):
        """Let's a player cheat to skip to the end."""
        self.score = 100
        print("\nCheater...")
