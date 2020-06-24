import pygame, sys
from pygame.locals import  *
from constants import *
from Xiangqi import XiangqiGame

# For underlying board
def create_board():
    """Creates initial underlying board array"""
    return [x for x in range(PIECE_POS0, SIZE[0], SQUARE_SPACE)]

def create_new_game():
    """Creates new game object"""
    new_obj = XiangqiGame()
    new_obj.set_helper_mode(True)
    new_obj.set_debug_mode(False)
    
    return new_obj
