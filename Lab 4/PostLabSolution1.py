import os, random
import oxo

class Game:
    """This class represents a Tic-tac-toe game."""

    def __init__(self):
        """Initialize a new game with an empty board."""
        self.board = [" "] * 9

    @staticmethod
    def new_game():
        """Return a new empty game."""
        return [" "] * 9

    def save_game(self):
        """Save the current game to disk."""
        oxo.save_game(self.board)

    def restore_game():
        """Restore the previously saved game.
        If the game cannot be restored, return a new game."""
        try:
            board = oxo.restore_game()
            if len(board) == 9:
                return board
            else:
                return Game.new_game()
        except IOError:
            return Game.new_game()

    def generate_move(self, board):
        """Generate a random move from the available cells.
        If all cells are used, return -1."""
        options = [i for i in range(len(board)) if board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def is_winning_move(self, board):
        """Check if the current board has a winning move."""
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = board[a] + board[b] + board[c]
            if chars == "XXX" or chars == "OOO":
                return True
        return False

    def user_move(self, cell):
        """Make a user move on the given cell.
        If the cell is not empty, raise a ValueError.
        If the move results in a winning line, return the result.
        Otherwise, return an empty string."""
        if self.board[cell] != " ":
            raise ValueError("Invalid cell")
        else:
            self.board[cell] = "X"
        if self.is_winning_move(self.board):
            return "X"
        else:
            return ""

    def computer_move(self):
        """Make a computer move on a random available cell.
        If all cells are used, return 'D'.
        If the move results in a winning line, return 'O'.
        Otherwise, return an empty string."""
        cell = self.generate_move(self.board)
        if cell == -1:
            return "D"
        self.board[cell] = "O"
        if self.is_winning_move(self.board):
            return "O"
        else:
            return ""

    def test(self):
        result = ""
        while not result:
            print("-------------")
            print(f"| {self.board[0]} {self.board[1]} {self.board[2]} |")
            print(f"| {self.board[3]} {self.board[4]} {self.board[5]} |")
            print(f"| {self.board[6]} {self.board[7]} {self.board[8]} |")
            print("-------------")
            try:
                cell = int(input("Enter your move (0-8): "))
                if self.board[cell] != " ":
                    raise ValueError("Invalid cell")
                result = self.user_move(cell)
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()

            if not result:
                continue
            elif result == "D":
                print("It's a draw")
                print("-------------")
                print(f"| {self.board[0]} {self.board[1]} {self.board[2]} |")
                print(f"| {self.board[3]} {self.board[4]} {self.board[5]} |")
                print(f"| {self.board[6]} {self.board[7]} {self.board[8]} |")
                print("-------------")
            else:
                print(f"Winner is: {result}")
                print("-------------")
                print(f"| {self.board[0]} {self.board[1]} {self.board[2]} |")
                print(f"| {self.board[3]} {self.board[4]} {self.board[5]} |")
                print(f"| {self.board[6]} {self.board[7]} {self.board[8]} |")
                print("-------------")

if __name__ == "__main__":
    game = Game()
    game.test()