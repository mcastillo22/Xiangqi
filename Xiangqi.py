# Author: Marissa Castillo
# Date: 02/22/2020
# Description: A text-based program of the game Xiangqi- a battle between two armies with the goal of capturing the
#              enemy's general.


from XiangqiPieces import Piece, General, Advisor, Elephant, Horse, Rook, Cannon, Soldier


class XiangqiGame:
    """
    Version 1.0
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

    def __init__(self):
        """Initialize game state, checkmate status, turn, captured pieces, playing pieces, and board"""

        self._game_state = 'UNFINISHED'
        self._turn = 0
        self._captured_pieces = []
        self._board = [[Piece() for file in range(9)] for rank in range(10)]

        # Initialize Red pieces
        self._RR1 = Rook(' R ', 'red', [0, 0])
        self._RR2 = Rook(' R ', 'red', [0, 8])
        self._RH1 = Horse(' H ', 'red', [0, 1])
        self._RH2 = Horse(' H ', 'red', [0, 7])
        self._RE1 = Elephant(' E ', 'red', [0, 2])
        self._RE2 = Elephant(' E ', 'red', [0, 6])
        self._RA1 = Advisor(' A ', 'red', [0, 3])
        self._RA2 = Advisor(' A ', 'red', [0, 5])
        self._RG = General(' G ', 'red', [0, 4])
        self._RC1 = Cannon(' C ', 'red', [2, 1])
        self._RC2 = Cannon(' C ', 'red', [2, 7])
        self._RS1 = Soldier(' S ', 'red', [3, 0])
        self._RS2 = Soldier(' S ', 'red', [3, 2])
        self._RS3 = Soldier(' S ', 'red', [3, 4])
        self._RS4 = Soldier(' S ', 'red', [3, 6])
        self._RS5 = Soldier(' S ', 'red', [3, 8])

        # Initialize Black pieces
        self._BR1 = Rook(' R ', 'black', [9, 0])
        self._BR2 = Rook(' R ', 'black', [9, 8])
        self._BH1 = Horse(' H ', 'black', [9, 1])
        self._BH2 = Horse(' H ', 'black', [9, 7])
        self._BE1 = Elephant(' E ', 'black', [9, 2])
        self._BE2 = Elephant(' E ', 'black', [9, 6])
        self._BA1 = Advisor(' A ', 'black', [9, 3])
        self._BA2 = Advisor(' A ', 'black', [9, 5])
        self._BG = General(' G ', 'black', [9, 4])
        self._BC1 = Cannon(' C ', 'black', [7, 1])
        self._BC2 = Cannon(' C ', 'black', [7, 7])
        self._BS2 = Soldier(' S ', 'black', [6, 2])
        self._BS3 = Soldier(' S ', 'black', [6, 4])
        self._BS4 = Soldier(' S ', 'black', [6, 6])
        self._BS5 = Soldier(' S ', 'black', [6, 8])
        self._BS1 = Soldier(' S ', 'black', [6, 0])

        self._pieces = [self._RR1, self._RR2, self._RH1, self._RH2, self._RE1, self._RE2,
                        self._RA1, self._RA2, self._RG, self._RC1, self._RC2,
                        self._RS1, self._RS2, self._RS3, self._RS4, self._RS5,
                        self._BR1, self._BR2, self._BH1, self._BH2, self._BE1, self._BE2,
                        self._BA1, self._BA2, self._BG, self._BC1, self._BC2,
                        self._BS1, self._BS2, self._BS3, self._BS4, self._BS5]

        # Place pieces on board
        for piece in self._pieces:
            rank = piece.get_position()[0]
            file = piece.get_position()[1]
            self._board[rank][file] = piece

        # Modes:
        self._CLI_mode = False
        self._helper_mode = False

        self._debug_mode = False
        self._bcheck = False
        self._rcheck = False

    def set_CLI_mode(self, cbool):
        self._CLI_mode = cbool

    def set_helper_mode(self, hbool):
        self._helper_mode = hbool

    def set_debug_mode(self, dbool):
        self._debug_mode = dbool

    def add_turn(self):
        """Adds a single turn to the game."""
        self._turn += 1

    def get_turn(self):
        """Returns the player whose turn it is."""

        # Because Red begins, even turns are Red moves
        if self._turn % 2 == 0:
            return 'red'
        else:
            return 'black'

    def get_pieces(self, color=None):
        """Returns a list of pieces that are in play in the board.
        (This means that captured pieces are no longer included)."""

        pieces = self._pieces

        if color == 'red':
            pieces = [piece for piece in self._pieces if piece.get_color() == 'red']

        elif color == 'black':
            pieces = [piece for piece in self._pieces if piece.get_color() == 'black']

        return pieces

    def update_game_state(self, player):
        """Updates game state: 'UNFINISHED'; 'RED_WON' or 'BLACK_WON' if there is a checkmate."""

        self._game_state = player.upper() + '_WON'
        return True

    def get_game_state(self):
        """Returns game state: 'UNFINISHED'; 'RED_WON' or 'BLACK_WON' if there is a checkmate."""
        return self._game_state

    def is_in_check(self, player):
        """Determines if a player is in check.
        This means the General is in a position that allows them to be captured"""

        if player == 'red':
            opposing = 'black'
        else:
            opposing = 'red'

        # Get player's General's position
        gen_position = [gen.get_position() for gen in self.get_pieces(player) if gen.get_title()[1] == 'G']
        gen_position = gen_position[0]

        # Get all opposing pieces in play
        opposing_moves = [om.get_position() for om in self.get_pieces(opposing)]

        # Determine if opposing pieces can capture the General
        captures_gen = [self.check_move(piece, gen_position) for piece in opposing_moves]

        if True in captures_gen:
            return True
        else:
            return False

    def check_move(self, piece_position, target_position):
        """Used by the is_in_check and check_for_checkmate_stalemate methods to determine the validity of
        hypothetical moves. Takes two strings as two positions ('piece_position' moves to 'target_position')
        and checks the validity of the proposed move."""

        # Check out of bounds
        if (0 <= target_position[0] < 10) and (0 <= target_position[1] < 9):

            # Check target position does not have a piece of the same army
            moving_piece = self._board[piece_position[0]][piece_position[1]]
            if self._board[target_position[0]][target_position[1]].get_color() != moving_piece.get_color():

                temp = moving_piece.get_position()

                # Determine if move is valid based on piece's own specific rules
                valid = moving_piece.move(target_position, self.get_pieces())

                # Return to original position
                moving_piece.update_position(temp)

                return valid

            else:
                return False

        else:
            return False

    def check_for_checkmate_stalemate(self, player):
        """Checks to see if there are any valid moves left. If there are, see if there are moves that take their
        General out of check for all active pieces of the given player"""

        # Get a dictionary of active pieces, their position, and their possible movesets
        #   Dictionary is solely for debugging purposes
        pieces = [[piece, piece.get_position(), piece.get_moves()] for piece in self.get_pieces(player)]

        # Check that for each of the player's active pieces, it has legal moves
        checkmate_results = {}
        stalemate_results = []
        for piece in pieces:

            # If piece has available moves
            if piece[2] is not None:
                checkmate_results[str(piece[1])] = []

                # Iterate through each potential move
                for i in range(len(piece[2])-1):
                    temp = piece[1]

                    # If move is valid, check if player is in check
                    if self.check_move(piece[1], piece[2][i]):
                        piece[0].update_position(piece[2][i])
                        in_check = self.is_in_check(player)
                        piece[0].update_position(temp)

                        # If a valid move has been found that does not result in check, return False
                        if not in_check:
                            checkmate_results[str(piece[1])].append(piece[2][i])
                            checkmate_results[str(piece[1])].append(in_check)
                            return False

                        # If valid move, but leads to a check, add False to stalemate
                        stalemate_results.append(False)

                    else:
                        stalemate_results.append(None)

        # If in check, check if opposing piece can be captured
        if self.opposing_can_be_captured(player):
            return False

        # If a valid move is found, stalemate did not occur
        if True in stalemate_results:
            return False

        # Otherwise, return True
        return True

    def opposing_can_be_captured(self, player):
        """If a player is in check, this method determines if a move can be made to capture the attacking piece(s)."""

        # Get General and its position
        general = [gen for gen in self.get_pieces(player) if gen.get_title()[1] == 'G']
        general = general[0]
        gen_pos = general.get_position()

        # Check if attacking piece/pieces can be taken
        #   Get opposing color
        if player == 'red':
            opposing = 'black'
        else:
            opposing = 'red'

        #   Get all opposing pieces in play
        opposing_moves = [op.get_position() for op in self.get_pieces(opposing)]

        #   Determine what opposing pieces can capture the General
        attacking_pieces_pos = [piece for piece in opposing_moves if self.check_move(piece, gen_pos)]
        defending_pieces_pos = [piece.get_position() for piece in self.get_pieces(player)]

        #   Determine if those attacking pieces can be captured
        for atck_piece in attacking_pieces_pos:
            for dfd_piece in defending_pieces_pos:

                # If valid, not a checkmate or stalemate
                if self.check_move(dfd_piece, atck_piece):
                    return True

        return False

    def convert(self, board_position):
        """Helper function to convert given board position (file, rank) to numerical value [rank, file]
        Input columns are letters a-i, and input rows are numbers 1-10.

        For example: 'a1' is equivalent to [0][0]; 'e10' is [9][4]"""

        # Convert input to  position on board
        conversion_alpha = 'abcdefghi'

        if 2 <= len(board_position) <= 3 and board_position[0] in conversion_alpha:

            # Check if rank is valid:
            if len(board_position) > 2:
                if int(board_position[2]) != 0 or int(board_position[1]) > 1:
                    return False

            file = conversion_alpha.index(board_position[0])
            rank = int(board_position[1:]) - 1

            return [rank, file]

        else:
            return False

    def make_move(self, current, new):
        """Takes two strings as two positions ('current' moves to 'new') and checks the validity of the proposed move"""

        if self.get_game_state() == 'UNFINISHED':

            # Convert current position to numerical version
            current_pos = self.convert(current)

            # If position is out of bounds, return False
            if current_pos is False:
                return False

            # Get piece to be moved
            moving_piece = self._board[current_pos[0]][current_pos[1]]

            if moving_piece.get_color() is None:
                return False

            # Validate that the moving piece matches whose turn it is
            if self.get_turn() == moving_piece.get_color() or self._debug_mode is True:

                # Convert desired position to numerical version
                new_pos = self.convert(new)

                # If position is out of bounds, return False
                if new_pos is False:
                    return False

                # Get piece in desired spot
                piece_in_new_spot = self._board[new_pos[0]][new_pos[1]]

                # Determine if piece in target position belongs to same army (cannot capture own army)
                if piece_in_new_spot.get_color() == moving_piece.get_color():
                    return False

                # Determine if move is valid based on piece's own specific rules
                movement_status = moving_piece.move(new_pos, self.get_pieces())

                if movement_status:

                    # Determine if a piece is captured
                    capture_move = piece_in_new_spot.get_color() != moving_piece.get_color() \
                               and piece_in_new_spot.get_color() is not None

                    if capture_move:

                        if self._CLI_mode:
                            print(moving_piece.get_name(moving_piece.get_title()) + ' captures '
                                  + (piece_in_new_spot.get_name(piece_in_new_spot.get_title())) + '!')

                        # If opposing General is captured:
                        if piece_in_new_spot.get_title() == 'G':
                            self.update_game_state(self.get_turn())

                        # Add captured piece to captured pieces list
                        self._captured_pieces.append(piece_in_new_spot)
                        # Update captured piece's information
                        piece_in_new_spot.captured(self.get_pieces())

                    # Update board positions
                    #   1. Make previous spot blank
                    self._board[current_pos[0]][current_pos[1]] = Piece()

                    #   2. Change new position to hold moving piece
                    moving_piece.update_position(new_pos)
                    self._board[new_pos[0]][new_pos[1]] = moving_piece

                    # Prevent player from making a move that puts themselves in check
                    if self.is_in_check(self.get_turn()):

                        if self._CLI_mode:
                            print('Cannot put self in check!')

                        # Undo board changes
                        if capture_move:
                            # Undo Add captured piece to captured pieces list

                            self._captured_pieces.remove(piece_in_new_spot)
                            # Undo Update captured piece's information
                            piece_in_new_spot.undo_capture()

                        # Undo Update board positions
                        self._board[current_pos[0]][current_pos[1]] = moving_piece
                        moving_piece.update_position(current_pos)

                        self._board[new_pos[0]][new_pos[1]] = piece_in_new_spot
                        piece_in_new_spot.update_position(new_pos)

                        return False

                    self.add_turn()

                    if self._CLI_mode and self.is_in_check(self.get_turn()):
                        print(self.get_turn().title(), 'in check!')

                    # Update game state by checking if there is a checkmate or stalemate
                    if self.check_for_checkmate_stalemate(self.get_turn()):
                        self._turn -= 1
                        self.update_game_state(self.get_turn())
                        if self._CLI_mode:
                            print(self.get_game_state())

                    # For debugging:
                    self._rcheck = self.is_in_check('red')
                    self._bcheck = self.is_in_check('black')

                    return True

                else:
                    return False
            else:
                return False
        else:
            return False

    def print_board(self):
        """Prints a representation of the current game board"""

        def print_red(piece):
            """Print red pieces in RED"""
            print("\033[37;1;41m{}\033[000000m".format(piece), end="")

        def print_black(piece):
            """Print black pieces in YELLOW (for dark themed consoles)"""
            print("\033[39;1;47m{}\033[000000m".format(piece), end="")

        def print_connections(rank):
            """Print ASCII representation of spaces between positions on the board"""

            intersections = ' |   |   |   |   |   |   |   |   |'
            intersections_b = ' |   |   |   | / | \\ |   |   |   |'
            intersections_a = ' |   |   |   | \\ | / |   |   |   |'

            print(' \t' + str(rank))
            if rank in [1, 8]:
                print(intersections_a)
            elif rank in [2, 9]:
                print(intersections_b)
            elif rank in [5, 10]:
                return None
            else:
                print(intersections)

        # Print file row
        print()
        files = 'abcdefghi'
        for file in files:
            print(' ' + file, end='  ')
        print("\n")

        # Print half of board
        for i in range(5):
            for j in range(8):
                if self._board[i][j].get_color() == 'red':
                    print_red(str(self._board[i][j].get_title()))
                elif self._board[i][j].get_color() == 'black':
                    print_black(str(self._board[i][j].get_title()))
                else:
                    print('[ ]', end='')
                print('-', end="")

            if self._board[i][8].get_color() == 'red':
                print_red(str(self._board[i][8].get_title()))
            elif self._board[i][8].get_color() == 'black':
                print_black(str(self._board[i][8].get_title()))
            else:
                print('[ ]', end='')

            print(' ', end='')
            print_connections(i + 1)

        # Print River
        print("\033[34;1m {}\033[00m".format(str(' ' * 14) + 'RIVER'))

        # Print half of board
        for i in range(5, 10):
            for j in range(8):
                if self._board[i][j].get_color() == 'red':
                    print_red(str(self._board[i][j].get_title()))
                elif self._board[i][j].get_color() == 'black':
                    print_black(str(self._board[i][j].get_title()))
                else:
                    print('[ ]', end='')
                print('-', end='')

            if self._board[i][8].get_color() == 'red':
                print_red(str(self._board[i][8].get_title()))
            elif self._board[i][8].get_color() == 'black':
                print_black(str(self._board[i][8].get_title()))
            else:
                print('[ ]', end='')
            print_connections(i + 1)

    def hlpr_list_moves(self, position):
        if self._helper_mode:
            piece = self._board[position[0]][position[1]]
            avail_moves = piece.get_moves()
            legal_moves = [x for x in avail_moves if self.check_move(position, x)]
            legal_moves.sort()

            print(legal_moves)

        else:
            return False



def main():
    return True


if __name__ == '__main__':
    main()
