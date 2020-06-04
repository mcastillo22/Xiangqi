from Xiangqi import XiangqiGame


def main():

    game = XiangqiGame()
    game.set_CLI_mode(True)
    print(' >> Xiangqi 2GO v1')

    helper = input('\tTurn on helper mode? (Helper mode will display all legal moves for a piece) ')

    if helper.lower() in ['y', 'yes']:
        game.set_helper_mode(True)
        print("""\tHelper Mode turned on!
        Instructions:
        To see all possible moves of a piece, enter 'show' followed by the position of the piece.
        For example: 'show a1' will display a list of the moves the piece at a1 can perform.\n""")

    else:
        print('Helper mode is off.\n')

    print("Note: Please format moves as \'a1, a3\'. Red will go first.\n\t  Enter '0' or 'quit' anytime exit")
    game.print_board()
    print()

    running = True

    while running:
        if game.get_game_state() != 'UNFINISHED':
            replay = input('Play again? ')
            if replay.lower() in ['yes', 'y']:
                main()
            else:
                print('Thanks for playing!')
                running = False

        else:
            print(game.get_turn().title() + ': ', end='')
            moves = input()
            moves = moves.lower()

            if moves in ['0', 'quit', 'q']:
                print('Thanks for playing!')
                running = False

            else:
                h_move = moves.find('show')
                if h_move == -1:

                    moves = moves.replace(' ', '')
                    end = moves.find(',')

                    if end != -1:
                        prev = moves[:end]
                        new = moves[end+1:]
                        game.make_move(prev, new)
                        game.print_board()
                        print()

                elif h_move == 0:
                    end = moves.find(' ')
                    pos = game.convert(moves[end + 1:])

                    piece = game.get_piece_at_pos(pos)

                    if piece:
                        print('> ' + piece.get_name(piece.get_title()).title() + ' can move to ', end='')
                        print(game.hlpr_list_moves(pos))

                    else:
                        print('> There\'s no piece there!')

if __name__ == '__main__':
    main()