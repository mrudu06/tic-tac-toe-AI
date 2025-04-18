# Python Tic Tac Toe Game

A command-line Tic Tac Toe game implemented in Python where players can choose between different opponent types including human players and AI with varying difficulty levels.

## Features

- Multiple player options:
  - Human player (for local 2-player games)
  - Random Computer player (makes random moves)
  - Smart Computer player (uses minimax algorithm - unbeatable)
- Score tracking system
- Simple command-line interface
- Customizable match-ups (human vs human, human vs AI, or AI vs AI)

## Project Files

The game consists of two main Python files:

1. `tictactoe.py` - Main game file containing:
   - `tictactoe` class for board management and game logic
   - `ScoreBoard` class for tracking scores
   - Main game loop and player selection

2. `player.py` - Contains player implementations:
   - `Player` - Base class for all player types
   - `HumanPlayer` - For human input
   - `RandomComputerPlayer` - Makes random moves
   - `SmartComputerPlayer` - Uses minimax algorithm for optimal play

## How to Play

1. Ensure you have Python installed on your system
2. Save both files (`tictactoe.py` and `player.py`) in the same directory
3. Run the game by executing:
   ```
   python tictactoe.py
   ```

### Game Instructions

1. When the game starts, you'll be prompted to choose player types for both X and O:
   - Enter `1` for Human Player
   - Enter `2` for Random Computer Player  
   - Enter `3` for Smart Computer Player

2. The board is numbered as follows:
   ```
   | 0 | 1 | 2 |
   | 3 | 4 | 5 |
   | 6 | 7 | 8 |
   ```

3. If playing as a human, enter a number (0-8) when prompted to make your move

4. The game continues until:
   - A player wins by getting three in a row (horizontally, vertically, or diagonally)
   - The board is full (resulting in a tie)

5. After each game, the score is updated and displayed
6. You'll be asked if you want to play again

## Game Intelligence Levels

- **Human Player**: Moves are based on player input
- **Random Computer**: Makes completely random moves from available positions
- **Smart Computer**: Uses the minimax algorithm to make optimal moves. This AI is unbeatable - at best, you can force a tie.

## Understanding the Minimax Implementation

The SmartComputerPlayer uses the minimax algorithm, a recursive decision-making algorithm that:
- Simulates all possible game states
- Evaluates each end state with a score
- Chooses the move that maximizes the player's score while assuming the opponent will play optimally

## Possible Improvements

1. Add difficulty levels to the smart AI by limiting search depth
2. Implement alpha-beta pruning to improve minimax performance
3. Add a graphical user interface
4. Allow custom board sizes
5. Add multiplayer functionality over network

## How to Contribute

Feel free to fork this project and enhance it with additional features. Some ideas:
- Implement the improvements listed above
- Add more AI strategies
- Create unit tests
- Improve the user interface

## License

This project is open source and available under the MIT License.