from sudoku.modules.generator import Generator
from sudoku.algorithms.algorithms import Algortihms
from sudoku.algorithms.backtracking import Backtracking

import pprint

class Solver:

    @staticmethod
    def get_solved_board(size: int, alg: int) -> list:
        #TODO: Check Sudoku board sizes. 4x4, 6x6, 9x9 ... Not all sizes are allowed.
        '''
        Generates a solved Sudoku board.

        Parameters:
        size (int): Size of the Sudoku board (size x size).
        alg (int): Chosen algorithm. See sudoku.algorithms.available

        Returns:
        list: Solved Sudoku board as a 2D list.
        '''
        if(alg == Algortihms.BACKTRACKING):
            return Backtracking.solve(Generator.get_unsolved_board(size))

    @staticmethod
    def print_board(board: list):
        pprint.pprint(board)