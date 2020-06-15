import pygame, sys
from pygame.locals import  * 

from constants import *
from setup import *
from functions import *

from Xiangqi import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Xiangqi')

    BOARD = create_board()

    pos1 = None
    pos2 = None

    debugmode = True
    highlight = False
    center_coords = None

    game = XiangqiGame()
    running = True
    
    while running:

        # Show icons in proper positions
        draw_gameboard(screen)
        if highlight:
            highlight_piece(screen, center_coords)
        red_pieces = game.get_pieces(RED.lower())
        black_pieces = game.get_pieces(BLACK.lower())
        place_pieces(screen, red_pieces, black_pieces)

        turn = game.get_turn()

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    coordx, coordy = on_grid(mouse_x, mouse_y)
                    if pos1 is None:
                        pos1 = convert(BOARD, coordx, coordy)

                        # Highlight piece if it is the right turn
                        if pos1 in get_piece_pos(game, turn):
                            highlight = highlight_on()
                            center_coords = get_center(coordx, coordy)
                            highlight_piece(screen, center_coords)
                    
                    else:
                        pos2 = convert(BOARD, coordx, coordy)

                        if debugmode:
                            print(pos1, pos2)
                            print(game.make_move(pos1, pos2))
                        
                        pos1 = None
                        pos2 = None
                        highlight = False
    

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
