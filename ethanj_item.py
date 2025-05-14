# pieces

class Piece:
    def __init__(self, colour, symbol):
        self.Colour = colour
        self.Symbol = symbol
        self.HasMoved = False

    def get_symbol(self):
        if self.Colour == 'w':
            