import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class ScoreBoard:
    def __init__(self):
        self.x_score = 0
        self.o_score = 0

    def update_score(self, winner):
        if winner == 'X':
            self.x_score += 1
        elif winner == 'O':
            self.o_score += 1

    def display_score(self):
        print(f"\nSCORE BOARD:")
        print(f"X Player: {self.x_score}")
        print(f"O Player: {self.o_score}\n")


class tictactoe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    def choose_player(letter):
        while True:
            choice = input(f'Select {letter} player (1: Human, 2: Random Computer, 3: Smart Computer): ')
            if choice == '1':
                return HumanPlayer(letter)
            elif choice == '2':
                return RandomComputerPlayer(letter)
            elif choice == '3':
                return SmartComputerPlayer(letter)
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

    print("Welcome to Tic Tac Toe!")
    score_board = ScoreBoard()
    
    while True:
        x_player = choose_player('X')
        o_player = choose_player('O')
        t = tictactoe()
        
        winner = play(t, x_player, o_player, print_game=True)
        if winner:
            score_board.update_score(winner)
        
        score_board.display_score()
        
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nFinal Scores:")
            score_board.display_score()
            print("Thanks for playing!")
            break