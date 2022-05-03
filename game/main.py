"""Run the game."""

import game
import display
import highscore


class Main():
    """Handle running the game."""

    def main():
        """Run the game."""
        keep_going = True
        player_turn = 1
        bot = False
        game_in_progress = True

        print("Welcome to the game!")
        display.Display().print_start_menu()

        while keep_going:
            choice = input("..: ")

            if choice == '1':
                player1, player2, difficulty = game.Game().singleplayer()
                keep_going = False
                bot = True
            elif choice == '2':
                player1, player2 = game.Game().multiplayer()
                keep_going = False
            elif choice == '3':
                display.Display().print_rules()
                keep_going = True
            elif choice == '4':
                game.Game().exit_choice()
            else:
                print("Only 1-4 please!")

        if bot:
            while game_in_progress:
                if player_turn == 1:
                    player_won, reset = game.Game().turn(player1)
                    player_turn = 2

                    if player_won:
                        print(player1.name + " won!")
                        highscore.Highscore().add_highscore(
                            player1.rolls,
                            player1.name
                        )
                        print("Added rolls to highscore list")
                        game.Game().exit_choice()

                    if reset:
                        print("Reseting\n")
                        player1.clean_score()
                        player2.clean_score(difficulty)
                        player_turn = 1
                else:
                    player_won = game.Game().bot_turn(player2)
                    player_turn = 1

                    if player_won:
                        print(player2.name + " won!")
                        game.Game().exit_choice()

        else:
            while game_in_progress:
                if player_turn == 1:
                    player_won, reset = game.Game().turn(player1)
                    player_turn = 2

                    if player_won:
                        print(player1.name + " won!")
                        highscore.Highscore().add_highscore(
                            player1.rolls, player1.name
                        )
                        print("Added rolls to highscore list")
                        game.Game().exit_choice()

                    if reset:
                        print("Reseting\n")
                        player1.clean_score()
                        player2.clean_score()
                        player_turn = 1
                else:
                    player_won, reset = game.Game().turn(player2)
                    player_turn = 1

                    if player_won:
                        print(player2.name + " won!")
                        highscore.Highscore().add_highscore(
                            player2.rolls, player2.name
                        )
                        print("Added rolls to highscore list")
                        game.Game().exit_choice()

                    if reset:
                        print("Reseting\n")
                        player1.clean_score()
                        player2.clean_score()
                        player_turn = 1

    if __name__ == '__main__':
        main()
