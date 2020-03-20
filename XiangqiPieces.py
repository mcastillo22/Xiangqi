

class Piece:
    """Creates a Piece object for the Xiangqi game class. All pieces inherit from this class.
    A generic Piece will fill blank spaces on the game board."""

    def __init__(self, title='   ', color=None, position=None):
        """Initialize title (what will show on the board when printed), army it belongs to (red or black),
        and position"""

        self._title = title
        self._color = color  # Black or red
        self._position = position  # Position on the board. Is None if captured.
        self._is_captured = False
        self._available_moves = None

    def get_title(self):
        """Returns the Piece's given name. This name appears on the game board when printed to the console."""
        return self._title

    def get_position(self):
        """Returns the Piece's position on the board. This may be None."""
        return self._position

    def get_color(self):
        """Returns whose army the Piece belongs to- Red or Black."""
        return self._color

    def update_position(self, position):
        """Updates the Piece's position to the passed position on the board."""

        new_rank = position[0]
        new_file = position[1]
        self._position = [new_rank, new_file]

    def captured(self, pieces):
        """When a piece is captured, it is removed from the board and its position is reset."""

        search = [piece for piece in pieces if piece.get_position() == self.get_position()]
        pieces.remove(search[0])
        self._position = None
        self._is_captured = True

    def undo_capture(self):
        """If move places player in check, undo capture"""
        self._is_captured = False

    def check_facing_generals(self, pieces, desired_pos):
        """Determines if a proposed move will lead to the Generals facing each other directly.
        If so, returns False and prevents that move from taking place."""

        temp = self.get_position()
        self.update_position(desired_pos)

        # Get Generals' positions on board
        gen_positions = [pos.get_position() for pos in pieces if pos.get_title()[1] == 'G']

        # Check if Generals are on the same file
        if gen_positions[0][1] == gen_positions[1][1] and len(gen_positions) == 2:
            file = gen_positions[0][1]
            pieces_in_file = [piece.get_position()[0] for piece in pieces if piece.get_position()[1] == file]
            gen_positions = [gen[0] for gen in gen_positions]

            # Check if move would put Generals in the same file with no pieces in between
            lo_general = min(gen_positions)
            hi_general = max(gen_positions)
            pieces_between = [piece for piece in pieces_in_file if lo_general < piece < hi_general]

            # If pieces_between is empty, then the Generals have no pieces in between
            if not pieces_between:
                facing_generals = True
            else:
                facing_generals = False

        else:
            facing_generals = False

        self.update_position(temp)
        return not facing_generals

    def move_helper_rc(self, desired_pos, pieces, num, num2, b, b1):
        """Set-up method to determine if Rook/Cannon move is valid"""

        current = self.get_position()[num]

        # Get pieces in the same rank or file
        pieces_in_set = [pis.get_position()[num] for pis in pieces if pis.get_position()[num2] == b
                         and pis.get_position()[num] != b1]
        pieces_in_set.sort()
        lo = min([current, desired_pos[num]])
        hi = max([current, desired_pos[num]])

        # Determine pieces in between current position and desired position
        pieces_in_set = [pis for pis in pieces_in_set if lo < pis < hi]

        # If there are no pieces in between, the move is valid
        if not pieces_in_set:
            return True

        else:
            return False

    def get_moves(self):
        """Returns the Piece's moveset"""
        return self._available_moves

    def move(self, desired_position, pieces):
        """Allows movement for General and Advisor"""

        self.get_moves()

        if desired_position in self._available_moves:
            return self.check_facing_generals(pieces, desired_position)
        else:
            return False


class General(Piece):
    """The desired piece to capture. There is only one General per side.
    Moves one point vertically or horizontally, and cannot face the enemy general directly,
    meaning it cannot move into the same file as the enemy general without >= 1 piece between them).

    Limited to the palace: files d-f (3-5), rank 1-3 (RED)/8-10 (BLACK)

    If a move can be made to capture this Piece, then the player is in check."""

    def __init__(self, title='   ', color=None, position=None):
        super().__init__(title, color, position)

        # Limit movement to the palace
        self._out_of_bound_moves = [[0, 2], [1, 2], [2, 2], [3, 2],
                                    [0, 6], [1, 6], [2, 6], [3, 6],
                                    [3, 3], [3, 4], [3, 5],
                                    [9, 2], [8, 2], [7, 2], [6, 2],
                                    [9, 6], [8, 6], [7, 6], [6, 6],
                                    [6, 3], [6, 4], [6, 5]]

    def get_moves(self):
        """Updates and returns available General moves based on its current position.
        General can move one spot horizontally or vertically."""

        move_set = [[self._position[0], self._position[1] + 1], [self._position[0], self._position[1] - 1],
                    [(self._position[0] + 1), self._position[1]], [(self._position[0] - 1), self._position[1]]]

        self._available_moves = [move for move in move_set if move not in self._out_of_bound_moves]

        return self._available_moves


