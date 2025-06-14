class TicTacToe:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
        self.moves = 0

    def play(self, row: int, col: int) -> str:
        if self.winner:
            return f"Game over. Player {self.winner} has already won."

        if self.board[row][col] != "":
            return "Field already taken."

        self.board[row][col] = self.current_player
        self.moves += 1

        if self.check_winner(row, col):
            self.winner = self.current_player
            return f"Player {self.current_player} wins!"

        if self.moves == 9:
            return "Draw!"

        self.current_player = "O" if self.current_player == "X" else "X"
        return "Next move."

    def check_winner(self, row: int, col: int) -> bool:
        symbol = self.board[row][col]

        # Linha
        if all(self.board[row][i] == symbol for i in range(3)):
            return True

        # Coluna
        if all(self.board[i][col] == symbol for i in range(3)):
            return True

        # Diagonal principal
        if row == col and all(self.board[i][i] == symbol for i in range(3)):
            return True

        # Diagonal secundária
        if row + col == 2 and all(self.board[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def print_board(self):
        for row in self.board:
            print(" | ".join(cell if cell else "_" for cell in row))
        print()
