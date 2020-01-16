import pprint
import random

class Sudoku:

    board = list()

    def get_empty_board(self, size: int) -> list:
        #TODO: Check Sudoku board sizes. 3x3, 6x6, 9x9 ... Not all sizes are allowed.
        '''
        Generates an empty Sudoku board.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: An empty Sudoku board as a 2D list.
        '''
        for _ in range(size):
            self.board.append([0 for x in range(size)])
        return self.board

    def get_solved_board(self, size: int) -> list:
        #TODO: Check Sudoku board sizes. 3x3, 6x6, 9x9 ... Not all sizes are allowed.
        '''
        Generates a solved Sudoku board.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: Solved Sudoku board as a 2D list.
        '''
        self.board = self._populate_diagonal(size)
        return self.board #replace with (_solve(self.board))
        
    def _populate_diagonal(self, size: int) -> list:
        '''
        Populates the "diagonal" of the board with random
        numbers. Definition of the "diagonal" can be found
        in the README file as well as the explanation for
        this.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: Semi populated Sudoku board as a 2D list.
        '''
        self.divider = 2 if size % 2 == 0 else 3
        self.num_sectors = int(size / self.divider)
        for cluster in range(self.divider):
            self.possible_numbers = list([x for x in range(1, size + 1)])
            self.possible_numbers = random.sample(self.possible_numbers, size)
            for i in range(self.num_sectors):
                for j in range(self.num_sectors):
                    if self.possible_numbers:
                        self.board[i + self.num_sectors * cluster][j + self.num_sectors * cluster] = self.possible_numbers.pop()
        return self.board

    def _solve(self, board: list) -> list:
        '''
        Solves the Sudoku board.

        Parameters:
        board (list): Sudoku board that needs solving.

        Returns:
        list: Solved Sudoku board as a 2D list.
        '''
        
        pass


    @staticmethod
    def print_board(board: list):
        pprint.pprint(board)