class Advisor(Piece):
    """Two pieces per side directly next to the General.
    Moves one point diagonally.

    Limited to the palace: files d-f (3-5), rank 1-3 (RED)/8-10 (BLACK)"""

    def __init__(self, title='   ', color=None, position=None):
        super().__init__(title, color, position)

        # Limit movement to the palace
        self._out_of_bound_moves = [[0, 2], [1, 2], [2, 2], [3, 2],
                                    [0, 6], [1, 6], [2, 6], [3, 6],
                                    [3, 3], [3, 4], [3, 5],
                                    [9, 2], [8, 2], [7, 2], [6, 2],
                                    [9, 6], [8, 6], [7, 6], [6, 6],
                                    [6, 3], [6, 4], [6, 5]]

    def get_moves(self):
        """Allows one horizontal or one vertical move based on Advisor's current position."""

        move_set = [[self._position[0] + 1, self._position[1] + 1],
                    [self._position[0] - 1, self._position[1] - 1],
                    [(self._position[0] + 1), self._position[1] - 1],
                    [(self._position[0] - 1), self._position[1] + 1]]

        self._available_moves = [move for move in move_set if move not in self._out_of_bound_moves]

        return self._available_moves


class Elephant(Piece):
    """Two pieces per side next to the Advisors.
    Moves exactly two points in any diagonal direction.
    Cannot jump over pieces or cross the river."""

    def get_moves(self):
        """Returns the moveset for the Elephant"""

        self._available_moves = [[self._position[0] + 2, self._position[1] + 2],
                                 [self._position[0] - 2, self._position[1] - 2],
                                 [(self._position[0] + 2), self._position[1] - 2],
                                 [(self._position[0] - 2), self._position[1] + 2]]

        return self._available_moves

    def move(self, desired_position, pieces):
        """Allows one horizontal or one vertical move"""

        # Do not allow movement past the river
        if self.get_color() == 'red' and desired_position[0] >= 5:
            return False

        if self.get_color() == 'black' and desired_position[0] <= 4:
            return False

        self.get_moves()

        # Prevent Elephant from jumping over other pieces
        lo_rank = min([self.get_position()[0], desired_position[0]])
        lo_file = min([self.get_position()[1], desired_position[1]])

        is_blocking = [pos.get_position() for pos in pieces if pos.get_position() == [lo_rank + 1, lo_file + 1]]

        if desired_position in self._available_moves and not is_blocking:
            return self.check_facing_generals(pieces, desired_position)
        else:
            return False


class Horse(Piece):
    """Two pieces per side next to the Elephants.
    Moves one point orthogonally (h/v) then one point diagonally away from its former position.
    Cannot move over pieces."""

    def get_moves(self):
        """Returns the moveset of the Horse"""

        current_pos = self.get_position()
        rank = current_pos[0]
        file = current_pos[1]

        self._available_moves = [[rank + 2, file + 1], [rank + 2, file - 1], [rank - 2, file + 1], [rank - 2, file - 1],
                                 [rank + 1, file + 2], [rank + 1, file - 2], [rank - 1, file + 2], [rank - 1, file - 2]]

        return self._available_moves

    def move(self, desired_position, pieces):
        """Checks if Horse can move to given position"""

        self.get_moves()

        current_pos = self.get_position()
        rank = current_pos[0]
        file = current_pos[1]

        # Check if there is a blocking piece preventing move
        check_pos = []
        if abs(desired_position[0] - rank) == 2:
            lo = min(desired_position[0], rank)
            check_pos = [lo + 1, file]
        elif abs(desired_position[1] - file) == 2:
            lo = min(desired_position[1], file)
            check_pos = [rank, lo + 1]

        is_blocking = [pos.get_position() for pos in pieces if pos.get_position() == check_pos]

        # Check that Generals will not face each other
        if desired_position in self._available_moves and not is_blocking:
            return self.check_facing_generals(pieces, desired_position)
        else:
            return False


