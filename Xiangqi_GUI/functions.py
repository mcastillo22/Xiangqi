import pygame, sys
from pygame.locals import  *
from constants import *
from Xiangqi import *


def on_grid(x, y):
    """Checks that mouse has been clicked on an actual grid space on the gameboard"""
    for top_x in range(PIECE_POS0, SIZE[0] - PIECE_POS0, SQUARE_SPACE):
        for top_y in range(PIECE_POS0, SIZE[0] - PIECE_POS0 + SQUARE_SPACE, SQUARE_SPACE):
            box = pygame.Rect(top_x, top_y, ICON_SIZE, ICON_SIZE)
            if box.collidepoint(x, y):
                return [top_x, top_y]
    return [None, None]

def convert(board, x, y):
    """Converts screenboard grid to underlying board"""
    rank = board.index(y)
    rank = SWITCH.index(rank)
    fil = board.index(x)
    return [rank, fil]

def get_piece_pos(game, turn):
    """Get list of positions for the correct turn"""
    pieces = game.get_pieces(turn)
    pos = [p.get_position() for p in pieces]
    return pos

def get_center(x, y):
    """Returns the center coords from the top left and top right coords"""
    return x + SQUARE_SPACE // 2, y + SQUARE_SPACE // 2

def check_undo_button(game, x, y):
    button = pygame.Rect(X1, int(Y2 + SQUARE_SPACE * 1.25), BUTTON_SIZE, BUTTON_SIZE)
    if button.collidepoint(x, y):
        game.undo()

def display_status(screen, game, font_obj, action):
    text_obj = font_obj.render(action, True, WHITE)
    screen.blit(text_obj, (X1 + SQUARE_SPACE * 5, Y2 + SQUARE_SPACE // 2))
