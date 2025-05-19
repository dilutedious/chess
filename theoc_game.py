# main gameloop

from ethanj_pieces import King, Queen, Bishop, Knight, Rook, Pawn
from julianc_board import Board
from williamk_ui import algebra_to_coordinates, coordinates_to_algebra, display_board, get_user_move, parse_move, message

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player_colour = "w"
        self.gameover = False
    
    def switch_player(self):
        if self.current_player_colour == 'w': self.current_player_colour = 'b'
        elif self.current_player_colour == 'b': self.current_player_colour = 'w'
    
    def run_game(self):
        while not self.gameover:
            display_board(self.board)
            message(f"{self.current_player_colour.upper()}'s turn")

            valid_input = False
            start_coords, end_coords = None, None
            piece_moved = None
            
            while not valid_input:
                move_input = get_user_move()
                
                parsed = parse_move(move_input)
                if parsed == None:
                    message("Invalid input format! Please use 'xn xn' format (e.g. e1 e2)")
                    continue
                start_algebra, end_algebra = parsed
                if start_algebra == None or end_algebra == None: # validation at each step
                    message("Invalid input format! Please use 'xn xn' format (e.g. e1 e2)")
                    continue
                
                start_coords = algebra_to_coordinates(start_algebra)
                end_coords = algebra_to_coordinates(end_algebra)
                if start_coords == None or end_coords == None: # more validation at every step
                    message("Invalid square notation! Please choose a square from a1 to h8.")
                    continue

                piece_moved = self.board.get_piece(start_coords)

                if piece_moved == None: # even more validation
                    message("No piece at starting square...")
                    continue
                elif piece_moved.colour != self.current_player_colour: #checks for your colour
                    message("Not your colour! Pick one of your own pieces.")
                    continue
                elif not piece_moved.validate_move(start_coords, end_coords, self.board):
                    message("Invalid move for that piece. Make sure you know how the pieces move.")
                    continue
                else:
                    captured_piece = self.board.get_piece(end_coords)
                    if captured_piece != None and captured_piece.colour == self.current_player_colour:
                        message("Cannot capture your own piece!")
                        continue
                    else:
                        valid_input = True
            
            captured_piece = self.board.get_piece(end_coords)
            self.board.move_piece(start_coords, end_coords) # note: double move for pawn's first not implemented yet
            
            if captured_piece != None:
                message(f"{piece_moved.show()} captures {captured_piece.show()}!")

                if captured_piece.symbol == "♚♔":
                    display_board(self.board)
                    message(f"Game over! {self.current_player_colour.upper()} wins!")
                    self.gameover = True
                    break
            
            if not self.gameover:
                self.switch_player()

# run the code:

chessgame = Game()
chessgame.run_game()