class Rook(Piece):
    """Two pieces per side located at the ends of the board.
    Moves any distance orthogonally and cannot jump over pieces."""

    def move(self, desired_position, pieces):
        """Moves any distance orthogonally, but cannot jump over pieces."""

        current_position = self.get_position()
        rank = current_position[0]
        file = current_position[1]

        # Check if move is horizontal or vertical
        vertical = desired_position[0] != rank and desired_position[1] == file
        horizontal = desired_position[1] != rank and desired_position[0] == rank

        # Check if move is valid
        if vertical:
            valid_move = self.move_helper_rc(desired_position, pieces, 0, 1, file, rank)
        elif horizontal:
            valid_move = self.move_helper_rc(desired_position, pieces, 1, 0, rank, file)
        else:
            return False

        # Check that Generals will not face each other
        if valid_move:
            return self.check_facing_generals(pieces, desired_position)
        else:
            return False


class Cannon(Piece):
    """Two pieces per side located two rows from the General.
    Moves any distance orthogonally. Captures a single piece along its path by jumping over one other piece."""

    def move_helper_cannon(self, desired_pos, pieces, num, num2, b, b1):
        """Helper method to determine if Cannon move is valid"""

        current = self.get_position()[num]

        # Get pieces in the same rank or file
        pieces_in_set = [piece.get_position()[num] for piece in pieces if piece.get_position()[num2] == b
                         and piece.get_position()[num] != b1]
        pieces_in_set.sort()
        lo = min([current, desired_pos[num]])
        hi = max([current, desired_pos[num]])

        # Determine pieces in between current position and desired position
        pieces_in_set = [piece for piece in pieces_in_set if lo < piece < hi]

        # If there are no pieces in between or exactly one piece in between (capture move), the move is valid
        if len(pieces_in_set) == 1:
            return True
        else:
            return False

    def move(self, desired_position, pieces):
        """Moves any distance orthogonally, but can only jump over one piece if making a capture."""

        current_position = self.get_position()
        rank = current_position[0]
        file = current_position[1]
        valid_move = None

        # Check if move is horizontal or vertical
        vertical = desired_position[0] != rank and desired_position[1] == file
        horizontal = desired_position[1] != rank and desired_position[0] == rank

        # Check if move is a capture move
        piece_in_target = [piece.get_color() for piece in pieces if piece.get_position() == desired_position]

        # 1. If moving to an empty spot
        if not piece_in_target:
            if vertical:
                valid_move = self.move_helper_rc(desired_position, pieces, 0, 1, file, rank)
            elif horizontal:
                valid_move = self.move_helper_rc(desired_position, pieces, 1, 0, rank, file)

        # 2. If attempting to capture a piece
        elif len(piece_in_target) == 1:
            if vertical:
                valid_move = self.move_helper_cannon(desired_position, pieces, 0, 1, file, rank)
            elif horizontal:
                valid_move = self.move_helper_cannon(desired_position, pieces, 1, 0, rank, file)
        else:
            return False

        # Check that Generals will not face each other
        if valid_move:
            return self.check_facing_generals(pieces, desired_position)
        else:
            return False


class Soldier(Piece):
    """Five pieces per side. Advances forward by one point (cannot retreat/go backwards).
    Once they cross the river, they can also move horizontally."""

    def __init__(self, title='   ', color=None, position=None):
        super().__init__(title, color, position)
        self._is_past_river = False

    def update_position(self, position):
        """Updates position and takes into account if piece is across the river"""

        new_file = position[1]
        new_rank = position[0]
        self._position = [new_rank, new_file]

        # If soldier has crossed the river, update River Status
        if self.get_position()[0] >= 5 and self.get_color() == 'red':
            self._is_past_river = True

        if self.get_position()[0] <= 4 and self.get_color() == 'black':
            self._is_past_river = True

    def get_moves(self):
        """Allows one move forward. If the piece is past the river, it can move one point horizontally as well."""

        # If soldier is past the river, allow one point horizontal moves
        if self._is_past_river is True:
            self._available_moves = [[self._position[0], self._position[1] + 1],
                                     [self._position[0], self._position[1] - 1]]
        else:
            self._available_moves = []

        # Move-set for red army
        if self.get_color() == 'red':
            self._available_moves.append([(self._position[0] + 1), self._position[1]])

        # Move-set for black army
        elif self.get_color() == 'black':
            self._available_moves.append([(self._position[0] - 1), self._position[1]])
        else:
            return False

        return self._available_moves


def main():
    return True


if __name__ == '__main__':
    main()