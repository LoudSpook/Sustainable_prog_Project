"""Handle highscores."""

import os

class Highscore():
    """Handle the class."""

    def __init__(self):
        """Initiate object."""

    def add_highscore(self, rolls, name):
        last = True

        with open(r'C:\Users\adamh\Desktop\Sustainable_prog_Project\game\highscores.txt', 'r') as file:
            content = file.readlines()

        for line in content:
            index = content.index(line)
            if index % 2 != 0:
                int_line = int(line)
                if int_line > rolls:
                    rolls = str(rolls)
                    rolls += "\n"
                    name += "\n"

                    content.insert(index - 1, name)
                    content.insert(index, rolls)
                    file.close()
                    last = False
                    break
                
        if last:
            rolls = str(rolls)
            rolls += "\n"
            name += "\n"

            content.insert(index + 1, name)
            content.insert(index + 2, rolls)

        with open('highscores.txt', 'w') as file:
            content = "".join(content)
            file.write(content)

        file.close()
