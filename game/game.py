"""Hold functions used while playing the game."""

import dice
import player
import bot
import display
import sys

class Game():
    """Handle the game."""

    continue_turn = True

    def __init__(self):
        """Initiate object."""
        self.choice = None

    def singleplayer(self):
        """Handle the singleplayer option."""
        self.player1 = player.Player()
        self.player1.select_name()

        self.player2 = bot.Bot()
        self.player2.select_difficulty()

    def multiplayer(self):
        """Handle the multiplayer option."""
        self.player1 = player.Player()
        self.player1.select_name()

        self.player2 = player.Player()
        self.player2.select_name()

        return self.player1, self.player2

    def rules(self):
        "Handle choosing to print the rules."""
        self.display = display.Display()
        self.display.print_rules()
        del self.display

    def create_dice(self):
        """Create a dice object."""
        self.dice = dice.Dice()

    def roll(self, dice):
        """Handle choosing to roll a dice."""
        roll = self.dice.roll_dice()
        print(self.dice.turn_total)
        print("Roll: ", roll)
        if roll == 1:
            print("You rolled a 1!")
            self.continue_turn = False
            self.dice.clean_score()

    def hold(self, player, dice):
        """Handle choosing to hold."""
        player.add_score(self.dice.turn_total, self.dice.rolls_made)
        self.continue_turn = False


    def delete_dice(self):
        """Deletes a dice object."""
        del self.dice

    def exit_choice(self):
        sys.exit("You chose to exit")


if __name__ == '__main__':
    game = Game()
    player1, player2 = game.multiplayer()
    game.create_dice()

    game.roll(dice)
    game.roll(dice)
    game.roll(dice)
    print(game.dice.turn_total)
