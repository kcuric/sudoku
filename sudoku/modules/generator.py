from sudoku.entities.board import Board
import random
import math

class Generator:        

    @staticmethod
    def get_unsolved_board(order: int) -> list:
        '''
        Generates an empty board and then it
        populates the "diagonal clusters" of the board with random
        numbers. Definition of the "diagonal cluster" can be found
        in the README file.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: Semi populated Sudoku board as a 2D list.
        '''
        
        board = list()
        for _ in range(order):
            board.append([0 for x in range(order)])

        cell_num = math.pow(order, 2)
        cluster_order = int(math.sqrt(order))

        for cluster in range(cluster_order):
            possible_numbers = list([x for x in range(1, order + 1)])
            possible_numbers = random.sample(possible_numbers, order)
            for i in range(cluster_order):
                for j in range(cluster_order):
                    if possible_numbers:
                        board[i + cluster_order * cluster][j + cluster_order * cluster] = possible_numbers.pop()
                        
        return board

