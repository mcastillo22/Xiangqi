import pygame, sys
from pygame.locals import  *
from constants import *

# For screen gameboard:
def draw_gameboard(screen):
    """Draw gameboard outline"""

    def draw_func(start, end, size):
        pygame.draw.line(screen, BLACKCOLOR, [start[0], start[1]], [end[0], end[1]], size)

    def draw_borders():
        """Draw game borders"""

        border = {
            'left'  : ((X1, Y1), (X1, Y2)),
            'top'   : ((X1, Y1), (X2, Y1)),
            'right' : ((X2, Y1), (X2, Y2)),
            'bottom': ((X1, Y2), (X2, Y2))
        }

        for coords in border.values():
            draw_func(coords[0], coords[1], 4)

    def draw_ranks():
        """Draw rank (row) lines"""
        for y in range(SQUARE_SPACE + Y1, Y2-1, SQUARE_SPACE):
            pygame.draw.line(screen, BLACKCOLOR, [X1, y], [X2, y], 1)

    def draw_files():
        """Draw files (columns) lines"""
        for x in range(SQUARE_SPACE + Y1, X2-1, SQUARE_SPACE):
            pygame.draw.line(screen, BLACKCOLOR, [x, Y1], [x, Y1 + 4 * SQUARE_SPACE], 1)
            pygame.draw.line(screen, BLACKCOLOR, [x, PX2], [x, Y2], 1)

    def draw_palace():
        """Draw palace lines"""

        palace = {
            'r1': ((PX1, Y1), (PX2, PY2)),
            'r2': ((PX2, Y1), (PX1, PY2)),
            'b1': ((PX1, Y1 + REDP_OFFSET), (PX2, PY2 + REDP_OFFSET)),
            'b2': ((PX2, Y1 + REDP_OFFSET), (PX1, PY2 + REDP_OFFSET))
        }

        for coords in palace.values():
            draw_func(coords[0], coords[1], 1)

    screen.fill(BG_RED)
    pygame.draw.rect(screen, BOARD_YELLOW, (X1, Y1, SQUARE_SPACE * 8, SQUARE_SPACE * 9))
    pygame.draw.rect(screen, BLUE, (X1, Y1 + SQUARE_SPACE * 4, SQUARE_SPACE * 8, SQUARE_SPACE))
    draw_borders()
    draw_ranks()
    draw_files()
    draw_palace()

def load_images(color):
    """Load all piece images"""
    def define_path(color, piece):
        return f'Images/{color}/{piece}.png'

    def load(path):
        return pygame.image.load(path)

    pieces = {color + '_' + piece: None for piece in NAMES.values()}

    for piece in pieces.keys():
        path = define_path(color, piece)
        pieces[piece] = load(path)

    return pieces

def blit_pieces(screen, piecelist, icons, red):
    """Place piece on board"""
    def get_info(piece, prefix):
        name = piece.get_type()
        row, col = tuple(piece.get_position())
        fullpiece = icons[prefix + name]
        return name, row, col, fullpiece

    if red:
        prefix = RED + '_'
        n = 1
    else:
        prefix = BLACK + '_'
        n = 0

    for piece in piecelist:
        name, row, col, fullpiece = get_info(piece, prefix)
        row = SWITCH.index(row)
        coord = PIECE_POS0 + SQUARE_SPACE * col, PIECE_POS0 + SQUARE_SPACE * row
        screen.blit(fullpiece, coord)

def place_pieces(screen, red, black):
    """Loads and places icons on board in their proper position"""
    red_icons = load_images(RED)
    black_icons = load_images(BLACK)
    
    blit_pieces(screen, red, red_icons, True)
    blit_pieces(screen, black, black_icons, False)

def display_turn(screen, font_obj, turn):
    turn_text = font_obj.render(f'Turn: {turn.title()}', True, WHITE)
    screen.blit(turn_text, (X1, TEXT_Y))

def display_buttons(screen, game):
    if game.get_turn_num() > 0:
        create_new_game_button(screen, game)
        if game._temp is not None:
            create_undo_button(screen, game)

def create_undo_button(screen, game):
    undo = pygame.image.load('Images/undo.png')
    screen.blit(undo, (X1, BUTTONS_Y))

def create_new_game_button(screen, game):
    ng = pygame.image.load('Images/play.png')
    screen.blit(ng, (TEXT2_X, BUTTONS_Y))
