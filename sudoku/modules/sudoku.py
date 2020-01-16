import pprint

class Sudoku:

    def __init__(self):
        pass

    def get_empty_board(self, size: int) -> list:
        '''
        Generates an empty sudoku board.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: An empty Sudoku board as a 2D list.
        '''
        self.board = list()
        for _ in range(size):
            self.board.append([0 for x in range(size)])
        return self.board

    @staticmethod
    def print_board(board: list):
        pprint.pprint(board)