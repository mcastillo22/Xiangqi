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

def highlight_piece(screen, position):
    circle = pygame.image.load('Images/circle.png')
    screen.blit(circle, (position[0] - 2, position[1] - 2))

def highlight_on():
    return True

def draw_dot(screen, position):
    center_pos = position[0] + SQUARE_SPACE // 2 - 3, position[1] + SQUARE_SPACE // 2 - 3
    pygame.draw.circle(screen, GREEN, center_pos, 5, 0)

def display_moves(screen, game, board, position):
    moves = game.get_helper_moves(position)
    gameboard_moves = [(board[h[1]], board[SWITCH[h[0]]]) for h in moves]

    if game.get_debug_mode():
        print(moves)
        print(gameboard_moves)

    for move in gameboard_moves:
        draw_dot(screen, move)
    
