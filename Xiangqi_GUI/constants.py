RED = "Red"
BLACK = "Black"

BG_RED = (201, 90, 0)
BOARD_YELLOW = (245, 172, 61)
BLACKCOLOR = (0, 0, 0)
GREEN = (59, 193, 74)
BLUE = (0, 0, 255)
REDCOLOR = (255, 0, 0)

SIZE = (504, 617)

SQUARE_SPACE = 53
X1, Y1 = 40, 40
X2, Y2 = X1 + SQUARE_SPACE * 8, Y1 + SQUARE_SPACE * 9
PX1 = X1 + SQUARE_SPACE * 3
PX2, PY2 = X1 + SQUARE_SPACE * 5, X1 + SQUARE_SPACE * 2
REDP_OFFSET = SQUARE_SPACE * 7  # For Red Palace

PIECE_POS0 = SQUARE_SPACE // 3 + 1
ICON_SIZE = 45

NAMES = {'R': 'Rook',
         'H': 'Horse',
         'E': 'Elephant',
         'A': 'Advisor',
         'G': 'General',
         'C': 'Cannon',
         'S': 'Soldier'}

SWITCH = [x for x in range(9,-1,-1)]