import pygame, sys
from pygame.locals import  *
from constants import *
from Xiangqi import *

def on_grid(x, y):
    """Checks that mouse has been clicked on an actual grid space on the gameboard"""
    for top_x in range(PIECE_POS0, SIZE[0] - PIECE_POS0, SQUARE_SPACE):
        for top_y in range(PIECE_POS0, SIZE[1] - PIECE_POS0, SQUARE_SPACE):
            box = pygame.Rect(top_x, top_y, ICON_SIZE, ICON_SIZE)
            if box.collidepoint(x, y):
                return [top_x, top_y]
    return [None, None]

def convert(board, x, y):
    """Converts screenboard grid to underlying board"""
    row = board.index(y)
    row = SWITCH.index(row)
    col = board.index(x)
    return [row, col]

def get_piece_pos(game, turn):
    """Get list of positions for the correct turn"""
    pieces = game.get_pieces(turn)
    pos = [p.get_position() for p in pieces]
    return pos

def get_center(x, y):
    return x + ICON_SIZE // 2 + 1, y + ICON_SIZE // 2 + 1

def highlight_piece(screen, position):
    pygame.draw.circle(screen, BLACKCOLOR, position, int(ICON_SIZE // 1.55), 0)

def highlight_on():
    return True
