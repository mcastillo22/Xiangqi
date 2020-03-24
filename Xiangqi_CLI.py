from Xiangqi import XiangqiGame


def main():

    game = XiangqiGame()
    game.set_CLI_mode(True)
    print(' >> Xiangqi 2GO v1\n\tFormat moves as \'a1, a3\'. Red moves first.')
    game.print_board()
    print()

    running = True

    while running:
        print(game.get_turn().title() + ': ', end='')
        moves = input()
        moves = moves.replace(' ', '')
        end = moves.find(',')

        if end != -1:
            prev = moves[:end]
            new = moves[end+1:]
            game.make_move(prev, new)
            game.print_board()
            print()

if __name__ == '__main__':
    main()