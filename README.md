Basic description of the program
-----------------------
This is a representation of a simple dice game called pig.
You can play against another player or a computer controlled opponent. This program also adds every players score to a textfile called "highscores".

The rules of the game are simple. You start with 0 points and take turns rolling a dice. You can keeping rolling the dice until you either roll a 1 or choose to hold. If you choose to hold, all your roles from that turn is added to your score, then it's the other players turn. If you roll a 1, you get none of the points from that turn, then it's the other players turn.
First to get to 100 points and hold wins.
When you get to 100 points the game will save your name and the amount of rolls you made that game to the high scores list. The more rolls you made, the further down on the list you get placed.
Don't worry, your score is kept if you change name mid-game.

This program is menu driven, every time you're able to take an action, you will be shown a menu of options and be prompted to choose.

For testing purposes, there is a cheat function. To use this function you need to be in-game at the place where the game prompts you to choose from a menu where you can roll, hold, reset and exit.
Instead of choosing any of these options, enter 0.
Now you're a cheater!

Computer opponent intelligence
-----------------------
The intelligence of this computer opponent is not really intelligence at all, it's just different levels of cheating.
You can choose from three different difficulties, easy, medium or hard.
Depending on what difficulty you choose, the computer opponent will start with 0, 20 or 40 points. Harder difficulty, means a bigger head start for the bot.

How to install and run the program
-----------------------
There are two ways of installing this game.

```
1. Clone the repository to a folder of your choice. Done!
```
```
2. Download the zip file and extract the contents to a folder of your choice. Done!
```

To run the game you can choose to either open the folder containing the project, open the folder called "game" and executing the "main.py" file. Or you can navigate to the folder containing the project in your terminal then enter the command below.

```
python game/main.py
```

Installation for testing purposes
-----------------------
Before you can test the program you will have to install a few things. While in your terminal, navigate to the folder containing the project. Then enter the command below.

```
make venv
```

This will install venv.

Then enter this command to activate venv.

```
# For Windows
. .venv/Scripts/activate
```

```
# For Mac and Linux
. .venv/bin/activate
```

Then enter this command to install everything from "requirements.txt".

```
make install
```

When you're done, enter this to stop using venv.

```
deactivate
```

IMPORTANT
Before testing, open the files "main.py" and "game.py" in any text editor. Make sure every import statement at the top has "from game" in front of it, except for "import sys" and "import time" in "game.py".
Whenever you want to run the program regularly, you have to remove the "from game" parts again.
This is a weird quirk I couldn't find a solution to.

Run the testsuite
-----------------------
Open the Makefile and find the command called "unittest". At the end of the command there should be some quotation marks. If you want to run all of the tests, make sure it says "*_test.py" between the quoteation marks. If you want to run part of the tests, type the name of the file containing the tests you want to run between the quotation marks.
Then enter the following command into the terminal.

```
make unittest
```

IMPORTANT
When the tests run, they might ask you to enter difficulty, enter 1, 2 or 3. They might also ask you to enter a name, this will happen twice, put a different name each time.

Get coverage
-----------------------
To get the tests coverage report, enter the following command into the terminal. This will also run all tests. Follow the instructions above.

```
make coverage
```

Then open it by entering this.
```
start htmlcov/index.html
```


Run the whole testsuite
-----------------------
To run the whole testsuite you can open the Makefile, find the command named "unittest", and make sure it says "*_test.py" between the quotation marks at the end. Then enter t

Documentation and UML
-----------------------
The easiest way to regenerate the documentation for this project is to use the command below in the terminal.

```
make doc
```
