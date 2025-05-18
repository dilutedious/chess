# pieces file

class Piece:
    def __init__(self, colour, symbol):
        self.colour = colour
        self.symbol = symbol

    def validate_move(self, start_pos, end_pos, board_object):
        pass

    def show(self):
        if self.colour == 'w':
            return self.symbol[0]
        else:
            return self.symbol[1]

# pawn piece

class Pawn(Piece):
    def __init__(self, colour):
        symbol = '♟♙'
        super().__init__(colour, symbol)

    def validate_move(self, start_pos, end_pos, board_object):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        if self.colour == 'w':
            direction = -1

        # (0,0) is the top left of the board, white moves down the numbers
        # similarly, black moves up colours, hence the direction.

        else:
            direction = 1
        row_diff = end_row - start_row
        col_diff = end_col - start_col
        if col_diff == 0 and row_diff == 1 * direction:
            if board_object.emptytile(end_pos):
                return True
            
        if abs(col_diff) == 1 and row_diff == 1 * direction:
            if board_object.is_opp_piece(end_pos, self.colour):
                return True

        # only returns false if none of the moves work.

        return False        
    
# rook piece

class Rook(Piece):
    def __init__(self, colour):
        symbol = '♜♖'
        super().__init__(colour, symbol)
    
    def validate_move(self, start_pos, end_pos, board_object):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # check if the movement is a straight line

        if start_row != end_row and start_col != end_col:
            return False
        
        if not board_object.path_clear(start_pos, end_pos, "horizontal/vertical"):
            return False
        
        if board_object.emptytile(end_pos) or board_object.is_opp_piece(end_pos, self.colour):
            return True
        
        return False
        
# knight piece

class Knight(Piece):
    def __init__(self, colour):
        symbol = "♞♘"
        super.__init__(colour, symbol)

    def validate_move(self, start_pos, end_pos, board_object):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # using absolute value - direction doesn't matter for knight

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        if (row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1):
            if board_object.emptytile(end_pos) or board_object.is_opp_piece(end_pos):
                return True
            
        return False
    
    # bishop piece

class Bishop(Piece):
    def __init__(self, colour):
        symbol = "♝♗"
        super().__init__(colour, symbol)

    def validate_move(self, start_pos, end_pos, board_object):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # direction doesn't matter for bishop.

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # check if move is diagonal; height = length if diagonal.

        if row_diff != col_diff:
            return False 
        
        if not board_object.path_clear(start_pos, end_pos, "diagonal"):
            return False
        
        if board_object.emptytile(end_pos) or board_object.is_opp_piece(end_pos):
            return True
        
        return False

# queen piece

class Queen(Piece):
    def __init__(self, colour):
        symbol = "♛♕"
        super().__init__(colour, symbol)

    def validate_move(self, start_pos, end_pos, board_object):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        is_straight = start_row is end_row or start_col is end_col
        is_diagonal = abs(start_col - end_col) is abs(start_row - end_row)

        if not (is_straight or is_diagonal):
            return False
        
        if is_straight:
            path_type = "horizontal/vertical"
        elif is_diagonal:
            path_type = "vertical"

        if not board_object.path_clear(start_pos, end_pos, path_type):
            return False
        
        if board_object.emptytile(end_pos) or board_object.is_opp_piece(end_pos, self.colour):
            return True
        
        return False

# King piece

class King(Piece):
    def __init__(self, colour):
        symbol = "♚♔"
        super().__init__(colour, symbol)

    def validate_move(self, start_pos, end_pos, board_object):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # using absolute value - direction doesn't matter for king

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # checkmate/check not implemented yet... king captured is sufficient enough.

        if row_diff <= 1 and col_diff <= 1 and not (row_diff == 0 and col_diff == 0):
            if board_object.emptytile(end_pos) or board_object.is_opp_piece(end_pos, self.colour):
                return True
            
        return False