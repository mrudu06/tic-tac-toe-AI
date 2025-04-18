import tkinter as tk
from tkinter import messagebox
from game import tictactoe
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = tictactoe()
        self.buttons = []
        self.current_player = 'X'
        
        # Player selection frame
        self.setup_frame = tk.Frame(root)
        self.setup_frame.pack(pady=10)
        
        # Create player selection dropdowns
        self.x_var = tk.StringVar(value="Human")
        self.o_var = tk.StringVar(value="Random Computer")
        
        tk.Label(self.setup_frame, text="X Player:").grid(row=0, column=0, padx=5)
        tk.OptionMenu(self.setup_frame, self.x_var, "Human", "Random Computer", "Smart Computer").grid(row=0, column=1)
        
        tk.Label(self.setup_frame, text="O Player:").grid(row=0, column=2, padx=5)
        tk.OptionMenu(self.setup_frame, self.o_var, "Human", "Random Computer", "Smart Computer").grid(row=0, column=3)
        
        # Game board frame
        self.board_frame = tk.Frame(root)
        self.board_frame.pack()
        
        # Create game board buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.board_frame, text="", width=10, height=3,
                                 command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)
        
        # Reset button
        tk.Button(root, text="New Game", command=self.reset_game).pack(pady=10)
        
        # Initialize players
        self.update_players()
    
    def update_players(self):
        player_map = {
            "Human": HumanPlayer,
            "Random Computer": RandomComputerPlayer,
            "Smart Computer": SmartComputerPlayer
        }
        self.x_player = player_map[self.x_var.get()]('X')
        self.o_player = player_map[self.o_var.get()]('O')
    
    def make_move(self, row, col):
        index = row * 3 + col
        current_player = self.x_player if self.current_player == 'X' else self.o_player
        
        # If it's a computer's turn, ignore human clicks
        if not isinstance(current_player, HumanPlayer):
            return
        
        if self.game.board[index] == ' ':
            # Make human move
            self.game.make_move(index, self.current_player)
            self.buttons[index].config(text=self.current_player)
            
            if not self.check_game_end():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.root.after(500, self.make_computer_move)  # Schedule computer move
    
    def make_computer_move(self):
        current_player = self.x_player if self.current_player == 'X' else self.o_player
        
        # If current player is computer, make its move
        if not isinstance(current_player, HumanPlayer):
            move = current_player.get_move(self.game)
            self.game.make_move(move, self.current_player)
            self.buttons[move].config(text=self.current_player)
            
            if not self.check_game_end():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                # If next player is also computer, schedule its move
                if not isinstance(self.x_player if self.current_player == 'X' else self.o_player, HumanPlayer):
                    self.root.after(500, self.make_computer_move)
    
    def check_game_end(self):
        last_move = -1
        for i, square in enumerate(self.game.board):
            if square == self.current_player:
                last_move = i
                break
                
        if self.game.winner(last_move, self.current_player):
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_game()
            return True
        elif not self.game.empty_squares():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return True
        return False
    
    def reset_game(self):
        self.game = tictactoe()
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text="")
        self.update_players()
        
        # If X player is computer, start its move
        if not isinstance(self.x_player, HumanPlayer):
            self.root.after(500, self.make_computer_move)

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = TicTacToeGUI(root)
    root.mainloop()