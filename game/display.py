"""Handle things related to the display of menus."""

import time

class Display():
    """Handle the display object."""

    def __init__(self):
        """Instantiate object."""

    def print_start_menu(self):
        time.sleep(1)
        print("-------------------------\n"
        "1. Singleplayer\n"
        "2. Multiplayer\n"
        "3. Rules\n"
        "4. Exit\n"
        "-------------------------")

    def print_rules(self):
        time.sleep(1)
        print("RULES\n"
        "-------------------------\n"
        "Take turns rolling the die.\n"
        "You can roll until you roll a 1 or decide to hold.\n"
        "If you decide to hold, you add the numbers from every roll and\n"
        "add that to your total score.\n"
        "If you roll a 1, you get no points from that round.\n"
        "After you've rolled a 1 or decided to hold, it's next players turn.\n"
        "First to a score total of 100 wins.\n"
        "Good luck and have fun!")

    def print_game_menu(self):
        time.sleep(1)
        print(
        "-------------------------\n"
        "1. Roll\n"
        "2. Hold\n"
        "3. Change name\n"
        "4. Restart\n"
        "5. Exit"
        )
