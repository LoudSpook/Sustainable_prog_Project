"""Hold functions used while playing the game."""

import dice
import player
import bot
import display
import dice_graphics
import sys
import time


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
        difficulty = self.player2.select_difficulty()

        return self.player1, self.player2, difficulty

    def multiplayer(self):
        """Handle the multiplayer option."""
        self.player1 = player.Player()
        self.player1.select_name()

        self.player2 = player.Player()
        self.player2.select_name()

        return self.player1, self.player2

    def rules(self):
        """Handle choosing to print the rules."""
        self.display = display.Display()
        self.display.print_rules()
        del self.display

    def create_dice(self):
        """Create a dice object."""
        self.dice = dice.Dice()

    def roll(self):
        """Handle choosing to roll a dice."""
        self.dice_graphics = dice_graphics.DiceGraphics()
        roll = self.dice.roll_dice()

        if roll == 1:
            self.dice_graphics.dice_one()
            print("You rolled a 1!")
            self.continue_turn = False
            self.dice.clean_score()
            del self.dice_graphics

        elif roll == 2:
            self.dice_graphics.dice_two()
            del self.dice_graphics

        elif roll == 3:
            self.dice_graphics.dice_three()
            del self.dice_graphics

        elif roll == 4:
            self.dice_graphics.dice_four()
            del self.dice_graphics

        elif roll == 5:
            self.dice_graphics.dice_five()
            del self.dice_graphics

        elif roll == 6:
            self.dice_graphics.dice_six()
            del self.dice_graphics

        return self.continue_turn

    def delete_dice(self):
        """Delete a dice object."""
        del self.dice

    def exit_choice(self):
        """Exit the program."""
        sys.exit("Exiting game")

    def bot_turn(self, bot):
        """Handle how the but turn work."""
        keep_going = True
        bot_won = False
        max_rolls = bot.max_rolls

        self.create_dice()

        print("")
        print(bot.name + "'s turn")

        while keep_going:
            time.sleep(1)

            continue_turn = self.roll()

            if continue_turn:
                if max_rolls > 0:
                    max_rolls -= 1
                else:
                    keep_going = False
            else:
                keep_going = False

        score_to_add = self.dice.get_turn_total()
        rolls_to_add = self.dice.get_rolls_made()
        bot.add_score(score_to_add, rolls_to_add)
        print("BOT score: " + str(bot.score))

        if bot.score >= 100:
            bot_won = True

        return bot_won

    def turn(self, player):
        """Handle how the player turns work."""
        keep_going = True
        player_won = False
        self.create_dice()

        self.display = display.Display()

        while keep_going:
            reset = False

            print("")
            print(player.name + "'s turn")
            self.display.print_game_menu()
            choice = input("..: ")

            if choice == '1':
                continue_turn = self.roll()
                if not continue_turn:
                    keep_going = False

            elif choice == '2':
                keep_going = False
                score_to_add = self.dice.get_turn_total()
                rolls_to_add = self.dice.get_rolls_made()

                player.add_score(score_to_add, rolls_to_add)
                print("Your score is:", player.score)

            elif choice == '3':
                player.change_name()

            elif choice == '4':
                keep_going = False
                reset = True

            elif choice == '5':
                self.exit_choice()

            elif choice == '0':
                player.cheat()
                keep_going = False
            else:
                print("Only 1-5 please!")

            if player.score >= 100:
                player_won = True

        self.delete_dice()

        return player_won, reset
