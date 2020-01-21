import pprint
import random

class Sudoku:

    board = list()

    def get_empty_board(self, size: int) -> list:
        #TODO: Check Sudoku board sizes. 4x4, 6x6, 9x9 ... Not all sizes are allowed.
        '''
        Generates an empty Sudoku board.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: An empty Sudoku board as a 2D list.
        '''
        self.board = list()
        for _ in range(size):
            self.board.append([0 for x in range(size)])
        return self.board

    def get_solved_board(self, size: int) -> list:
        #TODO: Check Sudoku board sizes. 4x4, 6x6, 9x9 ... Not all sizes are allowed.
        '''
        Generates a solved Sudoku board.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: Solved Sudoku board as a 2D list.
        '''
        self.get_empty_board(size)
        self.board = self._populate_diagonal(size)
        return self._solve(self.board)
        
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
        self.possible_numbers_count = self.num_sectors * self.num_sectors
        for cluster in range(self.divider):
            self.possible_numbers = list([x for x in range(1, self.possible_numbers_count + 1)])
            self.possible_numbers = random.sample(self.possible_numbers, self.possible_numbers_count)
            for i in range(self.num_sectors):
                for j in range(self.num_sectors):
                    if self.possible_numbers:
                        self.board[i + self.num_sectors * cluster][j + self.num_sectors * cluster] = self.possible_numbers.pop()
                        
        return self.board

    def _find_empty_field(self, board: list, value=0) -> tuple:
        '''
        Finds an empty field in the Sudoku board if
        it exists and returns the coordinates (index).
        If the empty field doesn't exist than the
        function returns None.

        Parameters:
        board (list): Sudoku board.
        value (int): Value indicating an empty field. 
                    Default = 0

        Returns:
        tuple: (row, column) index of an empty field.
        '''
        for num, row in enumerate(board):
            if value in row:
                return (num, row.index(value))
        return None

    def _valid(self, board: list, entered_value: int, field: tuple) -> bool:
        '''
        Parameters:
        board (list): Sudoku board.
        entered_value (int): Value entered in the empty field.
        field (tuple): (row, column) index of the field where
                    the entered_value was inserted.

        Returns:
        bool: Validation of the entered value.
        '''

        chosen_row = field[0]
        chosen_col = field[1]
        
        # Check row
        for num in board[chosen_row]:
            if num == entered_value:
                return False

        # Check column
        for num in [row[chosen_col] for row in board]:
            if num == entered_value:
                return False

        # Check cluster
        # Find cluster
        size = len(board)
        divider = 2 if size % 2 == 0 else 3
        num_sectors = int(size / divider)
        cluster_beginning = (
            chosen_row // divider * num_sectors, 
            chosen_col // divider * num_sectors
        )

        for row in range(cluster_beginning[0], cluster_beginning[1] + divider):
            for col in range(cluster_beginning[1], cluster_beginning[0] + divider):
                if board[row][col] <= entered_value:
                    return False

        return True

    def _solve(self, board: list) -> list:
        '''
        Solves the Sudoku board using the backtracking
        algorithm.

        Parameters:
        board (list): Sudoku board that needs solving.

        Returns:
        list: Solved Sudoku board as a 2D list.
        '''
        find = self._find_empty_field(board)
        if not find:
            return board
        else:
            row, col = find

        for i in range(1, len(board) + 1):
            if self._valid(board, i, (row, col)):
                board[row][col] = i

                if self._solve(board):
                    return board

                board[row][col] = 0

        return None

    @staticmethod
    def print_board(board: list):
        pprint.pprint(board)