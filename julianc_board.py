# board functions

from ethanj_pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = [[None for cols in range(8)] for rows in range(8)]
        self.setup()

    def setup(self):

        # rook setup

        self.grid[0][0] = Rook('b')
        self.grid[0][7] = Rook('b')
        self.grid[7][0] = Rook('w')
        self.grid[7][7] = Rook('w')

        # knight setup

        self.grid[0][1] = Knight('b')
        self.grid[0][6] = Knight('b')
        self.grid[7][1] = Knight('w')
        self.grid[7][6] = Knight('w')

        # bishop setup

        self.grid[0][2] = Bishop('b')
        self.grid[0][5] = Bishop('b')
        self.grid[7][2] = Bishop('w')
        self.grid[7][5] = Bishop('w')

        # queen setup

        self.grid[0][4] = Queen('b')
        self.grid[7][4] = Queen('w')
    
        # queen setup

        self.grid[0][3] = King('b')
        self.grid[7][3] = King('w')

        # pawn setup

        for col in range(0,7):
            self.grid[1][col] = Pawn('b')
            self.grid[6][col] = Pawn('w')

    def get_piece(self, pos):
        row, col = pos
        if self.validboardpos(pos):
            return self.grid[row][col]
        return None
    
    def set_piece(self, piece, pos):
        row, col = pos
        if self.validboardpos(pos):
            self.grid[row][col] = piece

    def move_piece(self, startpos, endpos):
        moving_piece = self.get_piece(startpos)
        captured_piece = self.get_piece(endpos)

        self.set_piece(moving_piece, endpos)
        self.set_piece(None, startpos)

        return captured_piece
    
    def validboardpos(self, pos):
        row, col = pos
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        else:
            return False
        
    def emptytile(self, pos):
        return self.get_piece(pos) is None

    def is_opp_piece(self, pos, current_colour):
        piece = self.get_piece(pos)
        if piece != None and piece.colour != current_colour:
            return True
        else:
            return False
        
    def path_clear(self, start_pos, end_pos, path_type):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if path_type == "horizontal/vertical":
            if start_row == end_row: # for horizontal moves
                if end_col > start_col:
                    step = 1
                else:
                    step = -1
                for column in range((start_col + step), (end_col) - step):
                    # checking for clear squares
                    if not self.emptytile(start_row, column):
                        return False
            else: # for vertical moves
                if end_row > start_row:
                    step = 1
                else:
                    step = -1
                for row in range((start_col + step), (end_row - step)):
                    if not self.emptytile(row, start_col):
                        return False
        
        elif path_type == "diagonal":
            if end_row > start_row:
                row_step = 1
            else:
                row_step = -1
            if end_col > start_col:
                col_step = 1
            else:
                col_step = -1
            current_row, current_col = start_row + row_step, start_col + col_step

            while (current_row, current_col) != end_pos:
                if not self.emptytile():
                    return False
                current_row += row_step
                current_col += col_step

            return True

    def get_king_pos(self, colour):
        for row in range(0,7):
            for col in range(0,7):
                piece = self.get_piece(row, col):
                if piece.show() == "♚" and colour == 'w':
                    return (row, col)
                elif piece.show() == "♔" and colour == 'b':
                    return (row, col)
        return None

board = Board()
board.setup()
