# Simple Chess Game in Python
class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.symbol = self.get_symbol()

    def get_symbol(self):
        symbols = {
            'K': '♔' if self.color == 'W' else '♚',
            'Q': '♕' if self.color == 'W' else '♛',
            'R': '♖' if self.color == 'W' else '♜',
            'B': '♗' if self.color == 'W' else '♝',
            'N': '♘' if self.color == 'W' else '♞',
            'P': '♙' if self.color == 'W' else '♟'
        }
        return symbols[self.name]

    def __str__(self):
        return self.symbol


class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.turn = 'W'

    def create_board(self):
        b = [[None] * 8 for _ in range(8)]
        for i in range(8):
            b[1][i] = Piece('P', 'B')
            b[6][i] = Piece('P', 'W')
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i, name in enumerate(pieces):
            b[0][i] = Piece(name, 'B')
            b[7][i] = Piece(name, 'W')
        return b

    def print_board(self):
        print("  a b c d e f g h")
        for i in range(8):
            print(8 - i, end=' ')
            for j in range(8):
                piece = self.board[i][j]
                print(str(piece) if piece else '.', end=' ')
            print(8 - i)
        print("  a b c d e f g h")

    def move(self, start, end):
        x1, y1 = 8 - int(start[1]), ord(start[0]) - ord('a')
        x2, y2 = 8 - int(end[1]), ord(end[0]) - ord('a')

        piece = self.board[x1][y1]
        if not piece:
            print("No piece at start.")
            return False
        if piece.color != self.turn:
            print(f"It's {self.turn}'s turn.")
            return False

        # Simplified: allow any move (not validating real rules here)
        self.board[x2][y2] = piece
        self.board[x1][y1] = None
        self.turn = 'B' if self.turn == 'W' else 'W'
        return True

    def play(self):
        while True:
            self.print_board()
            move = input(f"{self.turn}'s move (e.g., e2 e4): ")
            if move.lower() in ['exit', 'quit']:
                break
            try:
                start, end = move.strip().split()
                self.move(start, end)
            except:
                print("Invalid input. Try again.")


if __name__ == "__main__":
    game = ChessGame()
    game.play()
