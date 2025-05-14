# pieces

class Piece:
    def __init__(self, colour, symbols):
        self.Colour = colour
        self.Symbol = symbols
        self.HasMoved = False

    def get_symbol(self):
        if self.Colour == 'w':
            return self.Symbol[1]
        elif self.Colour == 'b':
            return self.Symbol[0]

    def move_intent(startpos, endpos, capture):
        return NotImplementedError
    
    def slidingpiece():
        return False
    
class Pawn(Piece):
    def __init__(self, colour, symbols):
        super().__init__(colour, symbols = "♙♟")

    def 