import pygame, sys
from pygame.locals import  *
from constants import *


def highlight_piece(screen, position):
    circle = pygame.image.load('Images/circle.png')
    screen.blit(circle, (position[0] - 2, position[1] - 2))

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
