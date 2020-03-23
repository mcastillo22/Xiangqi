# Author: Marissa Castillo
# Date: 03/03/2020
# Description: A text-based program of the game Xiangqi- a battle between two armies with the goal of capturing the
#               enemy's general. This file includes Unit testing for Xiangqi Game

import unittest
from Xiangqi import XiangqiGame


game1 = XiangqiGame()
game1.print_board()


class TestProjects(unittest.TestCase):
    def test_1(self):
        checkr = game1.is_in_check('red')
        game1.make_move('e1', 'f1')
        game1.print_board()

    def test_beg(self):
        fullgame = XiangqiGame()
        fullgame.make_move('b3', 'e3')
        fullgame.make_move('b10', 'c8')
        fullgame.make_move('b1', 'c3')
        fullgame.make_move('a10', 'b10')
        fullgame.make_move('a1', 'b1')
        fullgame.make_move('h10', 'g8')
        fullgame.make_move('h1', 'i3')
        fullgame.make_move('c7', 'c6')
        fullgame.make_move('b1', 'b7')
        fullgame.make_move('c8', 'd6')
        fullgame.make_move('i1', 'i2')
        fullgame.make_move('g10', 'e8')
        fullgame.make_move('h3', 'f3')
        fullgame.make_move('c6', 'c5')
        fullgame.make_move('b7', 'b6')
        move = fullgame.make_move('d6', 'c4')

        self.assertTrue(move)

    def test_full(self):
        full = XiangqiGame()

        full.make_move('c4', 'c5')
        full.make_move('c10', 'e8')

        full.make_move('b3', 'd3')
        full.make_move('g7', 'g6')

        full.make_move('b1', 'c3')
        full.make_move('h10', 'g8')

        full.make_move('a1', 'b1')
        full.make_move('b10', 'd9')

        full.make_move('h3', 'e3')
        full.make_move('g8', 'f6')

        full.make_move('h1', 'g3')
        full.make_move('a10', 'b10')

        full.make_move('b1', 'b6')
        full.make_move('f6', 'g4')

        full.make_move('i1', 'i2')
        full.make_move('g4', 'e3')

        full.make_move('g1', 'e3')
        full.make_move('i10', 'i9')

        full.make_move('c3', 'd5')
        full.make_move('i9', 'g9')

        full.make_move('d3', 'd9')
        full.make_move('g9', 'd9')
        full.make_move('i2', 'd2')
        full.make_move('h8', 'h6')
        full.make_move('b6', 'b7')
        full.make_move('e7', 'e6')
        full.make_move('f1', 'e2')
        full.make_move('d10', 'e9')
        full.make_move('d2', 'd3')
        full.make_move('g6', 'g5')
        full.make_move('e3', 'g5')
        full.make_move('c7', 'c6')
        full.make_move('d5', 'c7')
        full.make_move('d9', 'd3')
        full.make_move('e2', 'd3')
        full.make_move('c6', 'c5')
        full.make_move('c7', 'd9')
        full.make_move('b10', 'd10')
        full.make_move('d9', 'b8')
        full.make_move('d10', 'd3')
        full.make_move('b8', 'd7')
        full.make_move('e10', 'd10')
        full.make_move('g3', 'h5')
        full.make_move('d3', 'h3')
        full.make_move('h5', 'i3')
        full.make_move('h6', 'h4')
        full.make_move('d7', 'c9')
        full.make_move('e9', 'd8')

        full.make_move('b7', 'h7')
        full.make_move('c5', 'd5')
        full.make_move('c9', 'b7')
        full.make_move('h3', 'i3')
        full.make_move('h7', 'h4')
        full.make_move('f10', 'e9')
        full.make_move('h4', 'f4')
        full.make_move('i3', 'i1')
        full.make_move('f4', 'f1')
        full.make_move('i1', 'i4')
        full.make_move('g5', 'e3')
        full.make_move('i7', 'i6')
        full.make_move('f1', 'f6')
        full.make_move('i4', 'e4')

        full.make_move('f6', 'i6')
        full.make_move('e4', 'h4')
        full.make_move('d1', 'e2')
        full.make_move('h4', 'e4')
        full.make_move('a4', 'a5')
        full.make_move('e6', 'e5')
        full.make_move('i6', 'h6')
        full.make_move('e4', 'c4')
        full.make_move('h6', 'b6')
        full.make_move('d10', 'e10')
        full.make_move('c1', 'a3')
        full.make_move('c4', 'c3')
        full.make_move('e3', 'c1')
        full.make_move('e5', 'e4')
        full.make_move('b7', 'd6')
        full.make_move('c3', 'c6')
        full.make_move('b6', 'c6')
        full.make_move('e8', 'c6')

        full.make_move('d6', 'c8')
        full.make_move('e4', 'f4')
        full.make_move('c8', 'a7')
        full.make_move('c6', 'e8')
        full.make_move('a7', 'c8')
        full.make_move('f4', 'g4')
        full.make_move('c8', 'd6')
        full.make_move('d5', 'e5')
        full.make_move('a5', 'a6')
        full.make_move('g4', 'g3')
        full.make_move('d6', 'f7')
        full.make_move('e5', 'e4')

        full.make_move('a6', 'b6')
        full.make_move('e4', 'd4')
        full.make_move('a3', 'c5')
        full.make_move('e10', 'f10')
        full.make_move('b6', 'b7')
        full.make_move('g3', 'g2')
        full.make_move('b7', 'b8')
        full.make_move('d4', 'c4')
        full.make_move('b8', 'c8')
        full.make_move('c4', 'c3')
        full.make_move('f7', 'g5')
        full.make_move('g10', 'i8')
        full.make_move('c8', 'c9')
        full.make_move('e8', 'g6')
        full.make_move('c9', 'd9')
        full.make_move('f10', 'e10')
        full.make_move('e2', 'f1')
        full.make_move('g6', 'e8')
        full.make_move('g5', 'h7')
        full.make_move('i8', 'g10')
        full.make_move('e1', 'd1')
        full.make_move('g2', 'f2')
        full.make_move('c1', 'a3')
        full.make_move('c3', 'd3')
        full.make_move('h7', 'g5')
        full.make_move('e8', 'c6')
        full.make_move('a3', 'c1')
        full.make_move('g10', 'e8')
        full.make_move('g5', 'e4')
        full.make_move('f2', 'f1')

        full.make_move('c5', 'e3')
        full.make_move('e8', 'g10')
        full.make_move('e4', 'g3')
        full.make_move('f1', 'e1')
        full.make_move('d1', 'e1')
        full.make_move('e9', 'd10')
        full.make_move('g3', 'e4')
        full.make_move('g10', 'e8')
        full.make_move('e3', 'g5')
        full.make_move('c6', 'a8')
        full.make_move('e1', 'd1')
        full.make_move('d8', 'e9')
        full.make_move('e4', 'c5')
        full.make_move('d3', 'c3')
        full.make_move('c1', 'e3')
        full.make_move('e10', 'f10')
        full.make_move('c5', 'e4')
        full.make_move('c3', 'd3')
        full.make_move('d1', 'e1')
        full.make_move('a8', 'c6')
        full.make_move('e4', 'f6')
        full.make_move('d3', 'd2')
        full.make_move('e3', 'c5')
        full.make_move('f10', 'e10')
        full.make_move('f6', 'e4')
        full.make_move('d2', 'c2')
        full.make_move('g5', 'e3')
        full.make_move('c2', 'd2')
        full.make_move('e4', 'd6')
        full.make_move('e9', 'd8')

        full.make_move('c5', 'a3')
        full.make_move('d10', 'e9')
        full.make_move('d6', 'c4')
        full.make_move('d2', 'c2')
        full.make_move('e1', 'd1')
        full.make_move('c6', 'a8')
        full.make_move('c4', 'd6')
        full.make_move('e8', 'g6')
        full.make_move('d6', 'f5')
        full.make_move('g6', 'i8')
        full.make_move('a3', 'c1')
        full.make_move('e10', 'f10')
        full.make_move('f5', 'd4')
        full.make_move('c2', 'b2')
        full.make_move('e3', 'g5')
        full.make_move('e9', 'f8')
        full.make_move('c1', 'e3')
        full.make_move('d8', 'e9')
        full.make_move('d1', 'e1')
        full.make_move('i8', 'g10')
        full.make_move('e1', 'f1')
        full.make_move('f10', 'e10')
        full.make_move('g5', 'i3')
        a = full.make_move('g10', 'i8')

        self.assertTrue(a)

    def test_full_game(self):
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
        a = fullgame.make_move('e8', 'e4')  # Check

        fullgame.print_board()
        red_check = fullgame.is_in_check('red')
        checkmate_red = fullgame.check_for_checkmate_stalemate('red')
        captures = fullgame.opposing_can_be_captured('red')

        self.assertTrue(captures)
        self.assertTrue(a)
        self.assertFalse(checkmate_red)
        self.assertTrue(red_check)

        red_move = fullgame.make_move('c3', 'e4')

        red_check_2 = fullgame.is_in_check('red')
        self.assertTrue(red_move)
        self.assertFalse(red_check_2)

        a = fullgame.make_move('f10', 'e9')

        a = fullgame.make_move('i3', 'g5')
        a = fullgame.make_move('g4', 'g3')

        a = fullgame.make_move('g2', 'g3')
        a = fullgame.make_move('f9', 'f10')

        a = fullgame.make_move('d4', 'c4')
        a = fullgame.make_move('f10', 'f8')

        a = fullgame.make_move('g3', 'b3')
        a = fullgame.make_move('e7', 'e6')

        a = fullgame.make_move('b3', 'b8')
        a = fullgame.make_move('e6', 'e5')

        a = fullgame.make_move('e4', 'c5')
        a = fullgame.make_move('g8', 'f6')

        a = fullgame.make_move('c5', 'e6')
        a = fullgame.make_move('f8', 'e8')

        a = fullgame.make_move('c7', 'c8')
        a = fullgame.make_move('e8', 'c8')

        a = fullgame.make_move('b8', 'c8')
        a = fullgame.make_move('c10', 'e8')

        a = fullgame.make_move('c8', 'c9')
        a = fullgame.make_move('h8', 'h10')

        a = fullgame.make_move('g5', 'e3')
        a = fullgame.make_move('h10', 'h4')

        a = fullgame.make_move('c9', 'd9')
        a = fullgame.make_move('h4', 'a4')

        a = fullgame.make_move('c4', 'c10')

        #fullgame.print_board()

        did_red_won = fullgame.get_game_state()
        is_checkmate = fullgame.check_for_checkmate_stalemate('black')
        in_check = fullgame.is_in_check('black')

        self.assertTrue(in_check)
        self.assertTrue(is_checkmate)
        self.assertEqual(did_red_won, 'RED_WON')

    def test_face_gen(self):
        """Test that Soldier cannot move out of file, resulting in Generals facing one another"""
        game1 = XiangqiGame()
        game1.make_move('e1', 'e2')
        game1.make_move('e7', 'e6')
        game1.make_move('e2', 'd2')
        game1.make_move('e6', 'e5')
        game1.make_move('d2', 'd3')
        game1.make_move('e5', 'd5')
        game1.make_move('e4', 'e5')
        game1.make_move('e10', 'e9')
        game1.make_move('d3', 'e3')
        game1.make_move('d5', 'e5')
        game1.make_move('e3', 'e2')
        face_gen = game1.make_move('e5', 'f5')
        empty_piece = game1.make_move('i2', 'i3')

        self.assertFalse(face_gen)
        self.assertFalse(empty_piece)

    def test_face_gen_2(self):
        """Test that the General cannot make a move that results in Generals facing each other"""
        game1 = XiangqiGame()
        game1.make_move('e1', 'e2')
        game1.make_move('e10', 'e9')
        game1.make_move('e2', 'd2')
        game1.make_move('e7', 'e6')
        game1.make_move('d2', 'd3')
        game1.make_move('e6', 'e5')
        game1.make_move('d3', 'd2')
        face_gen = game1.make_move('e9', 'd9')

        self.assertFalse(face_gen)

    def test_capture(self):
        game1 = XiangqiGame()
        game1.make_move('e1', 'e2')
        game1.make_move('e7', 'e6')

        game1.make_move('e2', 'd2')
        game1.make_move('e6', 'e5')

        game1.make_move('d2', 'd3')
        game1.make_move('e5', 'd5')

        game1.make_move('e4', 'e5')
        game1.make_move('e10', 'e9')

        game1.make_move('e5', 'e6')
        game1.make_move('e9', 'd9')

        game1.make_move('e6', 'e7')
        face_gen = game1.make_move('d5', 'e5')
        game1.make_move('d9', 'e9')

        game1.make_move('e7', 'f7')
        game1.make_move('g10', 'e8')

        capture = game1.make_move('f7', 'g7')

        black_pieces = len(game1.get_pieces('black'))
        red_pieces = len(game1.get_pieces('red'))

        game1.print_board()

        self.assertFalse(face_gen)
        self.assertTrue(capture)
        self.assertEqual(black_pieces, 15)
        self.assertEqual(red_pieces, 16)

    def cannon_check(self):
        game1 = XiangqiGame()
        game1.make_move('b3', 'b7')
        game1.make_move('c10', 'e8')

        true1 = game1.make_move('b7', 'b10')  # Check move
        in_check = game1.is_in_check('black')
        in_checkm = game1.check_for_checkmate_stalemate('black')
        in_check_r = game1.is_in_check('red')
        game1.make_move('e10', 'e9')

        move_l = game1.make_move('b10', 'f10')

        self.assertTrue(true1)
        self.assertTrue(in_check)
        self.assertFalse(in_checkm)
        self.assertFalse(in_check_r)
        self.assertTrue(move_l)

    def test_jump(self):
        game1 = XiangqiGame()
        soldier_false = game1.make_move('i4', 'h4')
        self.assertFalse(soldier_false)
        game1.make_move('c4', 'c5')
        game1.make_move('e10', 'e9')

        game1.make_move('c5', 'c6')
        game1.make_move('g10', 'e8')

        game1.make_move('e1', 'e2')
        capture = game1.make_move('e8', 'c6')

        red_pieces = len(game1.get_pieces('red'))
        black_pieces = len(game1.get_pieces('black'))

        game1.make_move('e2', 'f2')
        river = game1.make_move('c6', 'e4')  # False
        game1.make_move('e7', 'e6')

        ele_jump = game1.make_move('g1', 'e3')  # False
        # horses
        game1.make_move('b1', 'c3')
        game1.make_move('b10', 'c8')

        game1.make_move('c3', 'e2')
        horse_jump = game1.make_move('c8', 'b6')  # False
        game1.make_move('e6', 'e5')

        game1.make_move('b3', 'e3')
        game1.make_move('a10', 'a9')

        game1.make_move('e3', 'e5')
        puts_in_check_1 = game1.make_move('c6', 'e8')
        b_in_check = game1.is_in_check('black')
        game1.make_move('c6', 'a8')

        game1.make_move('i4', 'i5')
        game1.make_move('e9', 'e10')

        game1.make_move('e2', 'f4')
        puts_in_check = game1.make_move('d10', 'e9')

        game1.print_board()

        self.assertFalse(puts_in_check_1)
        self.assertFalse(puts_in_check)
        self.assertTrue(capture)
        self.assertEqual(red_pieces, 15)
        self.assertEqual(black_pieces, 16)
        self.assertFalse(river)
        self.assertFalse(ele_jump)
        self.assertFalse(horse_jump)
        self.assertFalse(b_in_check)
