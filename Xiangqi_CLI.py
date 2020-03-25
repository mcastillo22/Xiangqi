from Xiangqi import XiangqiGame


def main():

    game = XiangqiGame()
    game.set_CLI_mode(True)
    print(' >> Xiangqi 2GO v1')
    helper = input('\tTurn on helper mode? ')

    if helper.lower() in ['y', 'yes']:
        game.set_helper_mode(True)
        print("""\tHelper Mode turned on!
        Instructions:
        To see all possible moves of a piece, enter 'show' followed by the position of the piece.
        For example: 'show a1' will display a list of the moves the piece at a1 can perform.\n""")

    print("Note: Please format moves as \'a1, a3\'. Red will go first.\nEnter '0' or 'quit' to exit")
    game.print_board()
    print()

    running = True

    while running:
        print(game.get_turn().title() + ': ', end='')
        moves = input()
        moves = moves.lower()

        if moves in ['0', 'quit', 'q']:
            print('Thanks for playing!')
            running = False

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
            piece = [p for p in game.get_pieces(game.get_turn()) if p.get_position() == pos]

            if piece:
                print('> ' + piece[0].get_name(piece[0].get_title()).title() + ' can move to ', end='')
                game.hlpr_list_moves(pos)

            else:
                print("> There's no piece there!")

if __name__ == '__main__':
    main()