# Tic Tac Toe in Pygame

## Overview
This project is a simple implementation of the Tic Tac Toe game using Python and the Pygame library. It features a graphical user interface, turn-based gameplay, and win/draw detection.

## Features
- Graphical representation of the game board.
- Turn-based gameplay between two players (X and O).
- Detection of win conditions (row, column, and diagonal matches).
- Draw detection when all cells are filled without a winner.
- Display of the number of wins for each player.
- Restarting the game by pressing the space bar.
- Smooth user interactions using mouse input.

## Prerequisites
To run this project, you need to have Python installed along with the Pygame library.

### Installation
1. Install Python (if not already installed):
   - Download and install from [Python's official website](https://www.python.org/downloads/)

2. Install Pygame:
   ```bash
   pip install pygame
   ```

## How to Run
1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-pygame.git
   cd tic-tac-toe-pygame
   ```
2. Run the script:
   ```bash
   python tic_tac_toe.py
   ```

## Gameplay Instructions
- The game starts with an empty 3x3 grid.
- Players take turns placing X and O by clicking on the cells.
- The first player to align three marks in a row, column, or diagonal wins.
- If the board is full without a winner, the game results in a draw.
- Press the `SPACE` key to restart the game after a win or a draw.
- Close the window to exit the game.

## Code Structure
- `SettingColors()`: Defines colors used in the game.
- `SettingWindow()`: Initializes the game window and fonts.
- `DrawingBoard()`: Draws the Tic Tac Toe board with lines and cells.
- `StartingWindow()`: Main game loop handling user input and gameplay mechanics.
- `endWin(result)`: Displays the winning message and updates scores.
- `endDraw(x, o)`: Displays the draw message.

## Future Improvements
- Add AI to play against a computer opponent.
- Implement a better UI with animations.
- Add a menu screen with game options.
- Track player statistics across multiple games.

## License
This project is open-source and available under the MIT License.

## Contributions
Feel free to fork the repository, create a new branch, and submit pull requests with improvements or bug fixes.


