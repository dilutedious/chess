# user interface

# coordinate systems: using chess algebraic notation e.g. a8 = (0,0)

# translating chess algebra to coords

def algebra_to_coordinates(algebra_str):
    letters = "abcdefgh" # used to find index in string
    numbers = "12345678"
    if len(algebra_str) != 2: return None # can put things on the same line for simplicity
    file = algebra_str[0].lower()
    rank = algebra_str[1]
    if file not in "abcdefgh" and rank not in "12345678": return None
    
    col = letters.find(file)
    row = numbers.find(rank)

    return (row, col)

# translating coords to chess algebra

def coordinates_to_algebra(coordinates):
    letters = "abcdefgh" # used to find index in string
    numbers = "12345678"
    row, col = coordinates
    file = letters[col]
    rank = numbers[row]
    return file + rank

def display_board(board_object):
    print("    a b c d e f g h\n    - - - - - - - -")
    for row in range(0,8):
        line_printed = str(8 - row) + " |" # row label counts down from 8 to 1
        for col in range(0,8):
            piece = board_object.get_piece((row, col))
            if piece == None:
                if (row + col) % 2 == 0: line_printed += " ■" # checks if white or black square by certain diagonals only
                else: line_printed += " □"
            else:
                line_printed += " " + str(piece.show())
        print(line_printed + " | " + str(8 - row))
    print("    - - - - - - - -\n    a b c d e f g h")

def get_user_move():
    input_move = input("Enter your move: (e.g. 'e2 e4')")
    return input_move.strip().lower() # makes it interpretable for the program

def parse_move(user_move):
    parsed = user_move.split()
    if len(parsed) == 2: # validation step 1
        start_algebraic = parsed[0]
        end_algebraic = parsed[1]
        if len(start_algebraic) == 2 and len(end_algebraic) == 2: # validation step 2
            return start_algebraic, end_algebraic
    return None

def message(message):
    print(message)