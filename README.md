# Battleship Game

## Description
This Python project is a simple, text-based version of the classic game Battleship. The game is played against the computer in a 5x5 grid. Players take turns to guess the location of the enemy's ships and try to sink them all to win the game.

## Features
- Two boards: one for the player and one for the computer.
- Random placement of ships on the board.
- Turn-based gameplay allowing the player and the computer to guess ship locations.
- Real-time hit/miss feedback with each guess.
- Victory condition check after each turn.

## How to Play
1. Run the script in a Python environment.
2. Enter your name when prompted.

### During the Game
![During the Game](./images/gameon.png)

- You will see your board with your ships (marked as 'S') and the hits or misses.
- Enter the row and column numbers to hit a spot on the computer's board.
- The game will indicate whether it was a hit or a miss.
- The game ends when all ships on one board are sunk.

## Installation
No additional libraries are required to run this game. Just ensure you have Python installed on your system.

## Code Style and Linting Issues
While developing this game, we aimed to adhere to standard Python coding practices. However, you might encounter some style guide warnings if you run a linter on the code. These include:

- E302 expected 2 blank lines, found 1
- 6: E302 expected 2 blank lines, found 1
- 16: E302 expected 2 blank lines, found 1
- 33: E302 expected 2 blank lines, found 1
- 42: E302 expected 2 blank lines, found 1
- 55: E302 expected 2 blank lines, found 1
- 59: E305 expected 2 blank lines after class or function definition, found 1
- 83: E501 line too long (83 > 79 characters)

We plan to address these in future updates to better adhere to PEP 8 standards.

## Limitations
- The game currently does not have a graphical interface; it runs in the console.
- There is no difficulty level for the computer player; it makes random guesses.
- Board size and number of ships are fixed and cannot be changed in-game.

## Future Enhancements
- Adding a graphical user interface.
- Implementing adjustable difficulty levels.
- Allowing customizable board sizes and number of ships.

### Computer's Turn
![Computer's Turn](./images/computerplay.png)

### Game Over
![Game Over](./images/finish.png)
