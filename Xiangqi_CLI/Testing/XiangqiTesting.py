# Author: Marissa Castillo
# Date: 03/03/2020
# Description: A text-based program of the game Xiangqi- a battle between two armies with the goal of capturing the
#               enemy's general. This file includes Unit testing for Xiangqi Game

import unittest
from Xiangqi import XiangqiGame

print()

class TestProjects(unittest.TestCase):

    def test_helper(self):
        """Test helper mode"""

        part_game = XiangqiGame()
        part_game.set_debug_mode(True)
        part_game.set_helper_mode(True)

        moves = part_game.hlpr_list_moves([0,0])

        print(moves)
        self.assertEqual(['a2', 'a3'], moves)

        part_game.print_board()

    def test_quick_game(self):
        """Test full game with two checks"""

        fullgame = XiangqiGame()
        fullgame.set_CLI_mode(True)

        move = fullgame.make_move('i1', 'i2')
        move = fullgame.make_move('h8', 'h1')

        move = fullgame.make_move('c1', 'e3')
        move = fullgame.make_move('b10', 'c8')

        move = fullgame.make_move('e4', 'e5')
        move = fullgame.make_move('h10', 'g8')

        move = fullgame.make_move('e5', 'e6')
        move = fullgame.make_move('e7', 'e6')

        move = fullgame.make_move('g4', 'g5')
        move = fullgame.make_move('e6', 'e5')

        move = fullgame.make_move('e3', 'c5')
        move = fullgame.make_move('i10', 'h10')

        move = fullgame.make_move('b3', 'd3')
        move = fullgame.make_move('h10', 'h3')

        move = fullgame.make_move('a1', 'a2')
        move = fullgame.make_move('h3', 'd3')

        move = fullgame.make_move('a2', 'b2')
        move = fullgame.make_move('a10', 'b10')

        move = fullgame.make_move('d1', 'e2')
        move = fullgame.make_move('d3', 'g3')

        move = fullgame.make_move('a4', 'a5')
        move = fullgame.make_move('g3', 'g1')

        move = fullgame.make_move('e1', 'd1')
        move = fullgame.make_move('g1', 'g2')   # Check

        fullgame.print_board()
        rcheck1 = fullgame.is_in_check('red')
        rcheckmate1 = fullgame.check_for_checkmate_stalemate('red')

        self.assertFalse(rcheckmate1)
        self.assertTrue(rcheck1)

        move = fullgame.make_move('d1', 'd2')
        move = fullgame.make_move('g2', 'i2')

        move = fullgame.make_move('b2', 'c2')
        move = fullgame.make_move('h1', 'h2')   # Check

        fullgame.print_board()
        rcheck2 = fullgame.is_in_check('red')
        rcheckmate2 = fullgame.check_for_checkmate_stalemate('red')

        self.assertFalse(rcheckmate2)
        self.assertTrue(rcheck2)

        move = fullgame.make_move('d2', 'd1')
        move = fullgame.make_move('h2', 'c2')

        move = fullgame.make_move('b1', 'd2')
        move = fullgame.make_move('i2', 'i4')

        move = fullgame.make_move('c5', 'e3')
        move = fullgame.make_move('b8', 'b3')

        move = fullgame.make_move('d1', 'e1')
        move = fullgame.make_move('b3', 'd3')

        move = fullgame.make_move('e2', 'd3')
        move = fullgame.make_move('b10', 'b1')

        bwin = fullgame.get_game_state()
        rcheck = fullgame.is_in_check('red')
        bcheck = fullgame.is_in_check('black')

        fullgame.print_board()

        self.assertTrue(move)
        self.assertEqual(bwin, 'BLACK_WON')
        self.assertTrue(rcheck)
        self.assertFalse(bcheck)

    def test_full_game(self):
        """Test full game"""
        
        fullgame = XiangqiGame()
        
        fullgame.make_move('b3', 'e3')
        fullgame.make_move('b8', 'e8')

        fullgame.make_move('b1', 'c3')
        fullgame.make_move('b10', 'c8')

        fullgame.make_move('a1', 'b1')
        fullgame.make_move('a10', 'a9')

        fullgame.make_move('h1', 'g3')
        fullgame.make_move('a9', 'f9')

        fullgame.make_move('c4', 'c5')
        fullgame.make_move('h10', 'g8')

        fullgame.make_move('g4', 'g5')
        fullgame.make_move('i10', 'i9')

        fullgame.make_move('g1', 'i3')
        fullgame.make_move('f9', 'f6')

        fullgame.make_move('i1', 'i2')
        fullgame.make_move('i9', 'd9')

        fullgame.make_move('b1', 'b7')
        fullgame.make_move('c7', 'c6')

        fullgame.make_move('b7', 'c7')
        fullgame.make_move('f6', 'f4')

        fullgame.make_move('d1', 'e2')
        fullgame.make_move('f4', 'g4')

        fullgame.make_move('i2', 'g2')
        fullgame.make_move('d9', 'd8')

        fullgame.make_move('c5', 'c6')
        fullgame.make_move('g7', 'g6')

        fullgame.make_move('c6', 'd6')
        fullgame.make_move('g6', 'g5')

        fullgame.make_move('d6', 'd7')
        fullgame.make_move('d8', 'd9')

        fullgame.make_move('e3', 'd3')
        fullgame.make_move('d9', 'f9')

        fullgame.make_move('d3', 'd4')
        move = fullgame.make_move('e8', 'e4')  # Check

        fullgame.print_board()
        red_check = fullgame.is_in_check('red')
        red_checkmate = fullgame.check_for_checkmate_stalemate('red')
        captures = fullgame.opposing_can_be_captured('red')

        self.assertTrue(captures)
        self.assertTrue(move)
        self.assertFalse(red_checkmate)
        self.assertTrue(red_check)

        red_move = fullgame.make_move('c3', 'e4')

        red_check2 = fullgame.is_in_check('red')
        self.assertTrue(red_move)
        self.assertFalse(red_check2)

        move = fullgame.make_move('f10', 'e9')

        move = fullgame.make_move('i3', 'g5')
        move = fullgame.make_move('g4', 'g3')

        move = fullgame.make_move('g2', 'g3')
        move = fullgame.make_move('f9', 'f10')

        move = fullgame.make_move('d4', 'c4')
        move = fullgame.make_move('f10', 'f8')

        move = fullgame.make_move('g3', 'b3')
        move = fullgame.make_move('e7', 'e6')

        move = fullgame.make_move('b3', 'b8')
        move = fullgame.make_move('e6', 'e5')

        move = fullgame.make_move('e4', 'c5')
        move = fullgame.make_move('g8', 'f6')

        move = fullgame.make_move('c5', 'e6')
        move = fullgame.make_move('f8', 'e8')

        move = fullgame.make_move('c7', 'c8')
        move = fullgame.make_move('e8', 'c8')

        move = fullgame.make_move('b8', 'c8')
        move = fullgame.make_move('c10', 'e8')

        move = fullgame.make_move('c8', 'c9')
        move = fullgame.make_move('h8', 'h10')

        move = fullgame.make_move('g5', 'e3')
        move = fullgame.make_move('h10', 'h4')

        move = fullgame.make_move('c9', 'd9')
        move = fullgame.make_move('h4', 'a4')

        move = fullgame.make_move('c4', 'c10')

        fullgame.print_board()

        did_red_win = fullgame.get_game_state()
        is_checkmate = fullgame.check_for_checkmate_stalemate('black')
        b_check = fullgame.is_in_check('black')

        self.assertTrue(b_check)
        self.assertTrue(is_checkmate)
        self.assertEqual(did_red_win, 'RED_WON')

    def test_face_gen(self):
        """Test that Soldier cannot move out of file, resulting in Generals facing one another"""
        
        part_game = XiangqiGame()
        
        part_game.make_move('e1', 'e2')
        part_game.make_move('e7', 'e6')
        part_game.make_move('e2', 'd2')
        part_game.make_move('e6', 'e5')
        part_game.make_move('d2', 'd3')
        part_game.make_move('e5', 'd5')
        part_game.make_move('e4', 'e5')
        part_game.make_move('e10', 'e9')
        part_game.make_move('d3', 'e3')
        part_game.make_move('d5', 'e5')
        part_game.make_move('e3', 'e2')
        
        face_gen = part_game.make_move('e5', 'f5')
        empty_piece = part_game.make_move('i2', 'i3')

        self.assertFalse(face_gen)
        self.assertFalse(empty_piece)

    def test_face_gen_2(self):
        """Test that the General cannot make a move that results in Generals facing each other"""
        
        part_game = XiangqiGame()
        
        part_game.make_move('e1', 'e2')
        part_game.make_move('e10', 'e9')
        part_game.make_move('e2', 'd2')
        part_game.make_move('e7', 'e6')
        part_game.make_move('d2', 'd3')
        part_game.make_move('e6', 'e5')
        part_game.make_move('d3', 'd2')
        
        face_gen = part_game.make_move('e9', 'd9')

        self.assertFalse(face_gen)

    def test_capture(self):
        """Test capture method with Soldier's horizontal moves"""
        
        part_game = XiangqiGame()
        
        part_game.make_move('e1', 'e2')
        part_game.make_move('e7', 'e6')

        part_game.make_move('e2', 'd2')
        part_game.make_move('e6', 'e5')

        part_game.make_move('d2', 'd3')
        part_game.make_move('e5', 'd5')

        part_game.make_move('e4', 'e5')
        part_game.make_move('e10', 'e9')

        part_game.make_move('e5', 'e6')
        part_game.make_move('e9', 'd9')

        part_game.make_move('e6', 'e7')
        face_gen = part_game.make_move('d5', 'e5')
        part_game.make_move('d9', 'e9')

        part_game.make_move('e7', 'f7')
        part_game.make_move('g10', 'e8')

        capture = part_game.make_move('f7', 'g7') # Soldier capture

        black_pieces = len(part_game.get_pieces('black'))
        red_pieces = len(part_game.get_pieces('red'))

        part_game.print_board()

        self.assertFalse(face_gen)
        self.assertTrue(capture)
        self.assertEqual(black_pieces, 15)
        self.assertEqual(red_pieces, 16)

    def test_pieces(self):
        """Basic test of Red pieces moving"""

        part_game = XiangqiGame()
        part_game.set_debug_mode(True)

        # Cannon
        part_game.make_move('b8', 'e8')
        part_game.make_move('h3', 'h5')
        part_game.make_move('b3', 'b2')
        part_game.make_move('b2', 'd2')

        # Advisor
        part_game.make_move('f1', 'e2')
        part_game.make_move('e2', 'd3')
        ad_false = part_game.make_move('d3', 'c2')

        # Rook
        part_game.make_move('a1', 'a2')
        part_game.make_move('a2', 'i2')
        part_game.make_move('a10', 'a9')
        part_game.make_move('i2', 'f2')
        part_game.make_move('f2', 'f4')
        part_game.make_move('d3', 'e2')

        # Horse
        part_game.make_move('b1', 'a3')
        part_game.make_move('a3', 'c2')
        false_horse = part_game.make_move('h1', 'f2')
        self.assertFalse(false_horse)

        # Elephant
        part_game.make_move('c1', 'a3')
        part_game.make_move('a3', 'c5')
        part_game.make_move('g1', 'e3')

        part_game.make_move('h1', 'i3')

        # Soldier
        part_game.make_move('e7', 'e6')
        part_game.make_move('e6', 'e5')
        part_game.make_move('e5', 'd5')
        part_game.make_move('d5', 'd4')
        part_game.make_move('d4', 'd3')

        # General
        part_game.make_move('e1', 'f1')
        gen_false = part_game.make_move('f1', 'g1')

        part_game.make_move('e2', 'f3')
        part_game.make_move('d2', 'e2')

        part_game.make_move('e2', 'e1')
        part_game.make_move('a9', 'f9')
        part_game.make_move('f9', 'f4')
        part_game.add_turn()
        part_game.make_move('e8', 'e3')
        part_game.add_turn()
        part_game.make_move('f4', 'f3')

        print(part_game.check_for_checkmate_stalemate('red'))
        print(part_game.is_in_check('red'))

        part_game.print_board()

        self.assertFalse(ad_false)
        self.assertFalse(gen_false)

    def test_pieces_2(self):
        part_game = XiangqiGame()
        
        soldier_false = part_game.make_move('i4', 'h4')
        self.assertFalse(soldier_false)
        part_game.make_move('c4', 'c5')
        part_game.make_move('e10', 'e9')

        part_game.make_move('c5', 'c6')
        part_game.make_move('g10', 'e8')

        part_game.make_move('e1', 'e2')
        capture = part_game.make_move('e8', 'c6')

        red_pieces = len(part_game.get_pieces('red'))
        black_pieces = len(part_game.get_pieces('black'))

        part_game.make_move('e2', 'f2')
        river = part_game.make_move('c6', 'e4')  # False
        part_game.make_move('e7', 'e6')

        ele_jump = part_game.make_move('g1', 'e3')  # False
        # horses
        part_game.make_move('b1', 'c3')
        part_game.make_move('b10', 'c8')

        part_game.make_move('c3', 'e2')
        horse_jump = part_game.make_move('c8', 'b6')  # False
        part_game.make_move('e6', 'e5')

        part_game.make_move('b3', 'e3')
        part_game.make_move('a10', 'a9')

        part_game.make_move('e3', 'e5')
        puts_in_check_1 = part_game.make_move('c6', 'e8')
        b_in_check = part_game.is_in_check('black')
        part_game.make_move('c6', 'a8')

        part_game.make_move('i4', 'i5')
        part_game.make_move('e9', 'e10')

        part_game.make_move('e2', 'f4')
        puts_in_check = part_game.make_move('d10', 'e9')

        part_game.print_board()

        self.assertFalse(puts_in_check_1)
        self.assertFalse(puts_in_check)
        self.assertTrue(capture)
        self.assertEqual(red_pieces, 15)
        self.assertEqual(black_pieces, 16)
        self.assertFalse(river)
        self.assertFalse(ele_jump)
        self.assertFalse(horse_jump)
        self.assertFalse(b_in_check)
