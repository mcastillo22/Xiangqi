import pygame, sys
from pygame.locals import  * 

from constants import *
from setup import *
from visual_setup import *
from functions import *
from highlight_function import *

from Xiangqi import *


def main():
    """
    Version 1.7
    An object of a text-based game of Xiangqi- a battle between two armies with the goal of capturing the enemy's
    general. A river separates the two armies, and affects Piece movement. Generals and Advisors are limited to their
    respective palace. This game is also known as Chinese Chess.

    Players take turns moving one piece of their army at a time using algebraic notation.
    Red player goes first.
    Moves cannot be made that leave the two Generals directly facing one another (no pieces in between)
    In general, pieces capture pieces of the opposing army by moving to their position.
    Winning involves checkmating the opposing camp. Stalemates can also occur.

    This version allows movement based only on algebraic notation.
    This version does not implement perpetual check or chasing.
    This version uses 'ranks' to refer to rows, and 'files' to refer to columns.
    """

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Xiangqi')
    font_obj = pygame.font.SysFont('Calibri', 28)

    BOARD = create_board()

    pos1, pos2 = None, None
    coordx, coordy = None, None

    highlight = False
    highlighted_piece = None

    GAME = create_new_game()
    running = True
    
    while running:

        # Draw gameboard grid and buttons
        draw_gameboard(screen)
        display_buttons(screen, GAME)

        # Highlight active piece
        if highlight:
            highlight_piece(screen, highlighted_piece)
        
        # Show icons in proper positions
        red_pieces = GAME.get_pieces(RED.lower())
        black_pieces = GAME.get_pieces(BLACK.lower())
        place_pieces(screen, red_pieces, black_pieces)

        # Show available moves for active piece
        if highlight and pos1 is not None:
            display_moves(screen, GAME, BOARD, pos1)

        # Display the current player whose turn it is
        turn = GAME.get_turn()
        display_turn(screen, font_obj, turn)

        # Display game status (player in check, player won, etc.)
        if GAME.get_status() is not False:
            display_status(screen, GAME, font_obj, GAME.get_status())        
            if GAME.get_game_state() != 'UNFINISHED':
                turn = None
                highlight = False

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos

                    check_undo_button(GAME, mouse_x, mouse_y)
                    if check_new_game(GAME, mouse_x, mouse_y):
                        GAME = create_new_game()

                    coordx, coordy = on_grid(mouse_x, mouse_y)
                    in_board = coordx is not None and coordy is not None

                    if pos1 is None and in_board:
                        pos1 = convert(BOARD, coordx, coordy)

                        # Highlight piece if it is the right turn
                        if pos1 in get_piece_pos(GAME, turn):
                            highlight = True
                            highlighted_piece = coordx, coordy
                        
                        else:
                            pos1 = None

                    else:
                        if pos1 == pos2:
                            pos1, pos2 = None, None
                            highlight = False
                        
                        elif in_board:
                            pos2 = convert(BOARD, coordx, coordy)

                            if pos2 in get_piece_pos(GAME, turn):
                                pos1, pos2 = pos2, None
                                highlighted_piece = coordx, coordy

                            else:
                                GAME.make_temp()
                                GAME.make_move(pos1, pos2)
                                
                                pos1, pos2 = None, None
                                highlight = False
                        
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
