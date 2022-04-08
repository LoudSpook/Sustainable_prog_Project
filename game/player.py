"""Handle most things related to the player(s)."""


class Player():
    """Handle the player object."""

    def __init__(self):
        """Set default values to the object."""
        self.name = ""
        self.score = 0

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


if __name__ == '__main__':
    player = Player()
