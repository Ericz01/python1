import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        # Initialize game variables
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create the board
        self.create_board()
        
        # Start the game loop
        self.window.mainloop()

    def create_board(self):
        """Create the game board with buttons."""
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.window, text=" ", font=("Arial", 20), height=2, width=5,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        """Handle a player's move."""
        if self.board[row][col] == " ":
            # Update board and button text
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            # Check for win or draw
            if self.check_winner():
                self.end_game(f"Player {self.current_player} wins!")
            elif self.is_draw():
                self.end_game("It's a draw!")
            else:
                # Switch to the other player
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "This cell is already taken!")

    def check_winner(self):
        """Check if the current player has won."""
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True
        
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        
        return False

    def is_draw(self):
        """Check if the game is a draw."""
        return all(cell in ['X', 'O'] for row in self.board for cell in row)

    def end_game(self, message):
        """Display the game result and reset the board."""
        messagebox.showinfo("Game Over", message)
        self.reset_board()

    def reset_board(self):
        """Reset the game board for a new game."""
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

# Run the game
if __name__ == "__main__":
    TicTacToe()